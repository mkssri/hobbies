#include <iostream>
#include <vector>

class Solution {
public:
    vector<int> countBits(int n) {

        vector<int> ans;

        for(int i=0; i<=n; i++){
            ans.push_back(helper(i, 0));
        }
        return ans;   
    }

    int helper(int n, int res){
        while(n>0){
            res += (n&1);
            n = n>>1;
        }
        return res;
    }
};



#include <cstdlib>
class Solution {
public:
    vector<int> countBits(int n) {
        
        vector<int> ans;
        ans.push_back(0);

        for(int i=1; i<=n; i++){
            ans.push_back(ans[div(i,2).quot]+div(i,2).rem);
        }
        return ans;
    }
};