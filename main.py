import re
import csv
from typing import List

wordList = []
multiQueryList = []

def GetWords() -> tuple:
    with open("wordDictionary.txt", "r") as file:
        reader = csv.reader(file)
        words = []
        for row in reader:
            words.extend(row)
        words = tuple(words)
        return words

wordDictionary = GetWords()

def printWords(wordList: List[str], boolLimit: int) -> None:
    if boolLimit != 1:
        limitingNumber = len(wordList) // 193 + 3
    else:
        limitingNumber = (len(wordList) ** (1/5) + 2) // 1
    if len(wordList) == 1:
        print(f"The word you are finding is \"{wordList}\"")
    elif len(wordList) > 1:
        for i, word in enumerate(wordList):
            print(f"{i+1}. {word}")
            if i > limitingNumber:
                break
    else:
        print("Sorry, I couldn't find the word you described.\nPlease give me query in detail.")

def solveQuery(letterQuery, pos):
    if pos != ":":
        findingWords = [word for word in wordDictionary if len(word) > pos and letterQuery == word[pos]]
        wordList.extend(findingWords)
    
    else:
        findingWords = [word for word in wordDictionary if letterQuery in word]
        wordList.extend(findingWords)

def extraQuery(letterQuery, pos):
    if pos != ":":
        findingWords = [word for word in wordList if len(word) > pos and letterQuery == word[pos]]
        multiQueryList.extend(findingWords)
        
    else:
        findingWords = [word for word in wordDictionary if letterQuery in word]
        multiQueryList.extend(findingWords)


def main() -> None:
    letter_dict = {}
    isFirstQuery = True
    print("What word do you want to find?")
    wordFind = input("Tell me about this word\n==> ").lower()
    matches = re.findall(r'(?P<position>\w+)\s+(?:letter|word)\s+(?:is|which has|has)\s+(?P<letter_or_length>\w|\d+)', wordFind)
    
    for match in matches:
        position, letter = match
        letter_dict[position] = letter

    for letter_position, letterQuery in letter_dict.items():
        if isFirstQuery:
            if not letterQuery.isdigit():
                if letter_position == "first":
                    solveQuery(letterQuery, 0)

                elif letter_position == "second":
                    solveQuery(letterQuery, 1)

                elif letter_position == "third":
                    solveQuery(letterQuery, 2)

                elif letter_position == "fourth":
                    solveQuery(letterQuery, 3)

                elif letter_position == "fifth":
                    solveQuery(letterQuery, 4)

                elif letter_position == "sixth":
                    solveQuery(letterQuery, 5)

                elif letter_position == "seventh":
                    solveQuery(letterQuery, 6)

                elif letter_position == "eighth":
                    solveQuery(letterQuery, 7)

                else:
                    solveQuery(letterQuery, ":")
            
            else:
                findingWords = [word for word in wordDictionary if len(word) == int(letterQuery)]
                wordList.extend(findingWords)
            
            isFirstQuery = False
        
        else:
            if not letterQuery.isdigit():
                if letter_position == "first":
                    extraQuery(letterQuery, 0)

                elif letter_position == "second":
                    extraQuery(letterQuery, 1)

                elif letter_position == "third":
                    extraQuery(letterQuery, 2)

                elif letter_position == "fourth":
                    extraQuery(letterQuery, 3)

                elif letter_position == "fifth":
                    extraQuery(letterQuery, 4)

                elif letter_position == "sixth":
                    extraQuery(letterQuery, 5)

                elif letter_position == "seventh":
                    extraQuery(letterQuery, 6)

                elif letter_position == "eighth":
                    extraQuery(letterQuery, 7)

                else:
                    extraQuery(letterQuery, ":")
            
            else:
                findingWords = [word for word in wordList if len(word) == int(letterQuery)]
                multiQueryList = findingWords

    if len(letter_dict) > 1:
        printWords(multiQueryList, 0)
    else:
        printWords(wordList, 1)

if __name__ == "__main__":
    main()