from bs4 import BeautifulSoup
import urllib.request

#passing URL and file path to store html raw code
urllib.request.urlretrieve("https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-vm",
"/root/it3038c-scripts/project2/html-raw.txt")

#opens the file containing raw html code and reads through it (indicated by "r")
searchFile = open("html-raw.txt", "r")
searchFileContents = searchFile.read()
# using BeautifulSoup to parse through the raw html 
soup = BeautifulSoup(searchFileContents, "html.parser")

#this variable contains the newly opened "paragraph-text.txt" file in write* mode
paragraphText = open("paragraph-text.txt", "w")

# creates variable data using for loop to extract contents of all <p> tags
for data in soup.find_all("p"):
	findings = data.get_text()
	paragraphText.writelines(findings)

#opens the file in read* mode
paragraphText = open("paragraph-text.txt", "r")

readText = paragraphText.read()

#checking a pre-defined array of words
userWords = ["networking"]

#another for loop to include the userWords array, creates new variable word 
for word in userWords:
        #if statement that says "If the word is in the file, print the line containing the word."
        if word in readText:
            print(word)
            #stops the loop 
            break
#closes the file 
paragraphText.close()



