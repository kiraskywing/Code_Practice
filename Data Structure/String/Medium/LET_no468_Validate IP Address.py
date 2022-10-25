class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        items = queryIP.split('.')
        if len(items) == 4:
            for s in items:
                if not s:
                    return "Neither"
                if s != '0' and s[0] == '0':
                    return "Neither"
                if not s.isdigit():
                    return "Neither"
                if not (0 <= int(s) <= 255):
                    return "Neither"
                
            return "IPv4"
        
        items = queryIP.split(':')
        if len(items) == 8:
            for s in items:
                if not (1 <= len(s) <= 4):
                    return "Neither"
                for c in s:
                    if not ('0' <= c <= '9') and not ('a' <= c.lower() <= 'f'):
                        return "Neither"
            
            return "IPv6"
        
        return "Neither"
            