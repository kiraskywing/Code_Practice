class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> nextCourses(numCourses);
        vector<int> preTimes(numCourses, 0);
        for (vector<int>& e : prerequisites) {
            nextCourses[e[1]].push_back(e[0]);
            preTimes[e[0]]++;
        }
            
        
        vector<int> res;
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (preTimes[i] == 0)
                q.push(i);
        }
        
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            res.push_back(cur);
            
            for (int i : nextCourses[cur]) {
                preTimes[i]--;
                if (preTimes[i] == 0)
                    q.push(i);
            }
        }
        
        if (res.size() == numCourses)
            return res;
        
        return {};
    }
};