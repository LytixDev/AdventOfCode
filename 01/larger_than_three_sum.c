#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// len here means amount of lines in file, and not size
int find_file_len(char *file_name)
{
    FILE *fileptr;
    int filelen = 0;
    fileptr = fopen(file_name, "rb");
    
    char sample_chr = getc(fileptr);
    
    while (sample_chr != EOF) {
        // count whenever sample_chr is blank (new line) is encountered
        if (sample_chr == '\n')
            filelen += 1;
        sample_chr = getc(fileptr);
    }
    fclose(fileptr);
    return filelen;
}

char *read_file(long filelen, char *file_name)
{
    FILE *fileptr;
    char *buffer;

    // open the file in binary mode
    fileptr = fopen(file_name, "rb");

    // redundant check is we know from find_files this file must exist
    //if (fileptr == NULL) {
    //    return '\0';
    //}

    buffer = malloc(filelen);
    fread(buffer, filelen, 1, fileptr); 
    fclose(fileptr);
    return buffer;
}

int main()
{
    // test data
    //int measurements[] = {199, 200, 208, 210, 200, 207, 240, 269, 260, 263};

    char *input_data = "measurement.txt";
    int lines = find_file_len(input_data);
    printf("Total lines: %ld\n", lines);

    int *measurements = (int *) malloc(sizeof(int) * lines);
    int total_increased = 0;

    // fill measurements array
    FILE *fileptr = fopen(input_data, "r");
    if (fileptr == NULL) {
        printf("File '%s' can't be opened\n", input_data);
        exit(0);
    }

    int i = 0;
    char str[5];
    char current_char = fgetc(fileptr);
    while (current_char != EOF) {
        if (current_char != '\n') {
            strcat(str, &current_char);
        } else {
            printf("str: %s, i: %d\n", str, i);
            measurements[i] = atoi(str);
            strcpy(str, "");  // reset string
            i++;
        }
        current_char = fgetc(fileptr);
    }

    int old = measurements[0];
    int mid = measurements[1];
    int new = measurements[2];
    float prev = ((float) old + (float) mid + (float) new) / 3;
    for (int i = 3; i <= lines; i++) {
        old = mid;
        mid = new;
        new = measurements[i];
        float current = ((float) old + (float) mid + (float) new) / 3;
        if (current > prev)
            total_increased++;
        prev = current;
    }

    printf("Measurements that are larger than the previous measurement: %d\n", total_increased);
    free(measurements);
}
