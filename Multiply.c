#include <stdio.h>

int main() {    

    int number1, number2, mul;
    
    printf("Enter two integers separated by a space: ");
    scanf("%d %d", &number1, &number2);

    // calculate the sum
    mul = number1 * number2;      
    
    printf("%d x %d = %d", number1, number2, mul);
    return 0;
}