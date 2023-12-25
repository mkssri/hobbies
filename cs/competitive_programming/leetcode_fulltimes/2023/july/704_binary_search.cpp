class Solution {
public:
    int search(vector<int>& nums, int target) {

        int st = 0, mid = 0, end = nums.size()-1;

        while(st<=end) {
            
            mid = (st+end)/2;

            if(nums[mid]==target) {
                return mid;
            } else if(nums[mid] < target) {
                st = mid+1;
            } else {
                end = mid-1;
            }

        }

        return -1;
    }
};

class Solution {
public:
    int search(vector<int>& nums, int target) {

        int* ptr = &nums[0];
        size_t l = nums.size();
        int s=0, e=l-1;
        int m=0;
        int ele=0;

        while(s<=e) {
            m = (s+e)/2;
            ele = *(ptr+m);
            if(ele==target) {
                return m;
            } else if( ele<target ){
                s=m+1;
            } else {
                e=m-1;
            }

        }
        return -1;
    }
};
