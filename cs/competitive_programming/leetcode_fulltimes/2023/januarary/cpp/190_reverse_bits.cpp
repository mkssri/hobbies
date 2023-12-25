#include <iostream>

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        
        uint32_t res = 0;
        int d = 0;

        while(n>0){
            res = res + ((n%2) << (31-d));
            n = n>>1;
            d++;
        }

        return res;
    }
};

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {

        uint32_t res=0;
        int d=0;
        while(n>0){

            int tmp = 0;
            tmp = n%2;
            
            res = res + (tmp << (31-d));
            n=n>>1;
            d++;
        }

        return res;

    }
};
