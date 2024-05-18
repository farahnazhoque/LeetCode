"""
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""
from collections import defaultdict
def groupAnagrams(strs):
    result = defaultdict(list) # creating a dictionary with default value as list
    
    for word in strs: # iterating over the words in the list, strs
        sorted_word = ''.join(sorted(word)) # turning the word, eg: 'bat', to 'abt' to serve as key for the result dictionary
        result[sorted_word].append(word) # appending the word to the list of values if the sorted version of the word matches the key
        
    return list(result.values()) # returning the values of the dictionary as a list