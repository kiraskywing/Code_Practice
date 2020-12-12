class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []

        for i in range(1, len(searchWord) + 1):
            temp = []
            for word in products:
                if word.startswith(searchWord[:i]):
                    temp.append(word)
                if len(temp) == 3:
                    break
            result.append(temp)

        return result