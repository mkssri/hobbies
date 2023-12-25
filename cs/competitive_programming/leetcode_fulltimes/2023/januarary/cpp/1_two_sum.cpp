#include <iostream>
#include <vector>
#include <map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> visited;

        for(int i=0; i<nums.size(); i++){
            int n = nums[i];
            int complement = target-nums[i];

            if(visited.count(complement)){
                return {i, visited[complement]};
            }

            visited[nums[i]]=i;

        }
        return {};
    }
};


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        int n = nums.size();
        map<int, int> mp;


        for(int i=0; i<n; i++){
            mp[nums[i]]=i;
        }


        for(int i=0; i<n; i++){
            int complement=target-nums[i];

            if(mp.count(complement) && (i!=mp[complement])){
                return {i, mp[complement]};
            }

        }

        return {};
    }
};