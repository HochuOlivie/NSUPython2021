words = {}
with open("problem2.txt", "r") as f:
    for line in f.readlines():
        word, definition = line.strip().split(" - ")
        for i in definition.split(", "):
            words[i] = word

for k, v in sorted(words.items()):
    print(f"{k} - {v}")
