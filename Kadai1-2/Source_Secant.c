#include<stdio.h>
#include<math.h>
double func(double x);
int main() {
	double ans = 1;
	double oldans = ans + 1;
	int loop = 0;
	while (fabs(func(ans)) > 1.0e-20)
	{
		printf("Loop%d,x=%.20f\n",loop,ans);
		double y = func(ans);
		double a = (func(ans) - func(oldans)) / (ans - oldans);
		double x = y / a;
		oldans = ans;
		ans -= x;
		loop++;
	}
	printf("Loop%d,x=%.20f\n", loop, ans);
	printf("f(x)=%.20f\n", func(ans));
	return 0;
}

double func(double x) {
	return x - exp(-x);
}