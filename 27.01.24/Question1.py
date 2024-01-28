# time conversion

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* timeConversion(char* s) {
    // Allocate memory for the result string
    char* result = (char*)malloc(9 * sizeof(char));
    
    // Extract hours, minutes, seconds, and AM/PM indicator from the input string
    int hours, minutes, seconds;
    char period[3];
    sscanf(s, "%d:%d:%d%s", &hours, &minutes, &seconds, period);
    
    // Adjust hours based on AM/PM and convert to 24-hour format
    if (strcmp(period, "AM") == 0) {
        if (hours == 12) {
            hours = 0; // 12:00:00 AM is 00:00:00 in 24-hour format
        }
    } else {
        if (hours != 12) {
            hours += 12; // Add 12 hours to convert PM to 24-hour format
        }
    }
    
    // Format the result string
    sprintf(result, "%02d:%02d:%02d", hours, minutes, seconds);
    
    return result;
}

int main() {
    // Read the input time string
    char* s = (char*)malloc(11 * sizeof(char));
    fgets(s, 11, stdin);
    
    // Convert the time to 24-hour format
    char* result = timeConversion(s);
    
    // Print the result
    printf("%s\n", result);
    
    // Free dynamically allocated memory
    free(s);
    free(result);
    
    return 0;
}
