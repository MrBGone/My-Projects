#include <stdio.h>
#include <math.h>

int main() {
    int intOperand1 = 8;
    int intOperand2 = 4;
    float floatOperand1 = 9.5;
    float floatOperand2 = 3.5;

    // int operand int
    printf("int operand int:\n");
    printf("%d + %d = %d\n", intOperand1, intOperand2, intOperand1 + intOperand2);
    printf("%d - %d = %d\n", intOperand1, intOperand2, intOperand1 - intOperand2);
    printf("%d * %d = %d\n", intOperand1, intOperand2, intOperand1 * intOperand2);
    printf("%d / %d = %d\n", intOperand1, intOperand2, intOperand1 / intOperand2);

    // int operand foat
    printf("int operand float:\n");
    printf("%d + %f = %f\n", intOperand1, floatOperand2, intOperand1 + floatOperand2);
    printf("%d - %f = %f\n", intOperand1, floatOperand2, intOperand1 - floatOperand2);
    printf("%d * %f = %f\n", intOperand1, floatOperand2, intOperand1 * floatOperand2);
    printf("%d / %f = %f\n", intOperand1, floatOperand2, intOperand1 / floatOperand2);

    // float operand float
    printf("int operand int:\n");
    printf("%f + %f = %f\n", floatOperand1, floatOperand2, floatOperand1 + floatOperand2);
    printf("%f - %f = %f\n", floatOperand1, floatOperand2, floatOperand1 - floatOperand2);
    printf("%f * %f = %f\n", floatOperand1, floatOperand2, floatOperand1 * floatOperand2);
    printf("%f / %f = %f\n", floatOperand1, floatOperand2, floatOperand1 / floatOperand2);

    return 0;
}