#include <vector>
#include <iostream>

using namespace std;


void helper(vector<int> & vec) {

    for(auto iter=vec.begin(); iter!=vec.end(); iter++) {
        cout << *iter << endl;
    }
}

int main() {

    vector<int> vec = {1,2,3,4,6};
    helper(vec);
    cout<< "max size of vec: " << vec.max_size() << endl;

    cout << endl;

    auto it = vec.begin();
    vec.insert(it, 2);
    helper(vec);
    cout<< "max size of vec: " << vec.max_size() << endl;


    return 0;
}
