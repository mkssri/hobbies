#include <set>
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int si=s.size(), si_substr=0;
        int st=0;
        set<int> substr;
        int res=0;

        for(int en=0; en<si; en++) {
            for(;substr.count(st)!=0;) {
                substr.erase(s[st]);
                st++;
            }
            substr.insert(s[en]);
            si_substr=substr.size();
            res = max(res, si_substr);
        }

        return res;

    }
};

int main() {

    Solution obj=Solution();
    string in("au");    
    cout << obj.lengthOfLongestSubstring(in) << endl;

    in="murali";    
    cout << obj.lengthOfLongestSubstring(in) << endl;

    return 0;
}

// other solution
/* class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        int si=s.size(), si_substr=0;
        set<int> substr;
        int st=0;
        int res=0;

        for(int en=0; en<si; en++) {

            for(;substr.count(s[en])!=0;) {
                substr.erase(s[st]);
                st++;
            }
            substr.insert(s[en]);
            si_substr = substr.size();
            res = max(res, si_substr);
        }

        return res;
    }
};*/
