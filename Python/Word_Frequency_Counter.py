value = input("Enter a string: ").lower()

used_words = []
words = value.split()

for i in words:
    if i not in used_words:
        used_words.append(i)
        print(f"{i} : {words.count(i)}")

print(f"Total words: {len(words)}")
print(f"Unique words: {len(used_words)}")