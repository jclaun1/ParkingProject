#include <stdio.h>


int average_area(int m_colors) {
	int control_averages[];
	int space_averages[];

	//Pass this in as argument
	int numColors = m_colors;

	//RGB Values and averages
	int totals[numColors];
	if(numColors == 3){
		for(int i = x; i < x+w; i++){
			for(int j = y-h; j < y; j++){
				for(int k = 0; k < numColors; k++)
					totals[k] += pixels[i, j][k];
			}
		}
		int numPixels = w*h;
		for(int i = 0; i < numColors; i++)
			totals[numColors] += totals[i] / numPixels;
	}
	//BW Values
	else if(numColors == 1){
		for(int i = x; i < x+w; i++){
			for(int j = y-h; j < y; j++){
				totals[3] += pixels[i, j];
			}
		}
	}
	return totals[3];
}


/*-----------------------------------------------------------------*/
int compare_area(int test[], int expected[]){
	if(sizeof(test) != sizeof(expected)){
		fprintf("Arrays need to be same length");
		return NULL;
	}

	bool different = false;
	for(int i = 0; i < sizeof(test); i++){
		if(abs(test[i] - expected[i]) > IMAGE_THRESHOLD)
			different = true;
	}
	return different;
}


/*-----------------------------------------------------------------*/
void writeResults(int spaceValues[]){

//FILE IO 
/*
	FILE *fp;
	fp = fopen("pixels.txt");
	fprintf(fp)


*/

}


/*-----------------------------------------------------------------*/
int readPixels(char* fileName){
//FILE IO 
/*
	FILE *fp;
	fp = fopen(fileName);
	fprintf(fp)


*/
}



/*-----------------------------------------------------------------*/
int main() {
	int numSpots = 24;
	int numControls = 5;
	int pixels[4] = readPixels("pixels.txt")
	int space_averages[numSpots];
	int control_averages[numSpots];
	int spotValues[numSpots];
	//Get these from settings files
	int space_boxes = {}
	int control_boxes = {}

	//Getting average color values of each space
	for(int i = 0; i < sizeof(space_boxes); i++){
		int space[5] = space_boxes[i];
		int width = abs(space[2] - space[4]);
		int height = abs(space[3] - space[5]);
		space_average = average_area(pixels, space[2], space[3], width, height);
		space_averages[i] = space_average;
	}

	//Getting average color values of each control
	for(int i = 0; i < sizeof(control_boxes); i++){
		int control[5] = control_boxes[i];
		int width = abs(control[2] - control[4]);
		int height = abs(control[3] - control[5]);
		control_average = average_area(pixels, control[2], control[3], width, height);
		control_averages[i] = control_average;
	}

	//Comparing spots to see if they are taken or free
	for(int i = 0; i < sizeof(space_averages); i++){
		int num_controls = 5;
		bool is_occupied = false;

		for(int controlNum = 0; controlNum < sizeof(control_averages); controlNum++){
			if(compare_area(space_averages[i], control_averages[controlNum])==true)
				num_controls +=1;
		}

		if(num_controls >= 3)
			is_occupied = true;
		spotValues[i] = is_occupied;
	}
}
