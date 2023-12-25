#!/usr/bin/python3

# Link - https://leetcode.com/problems/shortest-word-distance/

from typing import List

import math

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        word1_lst, word2_lst = [], []
        
        for x in range(0, len(wordsDict)):
            
            if wordsDict[x] == word1:
                word1_lst.append(x)
            
            if wordsDict[x] == word2:
                word2_lst.append(x)

        
        print(word1_lst, word2_lst)
        
        
        min_diff = math.inf
        
        
        for x in word1_lst:
            for y in word2_lst:
                
                temp_diff = abs(y-x)
                min_diff = min(min_diff, temp_diff)
        
        return min_diff
            
# One pass Solution


import math

class Solution1:
    def shortestDistance1(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        i1, i2 = -1, -1
        min_distance = len(wordsDict)
        
        for i in range(min_distance):
            
            if wordsDict[i] == word1:
                i1 = i
            elif wordsDict[i] == word2:
                i2 = i
            
            if i1 != -1 and i2 != -1:
                min_distance = min(min_distance, abs(i1-i2))
        
        return min_distance