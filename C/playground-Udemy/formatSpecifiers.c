#include <stdio.h>
#include <stdbool.h>

int main(){
    int integerVar = 100;
    float floatingVar = 333.79;
    double doubleVar = 8.44e+11;
    char charVar = 'W';
    bool boolVar = 0;

    printf("integerVar - %d\n", integerVar);
    printf("floatingVar - %f\n", floatingVar);
    printf("doubleVar - %e\n", doubleVar);
    printf("doubleVar - %g\n", doubleVar);
    printf("charVar - %c\n", charVar);
    printf("boolVar - %i\n", boolVar);

    return 0;
}