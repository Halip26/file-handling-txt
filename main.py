def opening_function():
    f = open("penjaga-hati.txt", "r")
    data = f.read()
    print(data)
    f.close()


opening_function()


def characters_function():
    f = open("penjaga-hati.txt", "r")
    data = f.read()
    c = len(data)  # It calculates the number of letters.
    print("the total number of letters is: ", c)
    f.close()


characters_function()


def word_function():
    f = open("penjaga-hati.txt", "r")
    data = f.read()
    cnt = 0
    w = data.split()  # This splits the each word by space b/w each word.
    for ch in w:
        cnt += 1  # It will count all words
    f.close()
    print("No. of words in file", cnt)


word_function()


def lowerletter_function():
    f = open("penjaga-hati.txt", "r")
    data = f.read()
    count = 0
    for i in data:
        # is lower checks the letter if it is small
        if i.islower():
            count += 1

    f.close()
    print("No. of lower case letters in file : ", count)


lowerletter_function()


def upperletter_function():
    f = open("penjaga-hati.txt", "r")
    data = f.read()
    count = 0
    for i in data:
        # letter we can also use upper to calculate capital letters.
        if i.upper():
            count += 1
    f.close()
    print("No. of upper case letters in file : ", count)


upperletter_function()


def Slines_function():
    f = open("penjaga-hati.txt", "r")
    data = f.read()  # u can use readlines() for cek line starts with s
    count = 0
    for lines in data:
        if lines[0] == "s":
            count += 1
    f.close()
    print("No. of lines starting with 's' is : ", count)


Slines_function()


def find_words_function():
    f = open("penjaga-hati.txt", "r")
    data = f.read()
    count = 0
    ws = input("Enter word to find: ")
    word = data.split()
    # looping for find lower words
    for w in word:
        if ws.lower() in w.lower():
            count += 1
    f.close()
    print(ws, "found", count, "times in the file.")


find_words_function()
