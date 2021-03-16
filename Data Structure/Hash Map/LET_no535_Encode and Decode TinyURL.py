class Codec:
    def __init__(self):
        self.alnum = "abcdefghijklmnopqrstuvwxyz0123456789"
        self.urlToCode = {}
        self.codeToUrl = {}
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.urlToCode:
            code = ''.join(random.choice(self.alnum) for _ in range(6))
            if code not in self.codeToUrl:
                self.urlToCode[longUrl] = code
                self.codeToUrl[code] = longUrl
        return "http://tinyurl.com/" + self.urlToCode[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.codeToUrl[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))