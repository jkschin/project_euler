#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define LIMIT 10000000

unsigned long long * sieveOfEratosthenes(){
	int *marks;
	unsigned long long *primes;
	marks = calloc(LIMIT+1,sizeof(int));
	primes = calloc(LIMIT+1,sizeof(unsigned long long));
	for (int i=2;i<LIMIT+1;i++){
		marks[i]=1;
	}
	for (int i=2;i<sqrt(LIMIT)+1;i++){
		if (marks[i]){
			for (int j=i*i;j<LIMIT+1;j+=i){
				marks[j] = 0;
			}
		}
	}
	unsigned long long ctr = 0;
	for (unsigned long long i=2;i<LIMIT+1;i++){
		if (marks[i]){
			primes[ctr] = i;
			ctr++; 
		}
	}
	free(marks);
	return primes;
}

unsigned long long * distinctPrimeFactors(unsigned long long n, unsigned long long *primes){
	unsigned long long ctr = 0, index = 0, *exponents, original = n;
	int flag = 0;
	exponents = calloc(sqrt(LIMIT)+1,sizeof(unsigned long long));
	while(n!=1){
		while(n%primes[ctr]==0){
			n = n/primes[ctr];
			flag = 1;
		}
		if (flag){
			// printf("INIT %d\n",primes[ctr]);
			exponents[index] = original/primes[ctr];
			flag = 0;
			index++;
		}
		ctr++;
	}
	return exponents;
}

unsigned long long constructCyclic(unsigned long long p){
	unsigned long long b = 10;
	unsigned long long t = 0;
	unsigned long long r = 1;
	unsigned long long x,d;
	int array[5] = {7,4,6,7,1};
	int ctr = 0;
	unsigned long long total = 0;
	while (1){
		t++;
		x = r * b;
		d = (int)(x/p);
		r = x%p;
		total+=d;
		if (r==1){
			break;
		}
		ctr++;
	}
	return total;
	// if (t==(p-1)){
	// 	return 1;
	// }
	// return 0;
}

int modular_pow(unsigned long long base,unsigned long long exponent,unsigned long long modulus){
	if (modulus==1){
		return 0;
	}
	unsigned long long result = 1;
	base = base%modulus;
	while (exponent>0){
		if ((exponent%2)==1){
			result = (result*base) % modulus;
		}
		exponent = exponent >> 1;
		base = (base*base) % modulus;
	}
	if (result==1){
		return 0;
	}
	else{
		return 1;
	}
}

int isPrimitiveMod10(unsigned long long *exponents, unsigned long long n){
	int i = 0;
	while(exponents[i]){
		if(modular_pow(10,exponents[i],n)==0){
			return 0;
		}
		i++;
	}
	return 1;
}

int main(){
	// unsigned long long *primes = sieveOfEratosthenes();
	// unsigned long long a = 725509891;
	// unsigned long long *exponentsa = distinctPrimeFactors(a-1,primes);
	// printf("%d\n",isPrimitiveMod10(exponentsa,a));

	// unsigned long long b = 726509891;
	// unsigned long long *exponentsb = distinctPrimeFactors(b-1,primes);
	// printf("%d\n",isPrimitiveMod10(exponentsb,b));

	// unsigned long long c = 729809891;
	// unsigned long long *exponentsc = distinctPrimeFactors(c-1,primes);
	// printf("%d\n",isPrimitiveMod10(exponentsc,c));
	printf("%llu\n",constructCyclic(729809891));

	
	// printf("%d\n",constructCyclic(724399657));
	// unsigned long long ctr = 37450000,n;
	// printf("GENERATING SIEVE\n");
	// while(primes[ctr]){
	// 	n = primes[ctr];
	// 	unsigned long long *exponents = distinctPrimeFactors(n-1,primes);
	// 	if(isPrimitiveMod10(exponents,n)){
	// 		printf("%llu\n",n);
	// 	}
	// 	ctr++;
	// }
}
