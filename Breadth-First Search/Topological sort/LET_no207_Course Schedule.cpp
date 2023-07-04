class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegree(numCourses, 0);
        unordered_map<int, vector<int>> next_course;
        for (auto& item : prerequisites) {
            indegree[item[0]]++;
            next_course[item[1]].push_back(item[0]);
        }

        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0)
                q.push(i);
        }

        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            numCourses--;

            for (int nxt : next_course[cur]) {
                if (--indegree[nxt] == 0)
                    q.push(nxt);
            }
        }

        return numCourses == 0;
    }
};