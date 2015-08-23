#include <utility>

typedef unsigned value_type;

template<class string>
std::pair<value_type,value_type> hash_two(const string& str){
	value_type hash =5381 ,hash1 = 1315893911;
	typename string::size_type i=str.length();
	while(i--){
		hash = ((hash << 5) + hash) + str[i];
		hash1=str[i]^hash1 + hash;
	}
	return std::make_pair(hash,hash1);
}

template<class string,class begin,class end>
void gen_hash(const string& s,begin b,end e){
	std::pair<value_type,value_type> hash_pair=hash_two(s);

	value_type h1=hash_pair.first,h2=hash_pair.second;
	if(b!=e)*b=h1;else return;

	while(++b!=e){
		*b=h2;
		h2=h1+h2;
	}
}

#include <memory> 
#include <boost/scoped_array.hpp>
using namespace boost;



template<typename counter_type=unsigned>
class BloomFilter
{
public
	BloomFilter(unsigned bucket_size,unsigned hash_func_number):
		counter(new counter_type[bucket_size])
	{
		
	}
	template<typename string>
	void add(const string& s){
		
	}
private:
	scoped_array<counter_type> counter;
	unsigned hash_func_number;
	BloomFilter(const BloomFilter&){};
};


#include <iostream>
#include <set>
#include <boost/lexical_cast.hpp>
#include <string>
#include <fstream>
using namespace std;

int main(){
string s;
set<unsigned> hash_set;
ifstream input("sougo_word_sorted.txt");
unsigned line=0;
while(getline(input,s)){

	const unsigned size=10;
	unsigned c[size];
	gen_hash(s,c,c+size);
	for(int i=0;i<size;++i){
		//cout<<c[i]<<" "<<lexical_cast<string>(c[i]).length()<<"\n";
		hash_set.insert(c[i]);
	}
	cout<<++line<<" length "<<hash_set.size()<<endl;
}
//system("pause");
}
