class Solution {
public:
    bool isPalindrome(string s) {
        
        string result;

        for( char c : s ) {
            if(std::isalnum(c)) {
                result += std::tolower(c);
            }
        }

        int l = 0, r = result.length()-1;

        while(l<=r){
            if(result[l]!=result[r]) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};
