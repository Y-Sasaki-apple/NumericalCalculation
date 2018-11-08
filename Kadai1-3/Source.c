#include<stdio.h>
#include<math.h>
double func(double x);
double funcdiff(double x);
int main() {
	double ans = 1;
	int loop = 0;
	while (fabs(func(ans))>1.0e-8)
	{
		printf("Loop%d,x=%g\n", loop, ans);
		double y = func(ans);
		double a = funcdiff(ans);
		double x = y / a;
		ans -= x;
		loop++;
		if (loop > 20)break;
	}
	printf("Loop%d,x=%g\n", loop, ans);
	printf("f(x)=%g\n", func(ans));
	return 0;
}

double func(double x) {
	return 1/x+1;
}

double funcdiff(double x) {
	return -1/(x*x);
}