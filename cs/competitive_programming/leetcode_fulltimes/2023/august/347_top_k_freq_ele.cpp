#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        unordered_map<int, int> freq = {};

        for(int i: nums) {
            freq[i] += 1;
        }

        // By default pq is Max Heap
        priority_queue< pair<int, int>, vector< pair<int, int> > > pq = {};

        for(auto iter=freq.begin(); iter!=freq.end(); iter++) {
            pq.push({iter->second, iter->first});
        }

        vector<int> res = {};

        for(;k>0;k--) {
            res.push_back(pq.top().second);
            pq.pop();
        }

        return res;
    }
};

int main() {

   vector<int> in_arr = {};
   in_arr.push_back(1);
   in_arr.push_back(1);
   in_arr.push_back(1);
   in_arr.push_back(2);
   in_arr.push_back(2);
   in_arr.push_back(3);

    Solution obj;
    vector<int> res = {};

    res = obj.topKFrequent(in_arr,2);

    for(int t: res)
        cout << t << ' ';

    cout << endl;
    return 0;
}
/*
 * compilation:
 - g++ 347_top_k_freq_ele.cpp -o 347 -std=c++11
 - ./347
 */
