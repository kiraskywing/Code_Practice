def solution(word):
    diff = 1
    res = []
    
    """
    for c in word:
        cur = ord(c) - diff
        while cur < ord('a'):
            cur += 26
        
        diff += cur
        res.append(chr(cur))

    return ''.join(res)
    """

    res = []
    for i in range(len(word)):
        if i == 0:
            res.append(chr((ord(word[i]) - ord('a') - 1 + 26) % 26 + ord('a')))
        else:
            prev = ord(word[i - 1]) % 26
            cur = ord(word[i]) - ord('a')
            shift = (cur - prev + 26) % 26
            res.append(chr(ord('a') + shift))

    return ''.join(res)

word = "dnotq"
word = "flgxswdliefy"
print(solution(word))

# w[0] = w2[0] + 1  => w2[0] = w[0] - 1
# w[1] = w2[1] + w2[0] => w2[1] = w[1] - w2[0]