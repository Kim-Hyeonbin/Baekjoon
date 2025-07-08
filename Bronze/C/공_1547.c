#include <stdio.h>

int main() {
	
	int a[] = { 1, 2, 3 };

	int* loc = &a[0], total = 0, X, Y;

	scanf("%d", &total);

	for (int i = 0; i < total; i++) {

		scanf("%d %d", &X, &Y);

		if (X == *loc) {
			loc = &a[Y - 1];
		}
		else if (Y == *loc) {
			loc = &a[X - 1];
		}
		else if (X == Y) continue;
		else continue;

	}

	printf("%d", *loc);

}