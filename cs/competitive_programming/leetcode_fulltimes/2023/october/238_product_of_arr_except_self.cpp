#include <iostream>
#include <vector>

using namespace std;

class Solution {

public:
    vector<int> productExceptSelf(vector<int>& nums) {

        int n        = nums.size();
        vector<int> res(n,1);

        int l=1;
        for(int i=0; i<n; i++) {
            res[i] *= l;
            l      *= nums[i];
        }

        int r=1;
        for(int i=n-1; i>=0; i--) {
            res[i] *= r;
            r      *= nums[i];
        }

        return res;

    }
};

int main() {

    vector<int> nums{1,2,3,4};
    vector<int> out;
    
    Solution obj = Solution();
    out          = obj.productExceptSelf(nums);      

    cout << "output: " << endl;
    for(auto ptr=out.begin(); ptr!=out.end(); ptr++) {
        cout << *ptr << " ";
    }
    cout << endl;

    return 0;
}
