#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]){

	/****************************************************************************************************
    / Function Details:                                                                                  /
    /   1. Takes user input from command line.                                                           /
    /   2. Uses ASCII values of numbers to determine the value of the number                             /
    /       --does so by first mult. by 10 from previous value, then adding ASCII value minus ASCII of 0 /
    /   3. Prints integer value of string typed by user -- the two are identical.                        /
    *****************************************************************************************************/

	if (argc == 2){
		printf("The argument supplied is %s\n", argv[1]);
	} else if (argc > 2){
		printf("You have supplied too many arguments; only one is expected.\n");
	} else{
		printf("One argument is expected.\n");
	}

	int integerFromString = 0;
	int len = strlen(argv[1]);

	for (int i=0; i<len; i++){
	integerFromString = (integerFromString * 10) + (argv[1][i] - '0');
	}
	printf("The integer you have typed in is %d\n", integerFromString);
}

	
