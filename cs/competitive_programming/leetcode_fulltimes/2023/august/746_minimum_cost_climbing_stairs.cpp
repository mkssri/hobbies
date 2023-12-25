#include <iostream>
#include <vector>

using namespace std;

class Solution {

public:
    int minCostClimbingStairs(vector<int>& cost) {

        int si=cost.size();
        cost.push_back(0);
        cost.push_back(0);

        for(int idx=si-1; idx>=0; idx--) 
            cost[idx]=cost[idx]+min(cost[idx+1], cost[idx+2]);
        
        return min(cost[0], cost[1]);

    }
};
