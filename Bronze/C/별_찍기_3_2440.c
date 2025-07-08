#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int N, M;
	scanf("%d", &N);
	M = N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			printf("*");
		}
		printf("\n", M--);
	}
}