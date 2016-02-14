#include <stdio.h>
#include <stdlib.h>

#define LIMIT 1000

int main(){
	int a,b,c,m,n;
	int flag = 0;
	for(m=1;m<LIMIT;m++){
		for(n=1;n<m;n++){
			a = m*m - n*n;
			b = 2*m*n;
			c = m*m + n*n;
			int total = a+b+c;
			if(total>1000){
				break;
			}
			if(total==1000){
				flag = 1;
				break;
			}
		}
		if (flag){
			break;
		}
	}
	printf("%d,%d,%d\n",a,b,c);
	return 0;
}