import sys
import string


n = len(sys.argv)
if n != 2:
    print("Filename not provided.")
    print("Usage: python3 customCounter.py <file>")
else:
    characters = {char: 0 for char in list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(" `~!@#$%^&*()_+-=[]		{}\|;'\".>,</?")}
    # characters = string.lowercase + string.uppercase + string.digits
    # print(characters.keys())
    try:
        with open(sys.argv[1], 'r') as f:
                for line in f:
                    for char in line:
                        if char in characters:
                            characters[char] += 1

        for char, count in characters.items():
            if count != 0:
                print(f"{char}: {count}")
    except FileNotFoundError as error:
        print("Filename not provided.")
        print("Usage: python3 customCounter.py <file>")