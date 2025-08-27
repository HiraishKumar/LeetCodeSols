#include <stddef.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    char* compare = strs[0];
    int endPoint = strlen(compare);
    for (int i =0 ; i < strsSize; i++){
        for (int j = 0; j < endPoint; j++){
            if (compare[j] != strs[i][j]){
                endPoint = j;
                break;
            }
        }
    }
    
    char* result = (char*)malloc((endPoint + 1) * sizeof(char));
    if (result == NULL){
        return NULL;
    }
    strncpy(result, compare, endPoint );
    result[endPoint] = '\0';

    return result;
}