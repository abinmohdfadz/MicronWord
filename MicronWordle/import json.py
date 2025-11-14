import json

# Read the words from the text file
with open("validWords.txt", "r", encoding="utf-8") as txt_file:
    words = [line.strip() for line in txt_file if line.strip()]

# Save the words as a JSON array
with open("validWords.json", "w", encoding="utf-8") as json_file:
    json.dump(words, json_file, indent=2)

print("Conversion complete. File saved as validWords.json")
