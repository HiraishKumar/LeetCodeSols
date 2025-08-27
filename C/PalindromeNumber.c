#include <stdbool.h>


int reversed_int( int num){
    long rev_num = 0;
    while (num > 0){
        rev_num = rev_num * 10 + num % 10; 
        num = num / 10;
    }
    return rev_num;
}


bool isPalindrome(int x) {
    if (x < 0){
        return false;
    }
    long rev_num = reversed_int(x);
    if (rev_num == x){
        return true;
    } else {
        return false;
    }
    
}