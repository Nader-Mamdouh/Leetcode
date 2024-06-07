class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        st = sentence.split(" ")
        from collections import defaultdict
        di = defaultdict(list)
        for word in dictionary:
            di[word[0]].append(word)

        for key in di:
            di[key].sort(key=len)
        for i in range(len(st)):
            for root in di[st[i][0]]:
                if st[i].startswith(root):
                    st[i] = root
                    break

        return " ".join(st)
