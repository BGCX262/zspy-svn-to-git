0.
python.org
下载安装python2.52

1.安装setup_tools
http://pypi.python.org/packages/2.5/s/setuptools/setuptools-0.6c8.win32-py2.5.exe#md5=963088fdb1c7332b1cbd4885876e077a
添加easy_install.exe目录到环境变量

2.
easy_install -U setuptools
easy_install -U BeautifulSoup
easy_install -U Mako
easy_install -U Elixir
PyDispatcher


3.如何离线安装
在有网络的地方
easy_install -zmaxd . BeautifulSoup
然后将整个目录下的内容copy到目标机器，执行
easy_install -f . BeautifulSoup

