class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> res;
        for (int ast : asteroids) {
            if (ast > 0)
                res.push_back(ast);
            else {
                while (!res.empty() && res.back() > 0 && res.back() < -ast)
                    res.pop_back();

                if (res.empty() || res.back() < 0)
                    res.push_back(ast);
                else if (res.back() == -ast)
                    res.pop_back();
            }
        }

        return res;
    }
};