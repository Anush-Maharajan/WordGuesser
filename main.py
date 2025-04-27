import re
import csv
from typing import List

def GetWords() -> tuple:
    with open("wordDictionary.txt", "r") as file:
        reader = csv.reader(file)
        words = []
        for row in reader:
            words.extend(row)
        words = tuple(words)
        return words

wordDictionary = GetWords()

def printWords(wordList: List[int]) -> None:
    if len(wordList) == 1:
        print(wordList)
    elif len(wordList) > 1:
        for i, word in enumerate(wordList):
            print(f"{i+1}. {word}")
    else:
        print("Sorry, I couldn't find the word you described.")

cases = ["first", "last"]

def main() -> None:
    print("What word do you want to find?")
    wordFind = input("Tell me about this word\n==>").lower()
    match = re.search(r'.*letter.*is\s*(\w)', wordFind)
    if "first" in wordFind:
        wordList = [word for word in wordDictionary if match.group(1) in word]
        printWords(wordList)

if __name__ == "__main__":
    main()