from asyncio import Semaphore, gather, wait_for
from json import loads
from pathlib import Path
from socket import AF_INET
from typing import Literal

from aiodns import DNSResolver
from aiodns.error import DNSError
from pycares.errno import ARES_ENOTFOUND

domains_lists_dir = Path(__file__).parent / 'domains'
base_dnsbl_list = domains_lists_dir / 'base_dnsbl_domains.json'
all_dnsbl_list = domains_lists_dir / 'all_dnsbl_domains.json'
base_dnsbl_domains = loads(base_dnsbl_list.read_text())
all_dnsbl_domains = loads(all_dnsbl_list.read_text())


async def check_dnsbl(ip: str, dnsbl_domain: str, resolver: DNSResolver, semaphore: Semaphore, timeout: float) -> dict:
    reverse_ip = '.'.join(ip.split('.')[::-1])
    full_domain = f"{reverse_ip}.{dnsbl_domain}"
    async with semaphore:
        try:
            await wait_for(resolver.gethostbyname(full_domain, AF_INET), timeout)
            await resolver.gethostbyname(full_domain, AF_INET)
            return {'domain': dnsbl_domain, 'result': True}
        except TimeoutError:
            return {'domain': dnsbl_domain, 'result': None}
        except DNSError as e:
            if e.args[0] == ARES_ENOTFOUND:
                return {'domain': dnsbl_domain, 'result': False}
            else:
                return {'domain': dnsbl_domain, 'result': None}
        except:
            return {'domain': dnsbl_domain, 'result': None}


async def dnsbl_check_ip(ip: str, dnsbl: Literal['base', 'all'] = 'base', non_system_dns: bool = False, max_concurrent_requests: int | None = None, timeout: float = 30.0) -> dict:
    """
    асинхронно проверяет ip адрес на наличие в списках dnsbl.

    функция принимает ip адрес и проверяет его в базах dnsbl (dns-based blacklist), можно выбрать базовый или полный список проверок через аргумент `dnsbl` (смысла в полном практически нет, используйте `base`), параметр `non_system_dns` позволяет выбрать несистемные dns серверы, а `max_concurrent_requests` ограничить количество одновременных запросов.

    Args:
        ip (str): ip адрес, который необходимо проверить.
        dnsbl (Literal['base', 'all']): тип списка dnsbl для проверки. принимает значения 'base' или 'all'. по умолчанию 'base'.
        non_system_dns (bool): если True, используются предопределенные dns серверы (1.1.1.1, 77.88.8.8, 8.8.8.8). по умолчанию False.
        max_concurrent_requests (int | None): максимальное количество одновременных запросов. если None, ограничение определяется количеством доменов в списке. по умолчанию None.
        timeout (float): максимальное время ожидания ответа от dns сервера в секундах. по умолчанию 30.0.

    Returns:
        dict: словарь с результатами проверки, включая процентное соотношение ip адресов, найденных в списке dnsbl, общее количество проверенных доменов, количество положительных и отрицательных результатов, а также количество результатов, когда проверка не была завершена из-за таймаута или другой ошибки, и список с полным отчетом от каждого домена в базе dnsbl
    """

    resolver = DNSResolver(['1.1.1.1', '77.88.8.8', '8.8.8.8']) if not non_system_dns else DNSResolver()
    dnsbl_list = all_dnsbl_domains if dnsbl == 'all' else base_dnsbl_domains
    semaphore = Semaphore(max_concurrent_requests if max_concurrent_requests else len(dnsbl_list))
    tasks = [check_dnsbl(ip, domain, resolver, semaphore, timeout) for domain in dnsbl_list]
    results = await gather(*tasks)
    true_count = sum(1 for result in results if result['result'] is True)
    false_count = sum(1 for result in results if result['result'] is False)
    return {
        'ip': ip,
        'spammy': f'{(true_count * 100) / (true_count + false_count):.2f}%',
        'total_domains': len(dnsbl_list),
        'true_count': true_count,
        'false_count': false_count,
        'none_count': sum(1 for result in results if result['result'] is None),
        'results': results
    }


if __name__ == '__main__':
    async def test():
        print(await dnsbl_check_ip('45.144.48.63'))


    from asyncio import run

    run(test())
