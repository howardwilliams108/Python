from hashlib import sha256


def find_groups(filename):
    groups = {}  # I use groups to initialize the empty dictionary.
    lines = [line.strip() for line in open(filename, "r", encoding="utf-8") if line.strip()]
    for word in sorted(set(lines)):  #using my previous experiences in python, I use sorted to sort fruits alphabetically and use sets to remove duplicates
        data = word.encode()                     # analogous to file bytes
        hash_code = sha256(data).hexdigest()
        integer = int(hash_code, 16)
        groups[word] = (hash_code, integer) # these are the items store in groups
    return groups

if __name__ == "__main__":
    groups = find_groups("wordcount.txt")
    for word in sorted(groups):
        hexdigest, integer = groups[word]
        print(f"The word is: {word}")
        print(f" The hex digest is {hexdigest} ")
        print(f"The integers are {integer} ")
        print()

