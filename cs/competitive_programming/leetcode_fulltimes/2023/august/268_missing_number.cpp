#include <iostream>
#include <vector>

using namespace std;

class Solution {

public:
    int missingNumber(vector<int>& nums) {

        int si = nums.size();
        int res = si;

        for(int i=0; i<si; i++) {
            res ^= i;
            res ^=nums[i];
        }

        return res;
    }
    
    int missingNumberV1(vector<int>& nums) {

        int si = nums.size();
        long long res = 0;
        long long tot = si*(si+1)/2; //you can also check if si is even/odd and accordingly divide by 2 first before multiplying

        //for(auto iter=nums.begin(); iter!=nums.end(); iter++) 
        for(vector<int>::iterator iter=nums.begin(); iter!=nums.end(); iter++) 
        res += *iter;

        return tot-res;
    }
};


int main() {

    Solution obj;

    vector<int> nums = {0,1,3};
    cout << "missing number: " << obj.missingNumber(nums) << endl;
    cout << "missing number: " << obj.missingNumberV1(nums) << endl;

    return 0;
}
