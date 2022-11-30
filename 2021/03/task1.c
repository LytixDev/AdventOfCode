#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define BITS 12
#define LIMIT 1000

int main()
{
    // initilize array of binary numbers (represented as a string / char*)
    char nums[LIMIT][BITS+1];
    int ones[BITS];
    for (int i = 0; i < BITS; i++)
        ones[i] = 0;
    FILE *f;
    char line[BITS+1];
    const char *input_file = "input.txt";
    
    // open, read and put data into nums array
    if ((f = fopen(input_file, "r")) == NULL)
        return 1;

    int iter = 0;
    while (fgets(line, BITS+1, f)) {
        // remove '\n'
        if (strcmp(line, "\n")) {
            strcpy(nums[iter], line);
            iter++;
        }
    }

    fclose(f);

    for (int i = 0; i < LIMIT; i++) {
        for (int j = 0; j < BITS; j++) {
            if (nums[i][j] == '1')
                ones[j]++;
        }
    }

    int gamma_rate = 0;
    int epsilon_rate = 0;
    for (int i = 0; i < BITS; i++) {
        int one = ones[i] > LIMIT / 2;
        if (one) {
            gamma_rate += 1 * pow(2, BITS-i-1);;
        }
        else
            epsilon_rate += 1 * pow(2, BITS-1-i);
        
    }

    printf("%d\n", gamma_rate * epsilon_rate);
    return 0;
}
