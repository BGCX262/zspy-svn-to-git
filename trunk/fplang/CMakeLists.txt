cmake_minimum_required(VERSION 2.6)

#项目名称
PROJECT (fplang)

#头文件路径
INCLUDE_DIRECTORIES(
.
./sms/
/usr/include/python2.6/
)

#表示cpp文件列表的变量，如${DIRA_SRCS}代表src/dira目录下的所有源文件
AUX_SOURCE_DIRECTORY(fqset fqset_src)
AUX_SOURCE_DIRECTORY(fqset sms_src)
AUX_SOURCE_DIRECTORY(zutil zutil_src)

#设置变量
#SET(srcs
#    ${fqset_src}
#)

#需要链接的第三方库
SET(LIBRARYS
    #A.so
    #B.a
)

#定义宏,多个用空格隔开
ADD_DEFINITIONS(
    -DNDEBUG
    -std=c++0x
    -O3
    -march=i686
)


#添加可执行文件生成任务
ADD_EXECUTABLE(bin/fqset.exe ${fqset_src})
ADD_EXECUTABLE(bin/sms.exe ${sms_src})
ADD_LIBRARY(zutil SHARED ${zutil_src})
#添加链接库
TARGET_LINK_LIBRARIES(bin/fqset.exe ${LIBRARYS})
TARGET_LINK_LIBRARIES(bin/sms.exe pthread curl)
TARGET_LINK_LIBRARIES(zutil boost_python)
