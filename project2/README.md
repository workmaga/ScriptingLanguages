The project 2 python script builds off of the project 1 script and performs two functions:

1. Searches and retrieves raw html code from a website, parses through it, and extracts the contents of all <p> tags to be stored in a file.

2. Searches the file containg pargraph tag contents and outputs words based on pre-defined search terms.


What you will need:

  The bs4 module will need to be installed using pip, which can be done by running "pip install bs4".
  You will need to import the urllib.request python module.


How to run:

  Download the project 2 files.
  Determine the website and list of search words/terms that you are looking for. Change to the directory of the downloaded files and change the value of 'userWords' within the python script to include your words or terms.
  Make the script executable by running "chmod +x project2.py"
  Execute the script by running "python3 project2.py"


Output:

  If the search term you entered is found within the paragraph tags, it will be outputted to the screen. If the search word/term is NOT found, you will receive no response or output.
  Raw html code will be found in html-raw.txt
  The text from each paragraph tag will be found in paragraph-text.txt
  
  
Sources:
https://stackoverflow.com/questions/19184335/is-there-a-need-for-rangelena
https://stackoverflow.com/questions/51567427/find-specific-words-in-text-file-and-print-the-line-using-python?rq=3
https://stackoverflow.com/questions/31016734/selecting-specific-words-from-a-file-in-python
https://www.geeksforgeeks.org/how-to-extract-paragraph-from-a-website-and-save-it-as-a-text-file/
