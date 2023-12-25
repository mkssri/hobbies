class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        set<int> s1(nums.begin(), nums.end());
        
        // for(auto i: nums){
        //     s1.insert(i);            
        // }

        if (nums.size()==s1.size())
        return  false;
        return true;


    }
};

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        sort(nums.begin(), nums.end());

        for(int i=0; i<nums.size()-1; i++){
            if(nums[i+1]==nums[i]){
                return true;
            }
        }
        return false;
    }
};

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        unordered_set<int> st;

        for(auto i: nums){
            if(st.find(i) != st.end()){
                return true;
            }
            st.insert(i);
        }
        return false;
    }
};

