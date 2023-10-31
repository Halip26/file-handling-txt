# File Handling Operations in Python

This repository contains code that demonstrates different file handling operations in Python.

## Contents

- [File Handling Operations in Python](#file-handling-operations-in-python)
  - [Contents](#contents)
  - [Reading from a File](#reading-from-a-file)
  - [Writing to a File](#writing-to-a-file)
  - [Appending to a File](#appending-to-a-file)
  - [Creating an Empty File](#creating-an-empty-file)

## Reading from a File

To read the contents of a file, you can use the `open()` function with the `'r'` mode. The following code snippet demonstrates reading from a file named "check.txt":

```python
with open("check.txt", "r") as f:
    print(f.read())
```

## Writing to a File

To write content to a file, you can use the open() function with the 'w' mode. The code snippet below shows how to write to a file named "check2.txt":

```python
with open("check2.txt", "w") as f:
    f.write("Sekarang file baru ada. Dengan informasi")
```

## Appending to a File

To append text to an existing file, you can use the open() function with the 'a' mode. The code snippet below demonstrates appending text to a file named "check2.txt":

```python
with open("check2.txt", "a") as f:
    f.write("Now the new file is there. We are appending text in file.")

```

## Creating an Empty File

To create an empty file, you can use the open() function with the 'x' mode. The code snippet below creates an empty file named "myfile.txt":

```python
with open("myfile.txt", "x"):
    pass

```
