#coding:utf-8
from setuptools import setup,find_packages
setup(
    name="znet",
    version="0.10",

    author="ZhangShen Peng",
    author_email="zsp007@gmail.com",
    #url=url,
    #download_url=download_url,
    #description=description,

    install_requires = [
        "BeautifulSoup",
        "Mako",
    ],
    #zip_safe=True,
    packages=find_packages(),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

