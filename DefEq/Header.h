#include<stdio.h>

//�v�Z�̈�[MIN,MAX]
#define MIN (0.0)
#define MAX (1.0)
//�v�Z�̈敪����
#define N (10)
//x=MIN�̂Ƃ��̒l
#define Y0 (0)

void Init(double* x, double* y) {
	//�����l�ݒ�
	for (int i = 0; i < N + 1; i++) {
		x[i] = (MAX - MIN) * i / N;
	}
	//x=MIN�̂Ƃ���y�̒l��ݒ�
	y[0] = Y0;
}

void Output(double* x, double* y) {
	for (int i = 0; i < N + 1; i++) {
		printf("%d\t%.20f\t%.20f\n",i, x[i], y[i]);
	}
}

double F(double x, double y) {
	return 1 + y;
}
