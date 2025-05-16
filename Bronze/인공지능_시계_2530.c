#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int si = 0, bun = 0, cho = 0, time = 0;
	scanf("%d", &si);
	scanf("%d", &bun);
	scanf("%d", &cho);
	scanf("%d", &time);

	si += time / 3600;
	time %= 3600;
	bun += time / 60;
	time %= 60;
	cho += time;

	while (1) {
		if (cho > 59) {
			bun++;
			cho -= 60;
		}
		else break;
	}

	while (1) {
		if (bun > 59) {
			si++;
			bun -= 60;
		}
		else break;
	}

	if (si > 23) si %= 24;

	printf("%d %d %d", si, bun, cho);

}