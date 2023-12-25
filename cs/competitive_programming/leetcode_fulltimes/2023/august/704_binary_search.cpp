#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {

        int st=0, ed=nums.size()-1, md=0;

        for(;st<=ed;) {
            md = st+(ed-st)/2;

            if(nums[md]>target) {
                ed = md-1;
            } else if(nums[md]<target) {
                st = md+1;
            } else {
                return md;
            }

        }

        return -1;
    }
};

int main() {
    
    vector<int> nums = {1,2,3,6,8,100};
    Solution obj;
    cout << "output: " << obj.search(nums, 3) << endl;

    return 0;
}
