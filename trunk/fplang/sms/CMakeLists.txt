cmake_minimum_required(VERSION 2.6)

#项目名称
PROJECT (sms)

#头文件路径
INCLUDE_DIRECTORIES(
.
/usr/include/python2.6/
)

LINK_DIRECTORIES(
.
)

#表示cpp文件列表的变量，如${DIRA_SRCS}代表src/dira目录下的所有源文件
AUX_SOURCE_DIRECTORY(. sms_src)

#定义宏,多个用空格隔开
ADD_DEFINITIONS(
    -DNDEBUG
    -std=c++0x
    -O3
    -march=i686
)

SET(EXECUTABLE_OUTPUT_PATH ./bin)
SET(LIBRARY_OUTPUT_PATH .)

#添加可执行文件生成任务
#ADD_EXECUTABLE(sms.exe ${sms_src})
ADD_LIBRARY(sms SHARED ${sms_src})
#添加链接库
TARGET_LINK_LIBRARIES(sms pthread curl fetion_32 boost_python)
