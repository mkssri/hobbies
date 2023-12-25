#include <iostream>
#include <unordered_set>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

       std::unordered_set<int> myset = {};
       std::vector<int>::iterator it;
       int vec_len=0, set_len=0;

       for(it=nums.begin(); it!=nums.end(); ++it){
          vec_len++;
          myset.insert(*it);
       }

      unordered_set<int>::iterator it_set;

      for(it_set=myset.begin(); it_set!=myset.end(); it_set++){
         set_len++;
      }

      if(vec_len==set_len){
         return false;
      }
      return true;
        
    }
};
