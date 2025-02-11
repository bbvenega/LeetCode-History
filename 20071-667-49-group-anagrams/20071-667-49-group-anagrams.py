class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))

            words[sorted_word].append(word)

        ans = []

        # print(f"words is currently {words} \n")

        for word in words:
            ans.append(words[word])

        return ans 