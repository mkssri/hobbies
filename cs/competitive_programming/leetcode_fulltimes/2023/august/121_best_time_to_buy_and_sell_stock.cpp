#include <iostream>
#include <vector>

using namespace std;

class Solution {

public:
    int maxProfit(vector<int>& prices) {
        
        int profit=0, idx=0, si=prices.size();
        int buy=prices[0], sell=prices[0];
       
        if(si>1) {
            for(;idx<si;idx++) {
                buy = std::min(buy, prices[idx]);
                profit = std::max(profit, prices[idx]-buy);
            }
        }
        return profit;
    }
};

// Bruteforce
class Solution1 {

public:
    int maxProfit(vector<int>& prices) {
        
        int profit=0, si=prices.size();
       
        for(int i=0; i<si; i++) {
            for(int j=i+1; j<si; j++) {
                profit = std::max(profit, prices[j]-prices[i]);
            }
        }
        return profit;
    }
};
