#ifndef _ZUTF8_HPP_2008_3_18_0_59_ZSP007_AT_GMAIL_COM
#define _ZUTF8_HPP_2008_3_18_0_59_ZSP007_AT_GMAIL_COM
#include <vector>
#include <cassert>
#include <cstring>
#include <cctype>
#include <utility>
/*
using namespace std;
using namespace zutil;
int main() {
    string test="这 is 一个test，好哈";
    vector<string> result=char_split(test);
    typedef ostream_iterator<string> ostream_itr;
    copy(result.begin(), result.end(), ostream_itr(cout,"\n"));
    return 0;
}
*/
namespace zutil {
using namespace std;

enum CharType {undefined=0,ascii,cn};

template<class Iter>
Iter en_word(Iter next,Iter end) {
    unsigned char c;
    while (next!=end) {
        c=static_cast<unsigned char>(*next);
        if (c<=0x7F && isalnum(*next)) {
            ++next;
        } else {
            break;
        }
    }
    return move(next);
}
template<class Iter>
pair<Iter,CharType> utf8_next(Iter next,Iter end) {
    unsigned char c;
    CharType char_type=undefined;
    c=static_cast<unsigned char>(*next);
    /*
    1.ascii 2.希腊字母 3.汉字 4.平面符号
    #那么如何判断UTF-8字符的长度呢？
    #0x00-0x7F 	1字节
    #0xC0-0xDF 	2字节
    #0xE0-0xEF 	3字节
    #0xF0-0xF7 	4字节
    #0xF8-0xFB 	5字节
    #0xFC-0xFD 	6字节
    */
    //设置char_length
    if (c>=0xE0) {
        if (c<=0xEF) {
            next+=3;//先判断中文,提高效率
            char_type=cn;
        } else if (c<=0xF7)next+=4;
        else if (c<=0xFB)next+=5;
        else if (c<=0xFD)next+=6;
    } else if (c<=0x7F) { //ascii码
        ++next;
        char_type=ascii;
    } else if (c>=0xC0)next+=2;
    assert(end-next>=0);
    return move(make_pair(next,char_type));
}
template<class String>
vector<String> char_split(String& s) {
    vector<String> buf;
    typedef typename String::iterator Iter;
    Iter from=s.begin(),end=s.end(),to;
    pair<Iter,CharType> result;
    while (from!=end) {
        result=utf8_next(from,end);
        if (result.second==ascii && isalnum(*from)) {
            to=en_word(result.first,end);
        } else {
            to=result.first;
        }
        buf.push_back(String(from,to));
        from=to;
    }
    return move(buf);
};

};

#endif
