int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

bool containsDuplicate(int* nums, int numsSize){

   qsort(nums, numsSize, sizeof(int), cmpfunc);

   int i=0;
   while(i<numsSize-1){
       if(*(nums+i)==*(nums+i+1))
        return true;
       i++;
   }
   return false;
}
