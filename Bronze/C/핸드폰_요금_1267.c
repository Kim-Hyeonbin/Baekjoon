#include <stdio.h>

int main() {

	int num = 0, M_tot = 0, Y_tot = 0, call_tot[20];

	scanf("%d", &num);

	for (int i = 0; i < num; i++) {
		scanf("%d", &call_tot[i]);
	}

	for (int i = 0; i < num; i++) {
		Y_tot += (call_tot[i] / 30) + 1;
	}
	Y_tot *= 10;

	for (int i = 0; i < num; i++) {
		M_tot += (call_tot[i] / 60) + 1;
	}
	M_tot *= 15;

	if (M_tot < Y_tot) {
		printf("M %d", M_tot);
	}
	else if (M_tot > Y_tot) {
		printf("Y %d", Y_tot);
	}
	else {
		printf("Y M %d", M_tot);
	}

}