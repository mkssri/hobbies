class Solution {

public:
    int climbStairs(int n) {

        if(n==1||n==2)
            return n;
        else {
            int x=2, y=1, temp=0;

            for(int i=3; i<=n; i++) {
                temp = x+y;
                y = x;
                x = temp;
            }
            return temp;
        }

    }
};
