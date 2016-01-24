#include <stdio.h>
#include <stdlib.h>

int collatz(unsigned long long n){
	unsigned long long count = 0;
	while(n!=1){
		if(n%2==0){
			n /= 2;
		}
		else{
			n = 3*n + 1;
		}
		count++;
	}
	count++;
	return count;
}

int main(){
	unsigned long long global_count = 0;
	int max = 0;
	for(int i=1;i<1000001;i++){
		unsigned long long local_count = collatz(i);
		if(local_count > global_count){
			global_count = local_count;
			max = i;
		}	
	}
	printf("%d\n",max);
}