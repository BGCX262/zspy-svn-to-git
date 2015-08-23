#include <iostream>
#include <string>
#include <fstream>
#include <ctime>

#include <boost/tokenizer.hpp>
#include <boost/lexical_cast.hpp>

#include "../src/cn_word.hpp"  
#include "../src/hash.hpp"

using namespace boost;
using namespace std;

typedef tokenizer<CnWord> CnTokenizer;
int main(){
	string s;
	while(cin>>s)
	cout<<"hash value : "<<hash(s.c_str(),5381)<<"\n";
/*
	string word;
    
    cout<<"加载词典中...."<<endl;
    ifstream dict_file("dict.txt");
    
    while(dict_file>>word){
        CnWord::add(word.c_str());
    }
    dict_file.close();
    cout<<"词典加载完毕."<<endl;
    ifstream story("test.txt");
    unsigned begin=time(0);
    while(getline(story,word)){
        CnTokenizer tok(word);
        for(CnTokenizer::iterator beg=tok.begin();beg!=tok.end();++beg){
            cout << *beg <<" ";
        }
        cout<<'\n';
    }
    cout<<"开始时间 "<<begin<<endl;
    cout<<"结束时间 "<<time(0)<<endl;
    cout<<"用时 "<<time(0)-begin<<endl;
    story.close();
*/
	return 0;
}
