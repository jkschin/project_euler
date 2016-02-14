//A faster solution has been found. See the python code.

#include <stdio.h>
#include <stdlib.h>

int checkValidity(unsigned long long LIMIT){
	unsigned long long a,b;
	unsigned long long lower = 0;
	unsigned long long upper = LIMIT;
	unsigned long long middle,q,r,numerator,denominator;
	int z = 0;
	denominator = (LIMIT) * (LIMIT-1);
	while(1){
		middle = (lower+upper)/2;
		numerator = (middle) * (middle+1);
		q = denominator/numerator;
		r = denominator%numerator;
		printf("%llu,%llu\n",numerator,denominator);
		printf("%llu,%llu\n",q,r);
		// a = gcd(middle+1,LIMIT);
		// b = gcd(middle,LIMIT-1);
		// printf("%llu,%llu\n",a,b);
		// numerator = (double)((middle+1)/a)*(double)((middle)/b);
		// denominator = (double)((LIMIT)/a)*(double)((LIMIT-1)/b);
		// prob = numerator/denominator;
		if(q==2 && r==0){
			printf("VALID\n");
			printf("%llu\n",middle+1);
			printf("%llu\n",LIMIT);
			return 1;
		}
		else if(q>=3 || (q==2&&r!=0)){
			printf("LOWER");
			lower = middle;
		}
		else if(q==1){
			printf("UPPER");
			upper = middle;
		}
		if(middle+1==upper){
			// printf("INVALID\n");
			return 0;
		}
		if(z==10){
			break;
		}
		z++;
	}
}

int main(){
	unsigned long long LIMIT = 100000000000;
	checkValidity(LIMIT);
	int v;
	// while(1){
	// 	v = checkValidity(LIMIT);
	// 	if(v){
	// 		break;
	// 	}
	// 	printf("%llu",LIMIT);
	// 	LIMIT++;
	// }
	// return 0;
}