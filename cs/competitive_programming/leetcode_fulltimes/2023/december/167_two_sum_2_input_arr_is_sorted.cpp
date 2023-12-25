#include <iostream>
#include <vector>

class Solution {

public:
    int helper(int l, int r, int target, std::vector<int>& nums) {
        int m=0;
        while(l<=r) {

            m = l + (r-l)/2;

            if(nums[m] == target) {
                return m;
            } else if(nums[m] < target) {
                l = m+1;
            } else {
                r = m-1;
            }
        }
        return -1;
    }

    std::vector<int> twoSum(std::vector<int>& numbers, int target) {
        std::vector<int> res;
        int idx = 0, n = numbers.size(), ano_num = 0;

        for(int i = 0; i < n; i++) {
            ano_num = target - numbers[i];

            if(ano_num >= numbers[i]) {
                idx = helper(i+1, n-1, ano_num, numbers);
            } else {
                idx = helper(0, i, ano_num, numbers);
            }

            if( idx != -1 ) {
               res.push_back( i+1 );
               res.push_back( idx+1  );
               break;
            }
        }

        return res;
    }

};

int main() {

    std::vector<int> in_list = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> res;

    Solution sol;
    res = sol.twoSum( in_list, target );

    std::cout << "[ " << res[0] << ", " << res[1] << " ]" << std::endl;

    return 0;
}
