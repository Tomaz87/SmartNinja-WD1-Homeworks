# Title: Mood checker

mood = input("Hi! How are you feeling today? ").lower()

# Eliminating accidentally inserted spaces in the mood variable.
x = mood.strip(" ")

if x == "happy":
    print("It is great to see you happy!")
elif x == "nervous":
    print("Take a deep breath 3 times.")
elif x == "sad":
    print("It could always be even sadder, so cheer up mate!")
elif x == "exited":
    print("Yeah! Let's do it!")
elif x == "relaxed":
    print("Well, that is very nice.")
else:
    print("I don't recognize this mood.")
