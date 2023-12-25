class Solution {
public:
    int search(vector<int>& nums, int target) {

        int l=0, r=nums.size()-1;
        int m=0;

        while(l<=r) {
            m = l+(r-l)/2;

            if(nums[m]==target) {
                return m;
            }

            // mid point is on left side
            if(nums[m]>=nums[l]) {

                if( (target>nums[m]) || (target<nums[l]) ) {
                    l = m+1;
                } else {
                    r = m-1;
                }

            }
            else { // mid point is on right side

                if( (target<nums[m]) || (target>nums[r])) {
                    r = m-1;
                } else {
                    l = m+1;
                }


            } 


        }

        return -1;
        
    }
};
