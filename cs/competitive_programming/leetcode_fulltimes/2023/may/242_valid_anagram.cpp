class Solution {
public:
    bool isAnagram(string s, string t) {

        std::map<char, int> mydict;
        std::string::iterator it1;

        char ch;
        for(it1= s.begin(); it1!=s.end(); it1++) {
            ch = *it1;
            if(mydict.count(ch)!=0) {
                mydict[ch]+=1;
            } else {
                mydict[ch]=1;
            }
        }
        for(it1= t.begin(); it1!=t.end(); it1++) {
            ch = *it1;
            if(mydict.count(ch)!=0) {
                mydict[ch]-=1;
            } else {
                mydict[ch]=-1;
            }
        }

        for(auto& pair: mydict){
            if(pair.second!=0){
                return false;
            }
        }
        return true;
    }
};
