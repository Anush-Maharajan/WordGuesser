import requests
import csv

# Define the API endpoint and the number of words you want
url = "https://random-word-api.herokuapp.com/word?number=100000"  # This will get 100000 words

# Send the GET request
response = requests.get(url)

if response.status_code == 200:
    words = response.json()
    with open("wordDictionary.txt", mode="a", newline="") as file:
        writer = csv.writer(file)

        for word in words:
            writer.writerow([word])
else:
    print("Failed to retrieve data")
