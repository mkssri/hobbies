class Solution {
public:
    bool isValid(string s) {

        std::unordered_map<char, char> book = {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };
        
        std::stack<char> st;

        int si = s.size();
        char e;

        for(int idx=0; idx<si; idx++){
            e = s[idx];
            if(book.count(e)>0) {
                st.push(e);
            } else if( (st.size()!=0) && ( e == book[st.top()] ) ) {
                st.pop();
            } else {
                return false;
            }

        }

        return (st.size()==0);

    }
};

// Following solutuion is cool! we do not use dictionary here
class Solution {
public:

    char getComplimentary(char i) {

        switch(i) {
            case '}':
                return '{';
            case ')':
                return '(';
            case ']':
                return '[';
        }

        return '\0';
    }

    bool isValid(string s) {

        std::stack<char> st;
        char e;

        for(int i=0; i<s.size(); i++) {
            e=s[i];
            if( e=='{' || e=='(' || e=='[' ) {
                st.push(s[i]);
            } else {
                if(!st.empty() && st.top()==getComplimentary(e)){
                    st.pop();
                } else {
                    return false;
                }
            }
        }

        return st.empty();
    }
};
