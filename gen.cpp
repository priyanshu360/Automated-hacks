#include <bits/stdc++.h>

using namespace std;

int rand(int a, int b){
	return a + rand() % (b - a + 1);
}



int main(int argc, char* argv[]){
	srand(atoi(argv[1]));
	int test = rand(1, 10);
	cout<<test<<endl;
	while(test--){
		int p = rand(1, 1000000000);
		int f = rand(1, 1000000000);
		int c1 = rand(1, 100000);
		int c2 = rand(1, 100000);
		int s = rand(1, 1000000000);
		int w = rand(1, 1000000000);
		//while(b < a) b = rand(1, 100000);
		//int k = rand(1 , 5);
		cout<<p<<" "<<f<<endl;
		cout<<c1<<" "<<c2<<endl;
		cout<<s<<" "<<w<<endl;
	}
	return 0;
}
