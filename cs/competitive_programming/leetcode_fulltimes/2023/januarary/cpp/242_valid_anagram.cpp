#include <iostream>
#include <algorithm>
#include <map>

using namesapce std;

class Solution {
public:
    bool isAnagram(string s, string t) {

        if(s.size() != t.size())
        return false;

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        return s==t;
        
    }
};


class Solution {
public:
    bool isAnagram(string s, string t) {

        if(s.size() != t.size())
        return false;

        map <char, int> m1, m2;
        m1 = helper(s);
        m2 = helper(t);

        return m1==m2;

    }

    map<char, int> helper(string s){
        map<char, int> d1;
        for(int i=0; i<s.size(); i++){
            d1[s[i]] += 1;
        }
        return d1;
    }

};