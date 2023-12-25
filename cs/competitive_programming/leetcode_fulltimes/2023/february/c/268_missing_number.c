int missingNumber(int* nums, int numsSize){

    int res = numsSize;
    int k = 0;

    for(k=0; k<numsSize; k++){
        res = res^k;
        res = res^(*(nums+k));
    }
    return res;

}