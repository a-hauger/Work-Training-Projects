#include <stdio.h>
#include <string.h>

void printAstTriangle(int number);

int main(int argc, char *argv[]){

	/***************************************************************
	/ Creates an isocoles triangle of base x defined by user input /
	***************************************************************/

	if (argc == 2){
		printf("The argument supplied is %s\n", argv[1]);
	}
	else if (argc > 2){
		printf("You have supplied too many arguments; only one is expected.\n");
	}
	else{
		printf("One argument is expect.\n");
	}

	int numAsterisks = 0;
	int len = strlen(argv[1]);

	for (int i = 0; i<len; i++){
		numAsterisks = (numAsterisks*10) + (argv[1][i] - '0');
	}

	printAstTriangle(numAsterisks);

	return (1);
}

void printAstTriangle(int number){

	for (int i=1; i<=number; i++){
		for (int j = 0; j < i; j++){
			printf("%c", '*');
		}
		printf("\n");
	}
}
