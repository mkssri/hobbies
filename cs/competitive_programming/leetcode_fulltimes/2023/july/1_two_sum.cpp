class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        int c = nums.size();

        vector<int> res;

        for(int i=0; i<c; i++) {
            for(int j=i+1; j<c; j++) {
                if((nums[i]+nums[j])==target) {
                    res.push_back(i);
                    res.push_back(j);
                    break;
                }
            }
        }
        return res;
    }
};

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> table;
        int c = nums.size();
        int complement = 0;


        for(int i=0; i<c; i++) {
            complement = target-nums[i];

            if(table.count(complement)){
                return {i, table[complement]};
            }
            table[nums[i]] = i;
        }

        return {};

    }
};
