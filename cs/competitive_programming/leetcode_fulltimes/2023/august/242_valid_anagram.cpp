class Solution {
public:
    bool isAnagram(string s, string t) {

        std::array<int, 26> res = {0}; // = {}

        for(auto it=s.begin(); it!=s.end(); ++it) {
            res[*it-'a'] += 1; 
        }
        for(auto it=t.begin(); it!=t.end(); ++it) {
            res[*it-'a'] -= 1; 
        }
        for(int idx=0; idx<26; ++idx) {
            if(res[idx]!=0)
                return false;
        }
        return true;

    }
};
