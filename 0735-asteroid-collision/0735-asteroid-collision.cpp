class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        

        stack<int> astStack;

        

        for(auto entry: asteroids) {
            

            bool collided = false;

            while(!astStack.empty() && entry < 0 && astStack.top() > 0)  {
                int top = astStack.top();
                if(abs(entry) > top) {
 
                    astStack.pop(); }

                else if(abs(entry) == top) {
                    astStack.pop();
                    collided = true;
                    break;                        
                    }
                   else {
                    collided = true;
                    break;
                   }


            }
            if(!collided) {
            astStack.push(entry);
            }
        }
    vector<int> ans;
    while(!astStack.empty()) {
        ans.push_back(astStack.top());
        cout << "astStack.top() = " << astStack.top() << endl;
        astStack.pop();
    }
    reverse(ans.begin(), ans.end());
    return ans;
    }
};