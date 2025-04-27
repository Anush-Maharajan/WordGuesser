import csv

words = set()

def cleanWords():
    with open("wordDictionary.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            words.update(row)
        print("Cleaned")

    with open("wordDictionary.txt", mode="w",newline="") as file:
        writer = csv.writer(file)
        for word in words:
            writer.writerow([word])
        print("Done")

cleanWords()
