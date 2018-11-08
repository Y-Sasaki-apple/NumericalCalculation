#include<stdio.h>
#include<math.h>
double func(double x);
int main() {
	double min=0, max=1;
	double mid= mid = (min + max) / 2;
	int loop = 0;
	while (fabs(func(mid))>1.0e-20)
	{
		printf("Loop%d,mid=%.20f\n", loop, mid);
		if (func(mid) > 0)
			max = mid;
		else 
			min = mid;
		mid = (min + max) / 2;
		loop++;
	}
	printf("Loop%d,mid=%.20f\n", loop, mid);
	printf("f(x)=%.20f\n", func(mid));
	return 0;
}

double func(double x) {
	return x - exp(-x);
}
