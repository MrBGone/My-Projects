# include <stdio.h>

int main() {
    
    // SI = Simple interest
    // P = Principal
    // R = Rate of Interest
    // T = Time Period

    // int P, R, T;
    int P, T;
    float R;

    printf("Enter the principal: ");
    scanf("%d", &P);

    printf("Enter the rate: ");
    scanf("%f", &R);
    
    printf("Enter the time: ");
    scanf("%d", &T);

    //Calculation of simple Interest
    double SI = (P * R * T) / 100;

    printf("The Simple interest is %lf", SI);
    return 0;
    }