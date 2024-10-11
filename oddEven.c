#include <stdio.h>

// Write a program to check if a number is divisible by 2 (odd or even).
int main(){
    int divisible;
    printf("Let's test odd or even.\nEnter a number: ");
    scanf("%d", &divisible);
    // The last step checks the mod of the input number. If true, it returns 1. If false, it returns 0.
    if (divisible % 2 == 0) {
        printf("True\n");
    }   else {
            printf("False\n");
        }
    return 0;
}