#include <string.h>

int value(char a){
    switch (a){
    case 'I':
        return 1;
    case 'V':
        return 5;
    case 'X':
        return 10;
    case 'L':
        return 50;
    case 'C':
        return 100;
    case 'D':
        return 500;
    case 'M':
        return 1000;
    default:
        return 0;
    }
}

int romanToInt(char* s) {
    int curchar;
    int nexchar;
    int result= 0;
    int len = strlen(s);

    for (int i = 0; i < len; i++ ){
        curchar = value(s[i]);
        if (i + 1 < len){
            nexchar = value(s[i+1]);

            if (curchar < nexchar ){
                result += nexchar - curchar;
                i++;
            }else{
                result += curchar;
            }
        } else{
            result += curchar;
        } 
    }
    return result;
}