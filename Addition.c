#include <stdio.h>

// simple addition program. Only works with integers.

int main() {    
    // introduce variables
    int number1, number2, sum;
    
    // user interaction with scanf
    printf("Enter two integers separated by a space: ");
    scanf("%d %d", &number1, &number2);

    // calculate the sum
    sum = number1 + number2;      
    
    printf("%d + %d = %d", number1, number2, sum);
    return 0;
}