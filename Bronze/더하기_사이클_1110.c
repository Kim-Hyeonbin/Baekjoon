#include <stdio.h>

int main(void) {

	int num = 0, cnt = 0, a, b, c;

	scanf_s("%d", &num);
	
	a = num;

	while (1) {
		b = (a / 10) + (a % 10);
		c = ((a % 10) * 10) + (b % 10);
		a = c;
		cnt++;

		if (a == num) break;
	}

	printf("%d", cnt);

}