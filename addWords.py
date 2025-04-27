import requests
import csv

# Define the API endpoint and the number of words you want
url = "https://random-word-api.herokuapp.com/word?number=10"  # This will get 10000 words

# Send the GET request
response = requests.get(url)

if response.status_code == 200:
    words = response.json()
    print(words)
    with open("wordDictionary.txt", mode="w", newline="") as file:
        writer = csv.writer(file)
            
        for word in words:
            writer.writerow([word])
else:
    print("Failed to retrieve data")
