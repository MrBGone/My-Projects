#include <stdio.h>
 
int main() {
    int side, area;
    printf("Enter the Length of a Side : \n");
    scanf("%d", &side);
 
    area = side * side;
    printf("The Area of the Square is: %d \n", area);
 
    return (0);
    }