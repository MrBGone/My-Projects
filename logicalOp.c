#include <stdio.h>

int main(){
    printf("%d\n", (5==5) && (3<5));
    printf("%d\n", (5==5) && (3>5));
    printf("%d\n", (5==5) || (3>5));
    printf("%d\n", (5==4) || (3>5));
    printf("%d\n", 5 != 3);
    printf("%d", 5 != 5);
    return 0;
}