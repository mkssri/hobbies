#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class KthLargest {
public:
    
    int k=0;
    priority_queue<int> pqH = {};
    priority_queue<int> pqL = {};

    KthLargest(int k, vector<int>& nums) {
        this->k=k;
        for(auto iter=nums.begin(); iter!=nums.end(); iter++)
        this->pqL.push(*iter);
    }
    
    int add(int val) {
    
        int temp = 0;
        if( pqH.size() < this->k ) {
            this->pqL.push(val);

            //Build pqH & update pqL
            // both are max heap's
            for(int idx=0;idx<this->k;idx++) {
                temp = pqL.top();
                this->pqL.pop();
                this->pqH.push(-1*temp);
            }

        } else {
            int h=-1*this->pqH.top();
            if(val>h) {
                this->pqH.pop();
                this->pqH.push(-1*val);
                this->pqL.push(h); 
            } else {
                this->pqL.push(val);
            }
        }

        return -1*this->pqH.top();
    }
};
