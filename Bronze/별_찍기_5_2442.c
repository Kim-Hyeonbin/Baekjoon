#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main() {

	int N;
	scanf("%d", &N);

	int a = (N - 1), b = 0;

	for (int i = 1; i <= N; i++) {
		for (int j = 0; j < a; j++) printf(" ");
		a--;
		for (int j = 0; j < (2 * i) - 1; j++) printf("*");
		printf("\n");
	}
}