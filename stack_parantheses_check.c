
#include <stdio.h>
#include <stdlib.h>

typedef struct stak 
{
    char data;
    struct stak *next;
}tsStack;



void push(tsStack **head,char val)
{
    tsStack *nu = (tsStack *)malloc(sizeof(tsStack));
    nu->data = val;
    printf("Pushed %c\n",val);
    nu->next = (*head);
    (*head) = nu;
}


char pop(tsStack **head)
{
    char res;
    tsStack *top;
    if(*head == NULL)
    {
        printf("Stack Overflow\n");
        exit(0);
    }
    top = *head;
    res = top->data;
    printf("Poping %c\n",res);
    *head = top->next;
    free(top);
    return res;
}

int isMatch(char one,char two)
{
    if(one == '(' && two  == ')')
        return 1;
    else if(one == '{' && two == '}')
        return 1;
    else if (one == '[' && two == '}')
        return 1;
    else 
        return 0;
}


int isComplete(char exp[])
{
    int i=0;
    tsStack *stack = NULL;
    
    while(exp[i])
    {
        if(exp[i] == '{' || exp[i] == '[' || exp[i] == '(')
        {
            push(&stack,exp[i]);
        }
        if(exp[i] == '}' || exp[i] == ']' || exp[i] == ')')
        {
            if (stack == NULL)
            {
                return 0;
            }
            else if(! isMatch(pop(&stack),exp[i]))
            {
                return 0;
            }
        }
        i++;
    }
    
    if(stack == NULL)
        return 1;
    else
        return 0;
}

int main()
{
    char exp[] = "[]";
    printf("Results : %d\n",isComplete(exp));

    return 0;
}

