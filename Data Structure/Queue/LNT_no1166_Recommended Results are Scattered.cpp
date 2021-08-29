class Solution {
public:
    /**
     * @param elements: A list of recommended elements.
     * @param n: [picture P] can appear at most 1 in every n
     * @return: Return the scattered result.
     */
    vector<string> scatter(vector<string> &elements, int n) {
        // write your code here
        vector<string> res;
        int i = 0, size = elements.size();

        while (elements[i][0] != 'P') {
            res.push_back(elements[i]);
            i++;
        }

        queue<string> p, v;
        while (i < size) {
            if (elements[i][0] == 'P')
                p.push(elements[i]);
            else
                v.push(elements[i]);
            i++;
        }

        for (int j = 0;; j++) {
            string cur;
            if (j % n == 0 && !p.empty()) {
                cur = p.front();
                p.pop();
                res.push_back(cur);
            }
            else if (j % n != 0 && !v.empty()) {
                cur = v.front();
                v.pop();
                res.push_back(cur);
            }
            else
                break;
        }

        return res;
    }
};