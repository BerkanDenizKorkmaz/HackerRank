#include <stdio.h>
#include <stdlib.h>

void update(int *a,int *b) {
    int a_mem = *a;
    int b_mem = *b;
    
    *a = a_mem + b_mem;
    *b = abs(a_mem - b_mem);    
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}