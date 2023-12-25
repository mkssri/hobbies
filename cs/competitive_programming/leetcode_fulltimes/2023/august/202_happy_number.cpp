#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {

public:

    int helper(int n) {
        int temp=0;
        for(;n>0;) {
            temp += pow(n%10,2);
            n=n/10;
        }
        return temp;
    }

    bool isHappy(int n) {
        int res=0;
        unordered_set<int> s;
        s.insert(n);

        for(;;){
            res = helper(n);
            if(res==1)
            return true;
            else if(s.count(res)==1)
            return false;
            else
            s.insert(res);
            n = res;
        }
    }

};

int main() {

    Solution obj;
    
    cout << "For n=2, res= " << obj.isHappy(2) << endl;
    cout << "For n=19, res= " << obj.isHappy(19) << endl;

    return 0;
}
