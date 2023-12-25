#include <iostream>
#include <vector>


class Solution {
public:
    int missingNumber(std::vector<int>& nums) {

        int n = nums.size();
        
        int res = 0;
        for(int i=0; i<=n; i++){
            res = res^i;
        }

        for(auto &i: nums){
            res = res^i;
        }

        return res;
    }
};

class Solution {
public:
    int missingNumber(std::vector<int>& nums) {

        int res = 0;
        int n = nums.size();
        std::set<int> s(nums.begin(), nums.end());

        for(int i=0;i<=n;i++){
            auto it = s.find(i);
            if (it != s.end()){
                continue;
            } else {
                res = i;
                break;
            }
        }
        
        return res;
    }
};