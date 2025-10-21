#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int int1;
    int int2;
    float fl1;
    float fl2;
    
	scanf("%d", &int1);
    scanf("%d", &int2);
    scanf("%f", &fl1);
    scanf("%f", &fl2);
    
    printf("%d %d\n", (int1 + int2), (int1 - int2));
    printf("%.1f %.1f",(fl1 + fl2), (fl1 - fl2));
    
    return 0;
}