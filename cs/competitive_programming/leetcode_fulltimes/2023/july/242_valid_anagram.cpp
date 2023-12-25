class Solution {
public:
    bool isAnagram(string s, string t) {
        
        int arr[26] = {0};

        int s1 = s.size();
        int s2 = t.size();
        int idx = 0;


        for(char c: s) {
            idx = (int)c - 'a';
            arr[idx] += 1;
        }

        for(char c: t) {
            idx = (int)c - 'a';
            arr[idx] -= 1;
        }


        for(int e: arr) {
            if(e!=0){
                return false;
            }
        }

        return true;

    }
};
