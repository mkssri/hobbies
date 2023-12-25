class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        map<int, int> m;

        for(auto &i: nums){
            m[i]++;
        }
        vector<int> res;
        // pair<first, second>: first is frequency,  second is number
        priority_queue<pair<int,int>> pq; 
        for(auto it = m.begin(); it != m.end(); it++){
            pq.push(make_pair(it->second, it->first));
            if(pq.size() > (int)m.size() - k){
                res.push_back(pq.top().second);
                pq.pop();
            }
        }
        return res;

    }

};