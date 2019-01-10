#include"Header.h"

#define EULER 1
#define RK4 4
#define WAY RK4

#if WAY == EULER
void Calc(double* x, double* y) {
	//オイラー法による計算
	for (int n = 0; n < N; n++) {
		double h = x[n + 1] - x[n];

		double k1 = F(x[n], y[n]);

		y[n + 1] = y[n] + h * k1;
	}
}
#endif
#if WAY == RK4
void Calc(double* x, double* y) {
	//4次ルンゲクッタ法による計算
	for (int n = 0; n < N; n++) {
		double h = x[n + 1] - x[n];

		double k1 = F(x[n], y[n]);
		double k2 = F(x[n] + h / 2, y[n] + h / 2 * k1);
		double k3 = F(x[n] + h / 2, y[n] + h / 2 * k2);
		double k4 = F(x[n] + h, y[n] + h * k3);
		y[n + 1] = y[n] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4);
	}
}
#endif
int main() {
	double x[N + 1];
	double y[N + 1];

	Init(x, y);
	Calc(x, y);
	Output(x, y);

	return 0;
}
