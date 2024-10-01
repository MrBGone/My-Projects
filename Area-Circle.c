#include <stdio.h>

int main() {
    float pi = 3.14;
    int radius;

    printf("Enter The Radius of a Cicle:");
    scanf("%d",&radius);

    printf("The radius of the circle is %d \n" , radius);
    float area = (float)(pi* radius * radius);

    printf("The area of the given circle is %f", area);
    return 0;
    }