// why can't lanternfish have natural predators ???? !!!
#include <stdlib.h>
#include <stdio.h>

#define MAX_AGE 10

int main()
{
    char file_name[] = "input.txt";
    // fill fish array with zeros
    unsigned long fish[MAX_AGE];
    for (int i = 0; i < MAX_AGE; i++)
        fish[i] = 0;
    
    FILE *fileptr = fopen(file_name, "r");
    // populate fish with input data
    char current_char = fgetc(fileptr);
    while (current_char != EOF && current_char != '\n') {
        if (current_char != ',')
            fish[current_char - '0']++;
        current_char = fgetc(fileptr);
    }

    int n = 255;
    unsigned long tmp[MAX_AGE];
    for (int i = 0; i < n; i++) {
        // reset tmp array
        for (int j = 0; j < MAX_AGE; j++)
            tmp[j] = 0;
        
        for (int k = 0; k < MAX_AGE; k++) {
            if (k != 0)
                tmp[k-1] = fish[k];
        }

        tmp[9] = tmp[0];
        tmp[7] += tmp[0];
        // copy tmp over to fish
        for (int i = 0; i < MAX_AGE; i++)
            fish[i] = tmp[i];
    }

    unsigned long sum = 0;
    for (int i = 0; i < MAX_AGE - 1; i++)
        sum += fish[i];

    printf("%ld\n", sum);

}
