class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        
        int o = 0;
        int b = 0;
        int i=31;

        while(n>0) {

            b = n%2; // b = n&1;
            o = o + (b<<i);
            i--;
            n = n>>1;
        }

        return o;

    }
};
