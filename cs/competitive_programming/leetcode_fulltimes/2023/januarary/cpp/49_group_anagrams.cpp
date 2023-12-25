class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        map<vector<int>, vector<string>> store;

        for(auto x: strs){
            vector<int> v(26,0);
            for(auto ch: x){
                v[ch-'a']++;
            }
            store[v].push_back(x);
        }

        vector<vector<string>> res;

        for(auto x: store){
            res.push_back(x.second);
        }

        return res;
    }
};


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, int> map;
        std::vector<vector<string>> res;

        for (const auto &s: strs) {
            std::string sorted = s;
            std::sort(sorted.begin(), sorted.end());

            if (map.count(sorted)) {
                res[map[sorted]].push_back(s);
            } else {
                res.push_back({s});
                map[sorted] = res.size() - 1;
            }
        }

        return res;
    }
};


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        vector<vector<string>> res;
        map<string, int> idx_finder;

        for(auto &x: strs){
            string tmp=x;
            sort(tmp.begin(), tmp.end());

            if(idx_finder.count(tmp)){
                res[idx_finder[tmp]].push_back(x);
            } else {
                res.push_back({x});
                idx_finder[tmp]=res.size()-1;
            }

        }

        return res;
        
    }
};

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        map<string, vector<string>> store;
        vector<vector<string>> res;


        for(auto &x: strs){
            string tmp = x;
            sort(x.begin(), x.end());
            store[x].push_back(tmp);
        }

        for(auto it=store.begin(); it!=store.end(); it++){
            res.push_back(it->second);
        }

        return res;


    }
};