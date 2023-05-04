class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> qr, qd;
        int n = senate.size();
        for (int i = 0; i < n; i++) {
            if (senate[i] == 'R')
                qr.push(i);
            else
                qd.push(i);
        }

        while (!qr.empty() && !qd.empty()) {
            int r = qr.front(), d = qd.front();
            qr.pop(), qd.pop();
            if (r < d)
                qr.push(r + n);
            else
                qd.push(d + n);
        }

        return !qr.empty() ? "Radiant" : "Dire";

    }
};