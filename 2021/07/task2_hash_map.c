#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>

#define LIMIT 1000
#define MAP_SIZE 1000000
#define NOT_IN_MAP -1

// key -> step size f.ex: 3-1=2
// value -> step, f.ex 1+2=3
struct Fuel {
    int key;
    int value;
};

struct Fuel *map[MAP_SIZE];

int hash_code(int key)
{
    return key % MAP_SIZE;
}

int search(int key)
{
    // get index
    int index = hash_code(key);
    
    // move until we find desired value
    while (map[index] != NULL) {
        if (map[index]->key == key)
            return map[index]->value;

        index++;
        index %= MAP_SIZE;
    }
    return NOT_IN_MAP;
}

void insert(int key, int value)
{
    struct Fuel *item = (struct Fuel*) malloc(sizeof(struct Fuel));
    item->key = key;
    item->value = value;

    int index = hash_code(key);
    while (map[index] != NULL && map[index]->key != -1) {
        index++;
        index %= MAP_SIZE;
    }
    
    map[index] = item;
}

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
    
    // open, read and store data in nums
    FILE *fileptr = fopen(file_name, "r");
    char current_str[5] = "";
    int iter = 0;
    int largest = 0;
    int len;
    int num;
    char current_char = fgetc(fileptr);
    while (current_char != EOF && current_char != '\n') {
        if (current_char == ',') {
            num = atoi(current_str);
            if (num > largest)
                largest = num;
            nums[iter] = num;
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


    int current;
    long min = INT_MAX;
    for (int i = 0; i < largest; i++) {
        long ith_sum = 0;
        for (int j = 0; j < LIMIT; j++) {
            // pointless calculating rest a series if it's larger than min
            if (ith_sum > min)
                break;
           
            int key = abs(i - nums[j]);
            current = search(key);
            if (current == NOT_IN_MAP) {
                int value = step(key + 1);
                insert(key, value);
                ith_sum += value;
            } else {
                ith_sum += current;
            }

            //ith_sum += step(abs(i - nums[j]) + 1);
            //printf("%d + %d = %d\n", i, nums[j], step(abs(i - nums[j]) + 1));
        }
        if (ith_sum < min)
            min = ith_sum;
    }
    
    printf("%ld\n", min);
}
