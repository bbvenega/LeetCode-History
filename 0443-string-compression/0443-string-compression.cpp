class Solution {
public:
    int compress(vector<char>& chars) {
        string s;
        auto temp = chars[0];
        int counter = 0;

        for(int i = 0; i < chars.size(); i++) {
             if (i == chars.size()-1){
                if(chars[i] == temp) {
                counter++;
                s += temp;
                if(counter > 1) {
                    
                    s += std::to_string(counter);
                }
                } else {
                    s+= temp;
                    if(counter > 1) {
                        s+= std::to_string(counter);
                    }
                    s+= chars[i];
                }

            } else if(chars[i] == temp ) {
                counter++;
                cout << "Counter: " << counter << endl;
            }
            
            else {
                 s += temp;
                if(counter > 1) {
                    cout << "Counter: " << counter << endl;
                    s += std::to_string(counter);
                }
                temp = chars[i];
                counter = 1;
            }
        }

        chars.clear();
        for(int i = 0; i < s.length(); i++) {
            chars.push_back(s[i]);
        }

        return chars.size();
    }
};