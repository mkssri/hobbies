class Solution {
public:
    int hammingWeight(uint32_t n) {
        
        int out = 0;

        while(n>0) {
            if((n%2)==1){
                out += 1;
            }
            n = n>>1;
        }

        return out;
    }
};

class Solution {
public:
    int hammingWeight(uint32_t n) {

        int out = 0;

        while(n>0) {
            if((n&1)==1){
                out += 1;
            }
            n = n>>1;
        }

        return out;
    }
};

class Solution {
public:
    int hammingWeight(uint32_t n) {

        int cnt = 0;

        for(int i=0; i<=31; i++) {
            cnt += (n&1);
            n = (n>>1);
        }

        return cnt;

    }
};
