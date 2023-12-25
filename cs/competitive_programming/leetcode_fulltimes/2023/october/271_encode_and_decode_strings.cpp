#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Codec {
public:

    // Encode
    string encode(vector<string>& strs) {
        string encoded;
        for(string &s:strs)
        encoded += to_string(s.size())+'.'+s;

        return encoded;
    }

    // Decode
    vector<string> decode(string s) {
        vector<string> decoded;

        for(int i=0,n=0; i<s.size(); i+=n,n=0) {
            
            for(;isdigit(s[i]);)
            n = 10*n + s[i++]-'0';

            decoded.push_back(s.substr(++i,n));
        }

        return decoded;
    }
};

int
main() {

 vector<string> in = {"rest", " at", " the", " end,", " not", " in",  " the", " middle."};
 Codec codec = Codec();

 string encoded         = codec.encode(in);
 vector<string> decoded = codec.decode(encoded);

 cout << "decoded string: " << endl;
 for(string &s: decoded) {
     cout << s;
 }

 cout << endl;

 return 0;
}
