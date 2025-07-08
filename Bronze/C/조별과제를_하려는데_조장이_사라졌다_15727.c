#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {

	int distance, time;

	scanf("%d", &distance);

	time = distance / 5 + 1;

	if (distance % 5 == 0) time -= 1;

	printf("%d", time);

}