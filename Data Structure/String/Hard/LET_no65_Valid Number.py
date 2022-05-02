class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {"sign":1, "digit":2, ".":3}, #0 initial state
            {"digit":2, ".":3},           #1 found sign (expect digit/dot)
            {"digit":2, ".":4, "e":5},    #2 digit consumer (loop until non-digit)
            {"digit":4},                  #3 found dot (only a digit is valid)
            {"digit":4, "e":5},           #4 after dot (expect digits and e)
            {"sign":6, "digit":7},        #5 found 'e' (only a sign or digit valid)
            {"digit":7},                  #6 sign after 'e' (only digit)
            {"digit":7}                   #7 digit after 'e' (expect digits) 
        ]
        
        cur_state = 0
        for c in s:
            if c in "0123456789": c = "digit"
            elif c in '+-': c = "sign"
                
            if c.lower() not in states[cur_state]:
                return False
            cur_state = states[cur_state][c.lower()]
        
        return cur_state in [2, 4, 7]