class Solution {
public:
    int reverse(int x) {

        bool neg = (x<0);
        x = abs(x);
        int res = 0;
        int tmp = 0;

        while(x>0){
            
            tmp = x%10;

            if( (double)INT_MAX/res <= 10)
            return 0;

            res = 10*res + tmp;

            x = x/10;
        }

        if(neg)
        return -1*res;
        
        return res;

    }
};

class Solution {
public:
    int reverse(int x) {
bool neg = (x<0);
    int tmp = 0;
    int res = 0;
    x = abs(x);

    while(x>0){

        tmp = x%10;

        if((double)INT_MAX/res <=10){
            return 0;
        }

        res = 10*res+tmp;
        x = x/10;
    }

    if(neg){
        return -1*res;
    }
    return res;
    }
};
