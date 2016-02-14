#include <stdio.h>
#include <stdlib.h>

int main(){
	unsigned long long a = 0;
	unsigned long long LIMIT = 1000000000000000;
	for(int i=0;i<LIMIT;i++){
		a+=1;
	}
	printf("%llu\n",a);
	return 0;
}