#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main() {

	int N;
	scanf("%d", &N);

	int a = N, b = 0;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < b; j++) {
			printf(" ");
		}
		b++;
		for (int j = 0; j < a; j++) {
			printf("*");
		}
		a--;
		
		printf("\n");
	}

}
