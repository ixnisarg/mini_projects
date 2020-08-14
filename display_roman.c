#include <stdio.h>

typedef struct program{
    char *sym;
    int val;
}romanMap;

int maxNumber(romanMap *nu,int val)
{
    int index;
    for(int i=0;i<10;i++)
    {
        if(nu[i].val <= val)
            index = i;
    }
    return index;
}

void decToRoman(romanMap *nu,int val)
{
    int max;
    if(val != 0)
    {
        max = maxNumber(nu,val);
        printf("%s",nu[max].sym);
        val = val - nu[max].val;
        decToRoman(nu,val);
    }
}
int main()
{
    romanMap nu[10] = {
        {"I",1},
        {"IV",4},
        {"V",5},
        {"IX",9},
        {"X",10},
        {"XL",40},
        {"L",50},
        {"XC",90},
        {"C",100},
        {"CD",400},
    };
    int n = 6;
    if(n>0 && n<=400)
    {
        decToRoman(nu,n);
    }
    return 0;
}

