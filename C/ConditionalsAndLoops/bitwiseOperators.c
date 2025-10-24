#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void calculate_the_maximum(int n, int k) {
    int and_max = 0;
    int or_max = 0;
    int xor_max = 0;

    int and_current;
    int or_current;
    int xor_current;

    for(int i =1; i<=n; i++){
        for (int ii = i+1; ii <=n; ii++) {
            and_current = i & ii;
            or_current = i | ii;
            xor_current = i ^ ii;
            
            if ( (and_current > and_max) && and_current < k) {
                and_max = and_current;
            }
            if ( (or_current > or_max) && or_current < k) {
                or_max = or_current;
            }
            if ( (xor_current > xor_max) && xor_current < k) {
                xor_max = xor_current;
            }
        }
    }
    printf("%d\n", and_max);
    printf("%d\n", or_max);
    printf("%d\n", xor_max);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}