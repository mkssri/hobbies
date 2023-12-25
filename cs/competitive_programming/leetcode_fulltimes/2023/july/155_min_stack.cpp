#include <iostream>
#include <vector>

class MinStack {
public:
    
    typedef struct ele {
        int e;
        int min_e;
    } T;

    std::vector<T> vec{};

    MinStack() {
    }
    
    void push(int val) {
        if(vec.empty()) {
            T e1 = {val, val};
            vec.push_back(e1);
            return;
        }
        T e1 = {val, std::min( vec.back().min_e, val) };
        vec.push_back(e1);
    }
    
    void pop() {
        vec.pop_back();
    }
    
    int top() {
        return vec.back().e;
    }
    
    int getMin() {
        return vec.back().min_e;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */


class MinStack {
public:

    multiset<int> minHeap;
    std::stack<int*> st;

    MinStack() {

    }

    void push(int val) {
        int* k = new int(val);
        st.push(k);
        minHeap.insert(*k);
    }

    void pop() {

        int* k = st.top();
        st.pop();
        minHeap.erase(minHeap.find(*k));

    }

    int top() {
        return *(st.top());
    }

    int getMin() {
        return *(minHeap.begin());
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
