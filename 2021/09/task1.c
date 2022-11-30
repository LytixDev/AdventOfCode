#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define LINES 100
#define LEN 101

int main()
{
    char nums[LINES][LEN];
    // fill last line with large number
    for (int i = 0; i < LEN; i++)
        strcpy(&nums[LINES][i], "99999999");

    char buffer[LEN];
    char file_name[] = "input.txt";
    int iter = 0;

    FILE *fp = fopen(file_name, "r");
    if (fp == NULL) return 1;
    
    while (fgets(buffer, sizeof(buffer), fp)) {
        if (strcmp(buffer, "\n") != 0) {
            strcpy(nums[iter], buffer);
            iter++;
        }
    }

    long sum = 0;
    // first line
    for (int i = 0; i < LEN-1; i++) {
        //printf("%c, %d, %d\n", nums[0][i], i, LEN);
        if (i != 0 && i != LEN-2) {
            if (nums[0][i] < nums[0][i-1] && nums[0][i] < nums[0][i+1] && nums[0][i] < nums[1][i])
                sum += nums[0][i] - '0' + 1;
        } else if (i == 0) {
        // edge case left
            if (nums[0][i] < nums[0][i+1] && nums[0][i] < nums[1][i])
                sum += nums[0][i] - '0' + 1;
        } else if (i == LEN-2) {
            // edge case right
            if (nums[0][i] < nums[0][i-1] && nums[0][i] < nums[1][i])
                sum += nums[0][i] - '0' + 1;
        }
    }

    for (int i = 1; i < LINES; i++) {
        for (int j = 0; j < LEN-1; j++) {
            // most cases
            if (j != 0 && j != LEN-2) {
                if (nums[i][j] < nums[i-1][j] && nums[i][j] < nums[i][j-1] && nums[i][j] < nums[i][j+1] && nums[i][j] < nums[i+1][j])
                    sum += nums[i][j] - '0' + 1;
            } else if (j == 0) {
            // edge case left
                if (nums[i][j] < nums[i-1][j] && nums[i][j] < nums[i][j+1] && nums[i][j] < nums[i+1][j])
                    sum += nums[i][j] - '0' + 1;
            } else if (j == LEN-2) {
                // edge case right
                if (nums[i][j] < nums[i-1][j] && nums[i][j] < nums[i][j-1] && nums[i][j] < nums[i+1][j])
                    sum += nums[i][j] - '0' + 1;
            }
            
        }
    }

    printf("%ld\n", sum);
}
