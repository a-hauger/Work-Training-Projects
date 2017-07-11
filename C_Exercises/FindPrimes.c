#include <limits.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//Function headers in order of use
unsigned long StringToULong(char *array[]);
void noArgsPrimeFinder();
void argsPrimeFinder(unsigned long num);
unsigned long * dynamicArrayMaker(unsigned long num, unsigned long * array);

int main(int argc, char *argv[]){
        
        /****************************************************************************************************
        /Function details:                                                                                  /
        /    1. Takes in a command line argument for the number of primes to be found.                      /
        /    2. Error control.                                                                              /
        /    3. Sends command line argument to StringTOULong to obtain the number from the string passed in./
        /        --chose unsigned long as user may input obscenly large number                              /
        /    4. Print a static number (100) prime numbers.                                                  /
        /    5. Print 'x' number of prime numbers                                                           /
        /        --uses a dynamic array as user input is unknown on compile time.                           /
        ****************************************************************************************************/

        if (argc == 2){
                printf("The argument supplied is %s\n", argv[1]);
        }
        else if (argc > 2){
                printf("You have supplied too many arguments; only one is expected.\n");
        }
        else{
                printf("One argument is expected.\n");
        }

    	unsigned long argumentNumber = StringToULong(argv);

        noArgsPrimeFinder();

        argsPrimeFinder(argumentNumber);

        return 0;
}


unsigned long StringToULong(char *array[]){
    int ULongFromString = 0;
    int len = strlen(array[1]);

    for (int i = 0; i<len; i++){
        ULongFromString = (ULongFromString * 10) + (array[1][i] - '0');
    }
    return ULongFromString;
}

void noArgsPrimeFinder(){
	int primeCounter = 1;
	unsigned long primeArray[100];
	unsigned long primeSquare[100];
	primeArray[0] = 2;
	primeSquare[0] = 4;
	printf("The following are the first 100 prime numbers.\n\t%lu\n", primeArray[0]);
	for (unsigned long i = 3; i<=ULONG_MAX && primeCounter<100; i++){
		int isPrime = 1;
		for (int j = 0; j < primeCounter; j++){
			if (i < primeSquare[j]){
				break;
			}
			else if (i%(primeArray[j]) == 0){
				isPrime = 0;
				break;
			}
		}
		if (isPrime){
			printf("\t%lu\n", i);
			primeArray[primeCounter] = i;
			primeSquare[primeCounter] = (i*i);
			primeCounter++;
		}
	}
}
unsigned long * dynamicArrayMaker(unsigned long num, unsigned long * array){
	unsigned long * tempArray = malloc(num * sizeof(unsigned long));
	for (int i = 0; i<(num/2); i++){
		tempArray[i] = array[i];
	}

	free(array);
	return tempArray;
}

void argsPrimeFinder(unsigned long num){
	int primeCounter = 1;
	unsigned long arraySize = 100;
	unsigned long * primeArray = malloc(arraySize * sizeof(unsigned long));
	unsigned long * primeSquare = malloc(arraySize * sizeof(unsigned long));
	primeArray[0] = 2;
	primeSquare[0] = 4;
	printf("\nThe following are the first %lu prime numbers.\n\t%lu\n", num, primeArray[0]);
	for (unsigned long i = 3; i<=ULONG_MAX && primeCounter<num; i++){
		int isPrime = 1;
		for (int j = 0; j < primeCounter; j++){
			if (i < primeSquare[j]){
				break;
			}
			else if (i%(primeArray[j]) == 0){
				isPrime = 0;
				break;
			}
		}
		if (isPrime){
			printf("\t%lu\n", i);
			if (primeCounter < arraySize){
				primeArray[primeCounter] = i;
				primeSquare[primeCounter] = (i*i);
				primeCounter++;
			}
			else{
				arraySize = arraySize*2;
				primeArray = dynamicArrayMaker(arraySize, primeArray);
				primeSquare = dynamicArrayMaker(arraySize, primeSquare);
			}
		}
	}
}	

