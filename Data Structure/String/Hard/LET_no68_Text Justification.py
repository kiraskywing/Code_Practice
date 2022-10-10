class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        chars = 0
        left = right = 0
        
        while right < len(words):
            if chars + len(words[right]) + right - left > maxWidth:
                if right - left == 1:
                    res.append(words[left] + ' ' * (maxWidth - chars))
                else:
                    counts = right - left - 1
                    spaces = ' ' * ((maxWidth - chars) // counts)
                    remain = ((maxWidth - chars) % counts)
                    temp = []
                    for i in range(remain):
                        temp.append(words[left + i] + spaces + ' ')
                    for i in range(left + remain, right - 1):
                        temp.append(words[i] + spaces)
                    res.append(''.join(temp) + words[right - 1])
                
                chars, left = 0, right
            
            chars += len(words[right])
            right += 1
        
        res.append(' '.join(words[i] for i in range(left, right)) + ' ' * (maxWidth - chars - (right - left - 1)))
        
        return res