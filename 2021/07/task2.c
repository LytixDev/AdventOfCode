#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>

#define LIMIT 1000

int step(int range)
{
    int f = 0;
    for (int i = 1; i < range; i++)
        f += i;

    return f;
}

int main()
{
    char file_name[] = "input.txt";
    unsigned short nums[LIMIT];
    // fill the array with zeros
    for (int i = 0; i < LIMIT; i++)
        nums[i] = 0;
    
    // open, read and store data in nums
    FILE *fileptr = fopen(file_name, "r");
    char current_str[255] = "";
    int iter = 0;
    int len;
    char current_char = fgetc(fileptr);
    while (current_char != EOF && current_char != '\n') {
        if (current_char == ',') {
            nums[iter] = atoi(current_str);
            strcpy(current_str, "");
            iter++;
        } else {
            len = strlen(current_str);
            current_str[len] = current_char;
            current_str[len+1] = '\0';
            //strcat(current_str, &current_char);
        }

        current_char = fgetc(fileptr);
    }

    // get last piece of data
    if (atoi(current_str) != 0)
        nums[iter] = atoi(current_str);

    int largest = 0;
    for (int i = 0; i < LIMIT; i++) {
        if (nums[i] > largest)
            largest = nums[i];
    }

    long min = INT_MAX;
    for (int i = 0; i < largest; i++) {
        long ith_sum = 0;
        for (int j = 0; j < LIMIT; j++) {
            ith_sum += step(abs(i - nums[j]) + 1);
            //printf("%d + %d = %d\n", i, nums[j], step(abs(i - nums[j]) + 1));
        }
        if (ith_sum < min)
            min = ith_sum;
    }
    
    printf("%ld\n", min);
}
