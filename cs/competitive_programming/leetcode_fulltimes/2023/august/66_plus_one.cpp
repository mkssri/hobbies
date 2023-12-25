#include <iostream>
#include <vector>

using namespace std;

void print_vec(vector<int>&); 

class Solution {

public:
    vector<int> plusOne(vector<int>& digits) {


       int c=0;
       int si=digits.size();

       digits[si-1]++;

       for(int idx=si-1; idx>=0; idx--) {
            digits[idx]+=c;
            c=digits[idx]/10;
            digits[idx]%=10; 

            if(c==0)
                break;
       }

       if(c!=0)
            digits.insert(digits.begin(), c);

        
        return digits;
    }
};

void print_vec(vector<int>& vec ) {
    for(auto iter=vec.begin(); iter!=vec.end(); iter++)
        cout << *iter;
}

int main() {

    vector<int> digits = {9,9,9,9,9,9,9,9,9,9,9,9,9};
    
    cout << "input digits: ";
    print_vec(digits); 
   
    Solution().plusOne(digits);

    cout << endl;
    cout << "output digits: ";
    print_vec(digits); 
    cout << endl;
    
    vector<int> digits1 = {9,9,9};
    
    cout << "input digits: ";
    print_vec(digits1); 
   
    Solution().plusOne(digits1);

    cout << endl;
    cout << "output digits: ";
    print_vec(digits1); 
    cout << endl;

    return 0;
}
