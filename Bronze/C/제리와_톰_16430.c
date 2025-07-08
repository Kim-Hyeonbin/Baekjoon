#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int A, B, P, Q;
	scanf("%d %d", &A, &B);
	
	P = B - A;
	Q = B;

	while (1) {
		if ((P % 2 == 0) && (Q % 2 == 0)) {
			P /= 2;
			Q /= 2;
		}
		else if ((P % 3 == 0) && (Q % 3 == 0)) {
			P /= 3;
			Q /= 3;
		}
		else {
			break;
		}
	}

	printf("%d %d", P, Q);
	
}