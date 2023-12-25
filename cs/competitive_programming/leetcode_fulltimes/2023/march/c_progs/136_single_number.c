/*
 Author: Murali Sriram
 Date: 03/26/2023
 Purpose: Murali Solved LC problem 136, which outputs single number for list of numbers(each number is repeated once except one number)
*/
int singleNumber(int* nums, int numsSize){

        int tmp = 0;

        for(int i=0; i<numsSize; ++i){
                    tmp = tmp ^ *(nums+i);
                        
        }
            
            return tmp;
            
}
