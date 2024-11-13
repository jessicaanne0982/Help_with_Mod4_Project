# Library Management System

The Library Management System is an application designed to allow users to easily manage all aspects of the library system - 
from the catalog of book titles to the list of library patrons to a directory of authors and their short biographies.  
Created in Python 3.13, this application demonstrates newly acquired knowledge of OOP principles, the practice of clean coding, 
and implementation of modular program writing.

## Installation

On a Windows PC, this application can be run in the Command Window.  Mac OS can run withing the Terminal Window.  
Ensure all files are present.

### Necessary files:
#### Main file to execute:
1. Library Management System.py

#### Classes within:
1. book_operations.py
2. patron_operations.py
3. author_operations.py

#### Text files required for file writing functions:
1. book_catalog.txt
2. patron_list.txt
3. author_list.txt

## Usage

This a multiple level program that begins by asking the user what type of operation they'd like to perform.
```python
Welcome to the Library Management System!

Please Choose from the following menu:
1. Book Operations
2. Patron Operations
3. Author Operations
4. Quit
```
From here, the user is presented with a number of different menus to perform operations specific to either 
books, patrons, or authors.
```python
Book Operations Menu:
1. Add a new book
2. Borrow a book
3. Return a book
4. Search for a book
5. Display all books
6. Export library catalog to a text file
```
```python
Patron Operations Menu:
1. Add a new patron
2. View patron details
3. Display all patrons
4. Export patrons to a text file
```
```python
Author Operations Menu:
1. Add a new author
2. View author details
3. Display all authors
4. Export authors to a text file
```
These menus allow the user to variety of options to navigate within the library system and to perform a number of 
helpful functions.  Error catching helps guide the user gracefully in the event of accidental incorrect input.