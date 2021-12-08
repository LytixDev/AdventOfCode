#include <stdio.h>

#define MAX 100

int main()
{
    char buffer[128];
    int i, right = 0, right_sum = 0, count_sum = 0;
    int counts[7] = {0};

    FILE *fp = fopen("input.txt", "r");
    if (fp == NULL)
        return -1;

    while (fgets(buffer, MAX, fp))
    {
        for (i = 0; i < 7; i++)
            counts[i] = 0;

        for (i = 0; i < MAX; i++) {
            if (buffer[i] == '|')
                break;
            else if (buffer[i] == ' ')
                continue;
            counts[buffer[i] - 'a'] += 1;
        }

        right = count_sum = 0;
        for (i += 2; i < MAX; i++) {
            if (buffer[i] == ' ' || buffer[i] == '\n') {
                right *= 10;
                switch (count_sum) {
                    case 42: break;
                    case 17: right++; break;
                    case 34: right += 2; break;
                    case 39: right += 3; break;
                    case 30: right += 4; break;
                    case 37: right += 5; break;
                    case 41: right += 6; break;
                    case 25: right += 7; break;
                    case 49: right += 8; break;
                    case 45: right += 9; break;
                    default: return -1;
                }

                count_sum = 0;
                if (buffer[i] == '\n') {
                    right_sum += right;
                    break;
                }
            }
            else 
                count_sum += counts[buffer[i] - 'a'];
        }
    }

    printf("%d\n", right_sum);
    fclose(fp);
    return 0;
}
