from collections import defaultdict
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        wordLen = len(start)
        front, back = defaultdict(list), defaultdict(list)
        front[start].append([start])
        back[end].append([end])
        # remove start from dict, add end to dict if it is not there
        dict.discard(start)
        if end not in dict:
            dict.add(end)
        forward, result = True, []
        while front:
            # get all valid transformations
            nextSet = defaultdict(list)
            for word, paths in front.items():
                for index in range(wordLen):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = word[:index] + ch + word[index+1:]
                        if nextWord in dict:
                            # update paths
                            if forward:
                                # append next word to path
                                nextSet[nextWord].extend([path + [nextWord] for path in paths])
                            else:
                                # add next word in front of path
                                nextSet[nextWord].extend([[nextWord] + path for path in paths])
            front = nextSet
            common = set(front) & set(back)

            print "front:", front, "back:", back, "forward:", forward, common, dict
            print '--------------'

            if common:
                # path is through
                if not forward:
                    # switch front and back if we were searching backward
                    front, back = back, front
                result.extend([head + tail[1:] for word in common for head in front[word] for tail in back[word]])
                return result

            if len(front) > len(back):
                # swap front and back for better performance (smaller nextSet)
                front, back, forward = back, front, not forward

            # remove transformations from wordDict to avoid cycles
            dict -= set(front)

        return []

beginWord = "red"
endWord = "tax"
wordList = set(["ted","tex","red","tax","tad","den","rex","pee"])

sol = Solution()
print sol.findLadders(beginWord, endWord, wordList)






