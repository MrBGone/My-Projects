#include <stdio.h>
#include <math.h>
#include <string.h>

int main(){

// Part 1: Program that includes all main arithmetic operations.
/*     int a = 10;
    int b = 5;

    int addition = a + b;
    printf("Addition: %d + %d = %d\n", a, b, addition);

    int subtraction = a - b;
    printf("Subtraction: %d - %d = %d\n", a, b, subtraction);

    int multiply = a * b;
    printf("Multiplication: %d * %d = %d\n", a, b, multiply);

    int divide = a / b;
    printf("Division: %d / %d = %d\n", a, b, divide);

    int modulus = a % b;
    printf("Modulus: %d mod %d = %d\n", a, b, modulus);

    double power = pow(a, b);
    printf("Power: %d + %d = %f\n", a, b, power); */

// Part 2: Type conversion.
/*     printf("%d \n", 3/2);
    printf("%f \n", 3.0/2); */

// Part 3: Write a program to check if a number is divisible by 2.
/*     int divisible;
    printf("Enter a number.");
    scanf("%d", &divisible);
    // The last step checks the mod of the input number. If true, it returns 1. If false, it returns 0.
    if (divisible % 2 == 0) {
        printf("True\n");
    }   else {
            printf("False\n");
        }
    printf("%d \n", divisible%2==0); */

// Part 4: Print True (1) or False (0) if a number is greater than 10 and less than 20.
/*     int f;
    printf("Enter a number.");
    scanf("%d", &f);
    printf("%d", (f>10) && (f<20)); */
    char a[10];
    char b[] = "yes";
    char c[10];
    printf("Is it Monday?\n");
    scanf("%s", &a);
    int result1 = strcmp(a, b);
    if (result1 == 0) {
        printf("It's monday\n");
    }   else {
            printf("Its not Monday\n");
    }
    printf("Is it snowing?\n");
    scanf("%s", &c);
    int result2 = strcmp(c, b);
    if (result2 == 0) {
        printf("It's snowing\n");
    }   else {
            printf("Its not snowing\n");
    }
    printf("%d\n", result1);
    printf("%d\n", result2);
    if (result1 || result2 == -1) {
        result1 = 1;
        result2 = 1;
    } else {
        return 0;
    }
    printf("%d\n", result1);
    printf("%d\n", result2);
    int final = result1 || result2;
    printf("%d\n", final);
    if (final == 0) {
        printf("It is not Monday and it is not snowing\n");
    }
    else if (result1 = 0) {
        printf("It is Monday but it is not snowing.");
    }
    else if (result2 = 0) {
        printf("It is snowing but it is Monday");
    }
    else (result1, result2 = 0);
        printf("It is snowing and it is Monday");
    
   // printf("It is either Monday and snowing or one of the two.");

    return 0;
}