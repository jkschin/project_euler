#include <iostream>
using namespace std;
#define BUFFER 100000

unsigned long long triangle(unsigned long long n){
	return n*(n+1)/2;
}

unsigned long long pentagon(unsigned long long n){
	return n*(3*n-1)/2;
}

unsigned long long hexagon(unsigned long long n){
	return n*(2*n-1);
}

bool compare(unsigned long long a, unsigned long long b, unsigned long long c){
	if((a == b) && (a == c)){
		return true;
	}
	return false;
}

int main(){
	unsigned long long tri[BUFFER];
	unsigned long long pen[BUFFER];
	unsigned long long hex[BUFFER];
	for (unsigned long long i = 1; i < BUFFER; i++){
		tri[i] = triangle(i);
		pen[i] = pentagon(i);
		hex[i] = hexagon(i);
	}
	// unsigned long long (*tri_ptr)[BUFFER] = &tri;
	// cout << *(*tri_ptr) << endl;
	unsigned long long ptrs[3] = {4000,2,2};
	while(true){
		// cout << ptrs[0] << " " << ptrs[1] << " " << ptrs[2] << endl;
		unsigned long long cur_tri = tri[ptrs[0]];
		unsigned long long cur_pen = pen[ptrs[1]];
		unsigned long long cur_hex = hex[ptrs[2]];
		// next_tri = tri[ptrs[0]+1];
		// next_pen = pen[ptrs[1]+1];
		// next_hex = hex[ptrs[2]+1];
		if (compare(cur_tri, cur_pen, cur_hex)){
			cout << cur_tri << endl;
			break;
		}
		if (cur_tri <= cur_pen && cur_tri <= cur_hex){
			ptrs[0]++;
			continue;
		}
		if (cur_pen <= cur_tri && cur_pen <= cur_hex){
			ptrs[1]++;
			continue;
		}
		if (cur_hex <= cur_pen && cur_hex <= cur_pen){
			ptrs[2]++;
			continue;
		}
	}
}