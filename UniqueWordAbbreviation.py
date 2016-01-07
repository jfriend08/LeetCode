'''
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
'''

class ValidWordAbbr(object):
  def __init__(self, dictionary):
    """
    initialize your data structure here.
    :type dictionary: List[str]
    """
    self.dict = self.transform(dictionary)

  def transform(self, dictionary):
    mydict = {}
    for elm in dictionary:
      if len(elm) > 2:
        word = elm[0] + str(len(elm)-2) + elm[-1]
      else:
        word = elm
      try:
        mydict[word].add(elm)
      except:
        mydict[word] = set([elm])
    return mydict

  def isUnique(self, word):
    """
    check if a word is unique.
    :type word: str
    :rtype: bool
    """
    if len(word) > 2:
      query = word[0] + str(len(word)-2) + word[-1]
    else:
      query = word
    return not query in self.dict or self.dict[query] == set([word])

arr = ["deer", "door", "cake", "card"]
sol = ValidWordAbbr(arr)
print sol.isUnique("dear")
print sol.isUnique("door")
print sol.isUnique("cart")
print sol.isUnique("cake")


# arr = ["a", "a"]
# sol = ValidWordAbbr(arr)
# print sol.isUnique("a")

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")