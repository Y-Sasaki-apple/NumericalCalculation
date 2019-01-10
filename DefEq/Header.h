#include<stdio.h>

//計算領域[MIN,MAX]
#define MIN (0.0)
#define MAX (1.0)
//計算領域分割数
#define DIV (5)
//x=MINのときの値
#define Y0 (0)

void Init(double* x, double* y) {
	//初期値設定
	for (int i = 0; i < DIV + 1; i++) {
		x[i] = (MAX - MIN) * i / DIV;
	}
	//x=MINのときのyの値を設定
	y[0] = Y0;
}

void Output(double* x, double* y) {
	for (int i = 0; i < DIV + 1; i++) {
		printf("%d\t%.20f\t%.20f\n",i, x[i], y[i]);
	}
}

double F(double x, double y) {
	return 1 + y;
}
