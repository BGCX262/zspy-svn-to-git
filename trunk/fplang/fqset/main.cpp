#include <iostream>
#include <string>
#include <algorithm>
#include <iterator>
#include <zutil/next_char.hpp>

using namespace std;
using namespace zutil;
int main() {
    string test="这 is 一个test，好哈";
    vector<string> result=char_split(test);
    typedef ostream_iterator<string> ostream_itr;
    copy(result.begin(), result.end(), ostream_itr(cout,"\n"));
    return 0;
}
