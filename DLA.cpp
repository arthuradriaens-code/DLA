#include <cmath>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

def update(state,WIDTH) {
	choises = [-1,1]
	for (int i=0;i!=WIDTH; ++i){
		for (int j=0;j!=WIDTH; ++j){
			if (state[i][j] == 1){
				if (i<WIDTH-1 && j < WIDTH-1 && -1<i && -1<j) && (state[i+1][j] == 2 | state[i-1][j] == 2 | state[i][j-1] == 2 | state[i][j+1] == 2){
					state[i][j] = 2
				}
				else{
					if random.random() < 0.5:
						i_ = 0
						j_ = int(random.choice(choises))
						if (j_ + j) > WIDTH - 1:
							j_ = -j
						elif (j_ + j) < 0:
							j_ = WIDTH - 1 - j
					else:
						j_ = 0
						i_ = int(random.choice(choises))
						if (i_ + i) < 0:
							i_ = WIDTH - 1 - i
						elif (i_ + i) > WIDTH - 1:
							i_ = -i
					if int(state[i+i_][j+j_]) == 1:
						state[i][j] = 1
					else:
						state[i][j] = 0
						state[i+i_][j+j_] = 1
				}
			}
			if state[i][j] == 2{
				state[i][j] = 2
			}
		}
	}
	return state


int main(){
	WIDTH = 512
	calctime = 5000
	int DLA[WIDTH][WIDTH] = {}	
	DLA[WIDTH/2][WIDTH/2] = 2	
}
