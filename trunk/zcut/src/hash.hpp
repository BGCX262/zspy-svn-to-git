#ifndef _CN_HASH_HPP_2008_3_18_12_39_ZSP007_AT_GMAIL_COM
#define _CN_HASH_HPP_2008_3_18_12_39_ZSP007_AT_GMAIL_COM

int hash(const char *str,unsigned buf_size){
	unsigned char * ustr =(unsigned char *)(str);
	unsigned long hash = 1315423911;
	int c;
	while(c = *ustr++){
		hash ^= ((hash << 5) + c + (hash >> 2));
	}
	return hash%buf_size;
}

#endif
