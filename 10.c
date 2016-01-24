#include <stdio.h>
#include <stdlib.h>

#define LIMIT 2000000

int main()
{
	unsigned long long int i,j;
	int *primes;
	int z = 1;
	unsigned long long out;

	primes = malloc(sizeof(int)*LIMIT);

	for (i=2;i<LIMIT;i++){
		primes[i] = 1;
	}

	for (i=2;i<LIMIT;i++){
		if (primes[i]){
			for (j=i;i*j<LIMIT;j++){
				primes[i*j]=0;
			}
		}
	}
	for (i=2;i<LIMIT;i++){
		if (primes[i]){
			out+=i;
		}
	}
	printf("%llu\n",out);
}
