import re
import csv

def GetWords():
    with open("wordDictionary.txt", "r") as file:
        reader = csv.reader(file)
        words = []
        for row in reader:
            words.extend(row)
        words = tuple(words)
        return words

wordDictionary = GetWords()

cases = ("first", "last")

def main():
    print("What word do you want to find?")
    wordFind = input("Tell me about this word\n==>")
    if cases in wordFind:
        match = re.search(r'letter is (\w)', wordFind)
        if "first" in wordFind:
            wordList = [word for word in wordDictionary if wordFind[0] in word]

if __name__ == "main":
    main()