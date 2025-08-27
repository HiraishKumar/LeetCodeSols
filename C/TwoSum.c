#include <stdlib.h>
#include <cstddef>


typedef struct 
{
    int key;
    int value;
    int used;
}HashItem;


int hash(int key, int size){
    if (key < 0){
        key = -key;
    }
    return key % size;
};

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int tablesize = numsSize * 2;
    int* result = (int*) malloc (2 * sizeof(int));
    HashItem* table = calloc(tablesize, sizeof(HashItem));

    for(int i = 0; i < numsSize; i++){
        int complemnet = target - nums[i]; 
        int h = hash(complemnet, tablesize);

        while (table[h].used){
            if (table[h].key == complemnet){
                result[0] = table[h].value;
                result[1] = i;
                free(table);
                return result;
            };
            h = (h + 1) % tablesize;
        };

        h = hash(nums[i], tablesize );
        while (table[h].used){
            h = (h + 1) % tablesize;
        }
        table[h].key = nums[i];
        table[h].value = i ;
        table[h].used = 1;  
    }
    free(table);
    return NULL;
}