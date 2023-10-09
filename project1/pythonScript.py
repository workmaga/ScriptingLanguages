#specifies which file to search through
searchFile = open("project1.txt", "r");

#reads the file into a string and stores that string in readText
readText = searchFile.read();

#splits the string 'readText' into a list where each word is a list item (array)
#\n 
fileWords = readText.split("\n");


#checking a pre-defined array of words
userWords = ["Password", "Username"]

#nested for loops

#creates new variable wordIndex and loops through the searchWords array in search
for wordIndex in fileWords:
    #another for loop to include the userWords array, creates new variable word 
    for word in userWords:
        #if statement that says "If the word is in the file, print the line containing the word."
        if word in wordIndex:
            print(wordIndex)
            #stops the loop 
            break
#closes the file 
searchFile.close();