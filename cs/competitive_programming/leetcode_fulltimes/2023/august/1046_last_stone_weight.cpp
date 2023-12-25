#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
    
        priority_queue<int> pq(stones.begin(), stones.end());

        /*for(auto iter=stones.begin(); iter!=stones.end(); iter++) {
            pq.push(*iter);
        }*/

        int x=0, y=0;
        for(;pq.size()>2;) {
            x=pq.top();
            pq.pop();
            y=pq.top();
            pq.pop();

            if(x!=y) {
                pq.push(abs(x-y));
            }
        }

        if(pq.size()==2) {
            x=pq.top();
            pq.pop();
            y=pq.top();
            pq.pop();
            return abs(x-y);
        } else {
            return pq.top();
        }

    }
};
