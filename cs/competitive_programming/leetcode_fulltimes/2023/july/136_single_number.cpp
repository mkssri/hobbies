class Solution {
public:
    int singleNumber(vector<int>& nums) {

        int c = nums.size();
        int o = 0;

        for(int i=0; i<c; i++) {
            o = (o^nums[i]);
        }
        
        return o;
    }
};
