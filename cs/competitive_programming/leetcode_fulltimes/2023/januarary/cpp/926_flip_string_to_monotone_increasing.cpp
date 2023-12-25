#include <stdio.h>
using namespace std;
#include <string>

class Solution {
public:
    int minFlipsMonoIncr(string s) {
        int flips = 0;
        int ones = 0;

        for(auto x: s){
            if(x=='0'){
                flips += 1;
            }
            else{
                ones += 1;
            }

            flips = min(flips, ones);
        }
        return flips;
    }
};