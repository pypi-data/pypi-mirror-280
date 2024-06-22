from setuptools import setup, find_packages

setup(
    name='prlsp_dnsbl',
    version='0.0.1a',
    author='prolapser',
    packages=find_packages(),
    url='https://github.com/prolapser/prlsp_dnsbl',
    license='LICENSE.txt',
    description='проверка ip по базам dns-based blacklist',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'aiodns', 'pycares'
    ],
    package_data={
        'prlsp_dnsbl': ['domains/*.json'],
    },
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
