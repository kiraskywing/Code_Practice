class Solution:
    def interpret(self, command: str) -> str:
        res = []
        for i in range(len(command)):
            if command[i].isalpha():
                res.append(command[i])
            if command[i] == ')' and command[i - 1] == '(':
                res.append('o')
        
        return ''.join(res)