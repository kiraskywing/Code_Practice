class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> record;
        for (auto& email : emails) {
            string cur;
            for (char c : email) {
                if (c == '.') 
                    continue;
                if (c == '+' || c == '@')
                    break;
                cur += c;
            }
            cur += email.substr(email.find('@'));
            record.insert(cur);
        }
        return record.size();
    }
};