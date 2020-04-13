# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.



def word_ladder(beginWord, endWord, wordList):
    from collections import defaultdict
    def valid(s1, s2):
        diff_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_count += 1
        return diff_count == 1
    # Find the index of the endWord in wordList
    end_index = -1
    for i in range(len(wordList)):
        if wordList[i] == endWord:
            end_index = i
    if end_index == -1:
        return 0

    start = len(wordList)
    wordList.append(beginWord)

    transforms = defaultdict(list)
    # transform into a graph adjacency list representation
    for i in range(len(wordList)-1):
        for j in range(i+1, len(wordList)):
            if valid(wordList[i], wordList[j]):
                transforms[i].append(j)
                transforms[j].append(i)
    # find if there is a valid path from end_index node to len(wordList)-1 node
    print(transforms)

    distances = [float('inf')] * len(wordList)
    parents = [None for _ in range(len(wordList))]
    distances[start] = 1
    print("start:", start, "end:", end_index)
    visited = [False] * len(wordList)
    for i in range(len(wordList)):
        u = -1
        min_distance = float('inf')
        for j in range(len(distances)):
            if not visited[j]:
                if distances[j] < min_distance:
                    min_distance = distances[j]
                    u = j
        visited[u] = True
        for v in transforms[u]:
            if not visited[v]:
                if distances[u] + 1 < distances[v]:
                    distances[v] = distances[u] + 1
                    parents[v] = u

    print(distances)
    print(parents)
    i = end_index
    while parents[i] is not None:
        print(wordList[i], end=" ")
        i = parents[i]
    print(wordList[start])
    return distances[end_index] if distances[end_index] != float('inf') else 0



def word_ladder_preprocess(beginWord, endWord, wordList):
    from collections import defaultdict, deque
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0
    L = len(beginWord)
    d = defaultdict(list)
    for word in wordList:
        for i in range(L):
            d[word[:i] + "*" + word[i+1:]].append(word)
    print(d)
    q = deque([(beginWord, 1)])
    visited = {beginWord: True}
    while q:
        current, dist = q.popleft()
        for i in range(L):
            intermediate_word = current[:i] + "*" + current[i+1:]
            for word in d[intermediate_word]:
                if word == endWord:
                    return dist + 1
                if word not in visited:
                    visited[word] = True
                    q.append((word, dist + 1))
            d[intermediate_word] = []
    return 0


print(word_ladder_preprocess("hot","cog",["hot","hog","cog"]))