#include <stdio.h>

int max_of_four(int a, int b, int c, int d) {
    int integers[4]; 
    integers[0] = a;
    integers[1] = b;
    integers[2] = c;
    integers[3] = d;

    int max = integers[0]; 

    for(int i = 1; i < 4; i++){ 
        if(integers[i] > max){
            max = integers[i];
        }
    }
    return max;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}