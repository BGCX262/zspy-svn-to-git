http://jaist.dl.sourceforge.net/sourceforge/boost/boost_1_34_1.7z

源代码是utf-8,支持的分词文件为utf-8

我用的编译器为gcc-4.2.1-2

依赖库
stl::tr1
boost

同时参见文档
www.boost.org/libs/tokenizer/index.html 
http://www.boost.org/libs/tokenizer/tokenizerfunction.htm

修改gen_make.bat可以更改生成的makefile的类型
cmake .. -G "MinGW Makefiles"

列表如下:
  Borland Makefiles           = Generates Borland makefiles.
  MSYS Makefiles              = Generates MSYS makefiles.
  MinGW Makefiles             = Generates a make file for use with
                                mingw32-make.
  NMake Makefiles             = Generates NMake makefiles.
  Unix Makefiles              = Generates standard UNIX makefiles.
  Visual Studio 6             = Generates Visual Studio 6 project files.
  Visual Studio 7             = Generates Visual Studio .NET 2002 project
                                files.
  Visual Studio 7 .NET 2003   = Generates Visual Studio .NET 2003 project
                                files.
  Visual Studio 8 2005        = Generates Visual Studio .NET 2005 project
                                files.
  Visual Studio 8 2005 Win64  = Generates Visual Studio .NET 2005 Win64
                                project files.
  Visual Studio 9 2008        = Generates Visual Studio 9 2008 project files.
  Visual Studio 9 2008 Win64  = Generates Visual Studio 9 2008 Win64 project
                                files.
  Watcom WMake                = Generates Watcom WMake makefiles.