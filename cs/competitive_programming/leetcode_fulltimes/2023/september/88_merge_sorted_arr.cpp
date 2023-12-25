#include <iostream>
#include <vector>

using namespace std;


class Solution1 {

public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    
        auto ptr1=nums1.begin();

        for(int idx=0; idx<n; idx++) 
        *(ptr1+m+idx)=nums2[idx]; 
        
        int it1=0, it2=0, temp=0;
        for(int idx2=0; idx2<n; idx2++) {
            for(int idx1=m-1; idx1>=0; idx1--) {
               it2                     = *(ptr1+idx1+1+idx2);
               it1                     = *(ptr1+idx1+idx2);

               if(it2<it1) {
                   temp                = *(ptr1+idx1+1+idx2);
                   *(ptr1+idx1+1+idx2) = *(ptr1+idx1+idx2);
                   *(ptr1+idx1+idx2)   = temp;
               } else {
                   break;
               }
            }
        }


    }

};

class Solution2 {

public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        
        int idx=m+n-1, idx1=m-1, idx2=n-1;

        for(;idx1>=0 && idx2>=0;)
        nums1[idx--] = nums1[idx1]>nums2[idx2]?nums1[idx1--]:nums2[idx2--];
        
        for(;idx2>=0;)
        nums1[idx--] = nums2[idx2--];
            
    }


};


void printVec(vector<int> & nums) {
    
    for(int t: nums)
    cout << t << " ";
    cout << endl;

}


int main() {

    vector<int> nums1 = {1,3,5,6,0,0,0};
    vector<int> nums2 = {2,4,7};
   
    cout << "before:" << endl;
    printVec(nums1);

    Solution2 obj2 = Solution2();
    obj2.merge(nums1, 4, nums2, 3);
    
    cout << "after:" << endl;
    printVec(nums1);

    nums1 = {1,3,5,6,0,0,0};
    cout << "before:" << endl;
    printVec(nums1);

    Solution1 obj1 = Solution1();
    obj1.merge(nums1, 4, nums2, 3);
    
    cout << "after:" << endl;
    printVec(nums1);
    
    return 0;
}
