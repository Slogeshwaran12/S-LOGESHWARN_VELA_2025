//Max Min


#include <stdio.h>
#include <stdlib.h>

char* readline();
char* ltrim(char*);
char* rtrim(char*);
int parse_int(char*);

/*
 * Complete the 'maxMin' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY arr
 */

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int maxMin(int k, int arr_count, int* arr) {
    // Sort the array in ascending order
    qsort(arr, arr_count, sizeof(int), compare);
    
    int unfairness = arr[k - 1] - arr[0];
    for (int i = 1; i <= arr_count - k; i++) {
        int diff = arr[i + k - 1] - arr[i];
        if (diff < unfairness)
            unfairness = diff;
    }
    return unfairness;
}

int main() {
    int n = parse_int(ltrim(rtrim(readline())));
    int k = parse_int(ltrim(rtrim(readline())));
    int* arr = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        int arr_item = parse_int(ltrim(rtrim(readline())));
        *(arr + i) = arr_item;
    }

    int result = maxMin(k, n, arr);
    printf("%d\n", result);

    free(arr);
    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (1) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);
        if (!line) break;

        data_length += strlen(cursor);
        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') break;
        alloc_length <<= 1;
        data = realloc(data, alloc_length);
        if (!data) break;
    }

    if (data[data_length - 1] == '\n') data[data_length - 1] = '\0';
    data = realloc(data, data_length);
    return data;
}

char* ltrim(char* str) {
    if (!str) return '\0';
    if (!*str) return str;

    while (*str != '\0' && isspace(*str)) str++;
    return str;
}

char* rtrim(char* str) {
    if (!str) return '\0';
    if (!*str) return str;

    char* end = str + strlen(str) - 1;
    while (end >= str && isspace(*end)) end--;
    *(end + 1) = '\0';
    return str;
}

int parse_int(char* str) {
    char* endptr;
    int value = strtol(str, &endptr, 10);
    if (endptr == str || *endptr != '\0') exit(EXIT_FAILURE);
    return value;
}
