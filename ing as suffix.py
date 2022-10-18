#if the length of the user input is greater than 3 characters then add ing as suffix otherwise print the same input.
word= str(input("Enter the word:"))
if len(word)>3:
    print(word+"ing")
else:
 print("word")