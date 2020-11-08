class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        folder.sort(key=len)
        temp = set()

        for elem in folder:
            i = 2
            while i < len(elem):
                if elem[i] == "/" and elem[:i] in temp:
                    break
                i += 1
            if i == len(elem):
                temp.add(elem)

        return list(temp)