class Solution {
public:
    int getSum(int a, int b) {
        if(b==0) return a;
        else{
            return getSum(a^b, (unsigned int)(a&b)<<1);
        }
    }
};

class Solution {
public:
    int getSum(int a, int b) {

        int carry;
        while(b!=0){
            carry = (unsigned int)(a&b)<<1;
            a = (a^b);
            b = carry;
        }

        return a;
        
    }
};