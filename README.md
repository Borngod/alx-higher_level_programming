<h1>alx-higher_level_programming</h1>

# 0x00. Python - Hello, World

- By Guillaume

## [](https://github.com/Pericles001/alx-higher_level_programming/tree/main/0x00-python-hello_world#concepts)Concepts

_For this project, students are expected to look at these concepts:_

- [Python programming](https://alx-intranet.hbtn.io/concepts/63)
- [Python programming](https://alx-intranet.hbtn.io/concepts/550)
- [Python programming](https://alx-intranet.hbtn.io/concepts/551)

![https://camo.githubusercontent.com/7da0256fce917a5d77c370a545dda177a38dd018c5a9641d576b1b2ebdd9a40c/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3233312f343861396664626436376338346133323861396466396563386439336239616332343538616333373732316437643533653531613237666232626463353236332e6a7067](https://camo.githubusercontent.com/7da0256fce917a5d77c370a545dda177a38dd018c5a9641d576b1b2ebdd9a40c/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3233312f343861396664626436376338346133323861396466396563386439336239616332343538616333373732316437643533653531613237666232626463353236332e6a7067)

## Author's disclaimer

```
Welcome to the Python world!

The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

- Guillaume

```

## [](https://github.com/Pericles001/alx-higher_level_programming/tree/main/0x00-python-hello_world#resources)Resources

**Read or watch**:

- [The Python tutorial](https://alx-intranet.hbtn.io/rltoken/JsFCs_NBzMAR7-XPAZ9BoA "The Python tutorial") (_only the first three chapters below_)
- [Whetting Your Appetite](https://alx-intranet.hbtn.io/rltoken/kifRlLG2iMX5AZiW8lrCMg "Whetting Your Appetite")
- [Using the Python Interpreter](https://alx-intranet.hbtn.io/rltoken/RVpfAuagCo9SdfYeoHd6jg "Using the Python Interpreter")
- [An Informal Introduction to Python](https://alx-intranet.hbtn.io/rltoken/bVps0ZPWq7qVZ7vc-eJGTw "An Informal Introduction to Python") (_Read up until "3.1.2. Strings" included_)
- [How To Use String Formatters in Python 3](https://alx-intranet.hbtn.io/rltoken/kopLNaXzBklkJ1fMCa0Gqw "How To Use String Formatters in Python 3")
- [Learn to Program](https://alx-intranet.hbtn.io/rltoken/szBsJ-Qyig_RrImN7RGlOg "Learn to Program")
- [Pycodestyle -- Style Guide for Python Code](https://alx-intranet.hbtn.io/rltoken/tgYt-0zVy1T4sDlE9ohxnA "Pycodestyle -- Style Guide for Python Code")

## [](https://github.com/Pericles001/alx-higher_level_programming/tree/main/0x00-python-hello_world#learning-objectives)Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/TYWTMEj3W1HhTHqMKu8kWA "explain to anyone"), **without the help of Google**:

### [](https://github.com/Pericles001/alx-higher_level_programming/tree/main/0x00-python-hello_world#general)General

- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where does the name 'Python' come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using `print`
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with `pycodestyle`

## [](https://github.com/Pericles001/alx-higher_level_programming/tree/main/0x00-python-hello_world#requirements)Requirements

### [](https://github.com/Pericles001/alx-higher_level_programming/tree/main/0x00-python-hello_world#python-scripts)Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of _this_ project, is mandatory
- Your code should use the pycodestyle (version 2.7.\*)
- All your files must be executable
- The length of your files will be tested using `wc`

### [](https://github.com/Pericles001/alx-higher_level_programming/tree/main/0x00-python-hello_world#shell-scripts)Shell Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`wc -l file` should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be executable

### [](https://github.com/Pericles001/alx-higher_level_programming/tree/main/0x00-python-hello_world#c-scripts)C Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl "betty-style.pl") and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl "betty-doc.pl")
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don't have to push them to your repo (if you do we won't take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don't forget to push your header file
- All your header files should be include guarded

## [](https://github.com/Pericles001/alx-higher_level_programming/tree/main/0x00-python-hello_world#more-info)More Info

### [](https://github.com/Pericles001/alx-higher_level_programming/tree/main/0x00-python-hello_world#zen)Zen

```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

```

### [](https://github.com/Pericles001/alx-higher_level_programming/tree/main/0x00-python-hello_world#pycodestyle)Pycodestyle

`Pycodestyle` is now the [new standard of Python style code](https://alx-intranet.hbtn.io/rltoken/UQ25jC6sA5XqZl6ZZIdAaw "new standard of Python style code")

