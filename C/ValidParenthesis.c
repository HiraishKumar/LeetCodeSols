#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool isValid(char* s) {
    char stack[strlen(s)];
    int top = -1;

    for(int i = 0; i < strlen(s); i++){
        if(s[i] == '{' || s[i] == '[' || s[i] == '(' ){
            stack[++top] = s[i];
        } else if (stack[top] != '{' && stack[i] == '}' ||
                   stack[top] != '[' && stack[i] == ']' ||
                   stack[top] != '(' && stack[i] == ')')
                   return false;
        top--;
    }
    return top == -1;
}