#include <stdio.h>
#include <math.h>

int main()
{
	int n = 2;
	int count;
	while(1){
		int i = 1;
		int check = 0;
		printf("%f",round(sqrt(n)));
		break;
		while(i<round(sqrt(n)))
		{
			printf("here");
		}
	}
	// while(1)
	// {
		// int i = 1;
		// int check = 0;
		// while(i<round(sqrt(n)))
		// {
		// 	if ( n%i==0 )
		// 	{
		// 		check++;
		// 	}
		// }
		// if(check==2)
		// {
		// 	count++;
		// }
		// if(count==1)
		// {
		// 	printf("%d",n);
		// }
		// n++;
		// if(n==10)
		// {
		// 	break;
		// }
	// }
	return 0;
}