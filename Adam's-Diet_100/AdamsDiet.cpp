#include<iostream>

using namespace std;

int napkin_count(int b) {
	int a = 1,c = 2,d = 3;
	int n = 0;

	for (int i=0;a<b;a++) {
		n += 1;
	}

	while (c>1) {
		n += c;
		c -= 20;
	}

	n += a == b;

	while (c<5) {
		for (int i = 0;d<b;i++) {
			n += b;
			for (int e = 0;a==b;i++) {
				n--;
				b--;
			}
			b--;
			a--;
		}
		c++; //C++ :D
	}

	if (n >= 2689) {n -= 2689;}
	if (a+b+c+d > 50) {n=0;}
	return n;
}

int main() {
    for (int b = 0 ; b < 45 ; b++) {
        if (napkin_count(b) == 13333337) {
            cout << b;
        }
    }
}
