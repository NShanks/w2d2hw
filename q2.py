# Exercise 2 - Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case


class TwoMethods():
    
    def getString():
        global sentence
        sentence = input("Give me a sentence and I'll work my magic: ")
        return sentence

    def printString():
        global sentence
        print(str.upper(sentence))
        
    getString()
    printString()

TwoMethods()