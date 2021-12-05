#include <stdio.h>

#define LIMIT 6400
unsigned char map[LIMIT][LIMIT];

int main()
{
    long ans = 0;

    // open file
    FILE *f;
    const char *input = "input.txt";
    if ((f = fopen(input, "r")) == NULL)
        return 1;

    char buf[128];
    int x1, x2, y1, y2;
    int high, low;
    while (fgets(buf, sizeof(buf), f)) {
        // why sscanf https://www.sas.upenn.edu/~saul/parasite/man/man3/scanf.3.html
        sscanf(buf, "%d,%d -> %d,%d", &x1, &y1, &x2, &y2);
        
        if (x1 == x2) {
            high = y1 > y2 ? y1 : y2;
            low = y1 < y2 ? y1 : y2;
            while (low <= high)
                map[x1][low++]++;
        } else if (y1 == y2) {
            high = x1 > x2 ? x1 : x2;
            low = x1 < x2 ? x1 : x2;
            while (low <= high)
                map[low++][y1]++;
        } else {
            int prog_x = x1 < x2 ? 1 : -1;
            int prog_y = y1 < y2 ? 1 : -1;
            int iter = (prog_x == 1 ? (x2 - x1) : (x1 - x2)) + 1;
            for (int i = 0; i < iter; i++) {
                map[x1][y1]++;
                x1 += prog_x;
                y1 += prog_y;
            }
        }
    }

    for (int i = 0; i < LIMIT; i++) {
        for (int j = 0; j < LIMIT; j++) {
            if (map[i][j] >= 2)
                ans++;
        }
    }
    
    printf("%ld\n", ans);

    fclose(f);
}
