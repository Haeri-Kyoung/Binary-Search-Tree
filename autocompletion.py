"""
file: autocompletion.py
Author: Haeri Kyoung (hxk9280@rit.edu)
Description: Python code of implementing a prefix searching system.
"""
def main():
    """Calling either BinarySearch or linearSearch to search the word that starts with the prefix"""
    i = input("filename")
    f = open(i)
    e = []
    for line in f:
        e.append(line.strip())
    print(e)
    i = input("Please enter the type of search to use [binary / linear]: ")
    while True:
        prefix = input("Please enter a prefix to search for: ")
        if prefix == '':
            print("Good bye!")
            return
        if i == "binary":
            result = binarySearch(e, prefix, 0, len(e)-1)
            print(result)
        elif i == "linear":
            word = linearSearch(e, prefix)
            print(word)

def binarySearch(e, prefix, start, end):
    """Search for the word it finds in the list that has that prefix firstly with linear search"""
    if start > end:
        return None
    mid_index = (start + end) // 2
    mid_value = e[mid_index]
    if prefix == mid_value[0:len(prefix)]:
        return mid_value
    elif prefix < mid_value:
        return binarySearch(e, prefix, start, mid_index-1)
    else:
        return binarySearch(e, prefix, mid_index+1, end)

def linearSearch(e, prefix):
    """Search for the word it finds in the list that has that prefix firstly with binary search"""
    for word in e:
        if prefix == word[0:len(prefix)]:
            return word
    return None

main()