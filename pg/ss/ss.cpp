#include <stdlib.h>

int randint(int, int);
void changeStatCpp(int*, int*, int);

int randint(int min, int max){
	return (rand() % (max - min)) + min;
}

void changeStatCpp(int* data, int* res, int len){
	int index, tmp;
	for(index=0; index<len; index+=3){
		tmp = randint(0, 6);
		switch(tmp){
			case 0:
				if(data[index] >= 511) data[index] = 0; 
				else data[index] += 1;
				break;
			case 1:
				if(data[index+1] >= 511) data[index+1] = 0; 
				else data[index+1] += 1;
				break;
			case 2:
				if(data[index+2] >= 511) data[index+2] = 0; 
				else data[index+2] += 1;
				break;
			case 3:
				if(data[index] <= 0) data[index] = 511; 
				else data[index] -= 1;
				break;
			case 4:
				if(data[index+1] <= 0) data[index+1] = 511; 
				else data[index+1] -= 1;
				break;
			case 5:
				if(data[index+2] <= 0) data[index+2] = 511; 
				else data[index+2] -= 1;
				break;
		}
	}
	for(index=0; index<len; index++){
		if(data[index]>=256) res[index] = 511 - data[index];
		else res[index] = data[index];
	}
}

extern "C"{
	void changeStat(int* data, int* res, int len){
		changeStatCpp(data, res, len);
	}
}
