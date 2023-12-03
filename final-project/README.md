Communicating with a Python server using Node JS


Description:

    These scripts work in conjuction to allow for communication from a Node JS script to a Python server hosting an application. 
    The application takes input from the Node JS script to calculate a users predicted GPA for a semester. 
    The Node JS script has a pre-defined array of values, which represent predicted GPA quality points for each class. 
    The Node JS script includes the necessary parameters to communicate with the Python server. 
    As mentioned, the technologies used in these scripts are Python and Node JS, but a few extra modules did need to be installed.

    For Python:

        Flask was installed using: pip install flask
    
    For Node JS:

        Request-Promise was installed using: npm install request-promise


    These technologies were chosen due to their simplicity in creating a server and their diverse collection of libraries to include. Some challenges faced during this script's creation were
    communication errors between the server. Another challenge I faced was to take user input in Node JS for the array. However, I ran into many issues with conversion. This is a feature I do hope to 
    implement soon. 


Execution:

    To start the Python Flask application server: python3 gpApplication.py
    To run the Node JS script: node userFile.js


Expected Output:

  Python Server:
  
    *Serving Flask App 'gpApplication'
    *Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit


  Node JS Script:
  
    Your predicted semseter GPA:  3.86668



References:    
https://www.geeksforgeeks.org/node-js-npm-node-package-manager/    
https://www.freecodecamp.org/news/python-string-to-array-how-to-convert-text-to-a-list/    
https://www.codemag.com/Article/1405000/Node.js-Succinctly    
https://www.geeksforgeeks.org/how-to-communicate-json-data-between-python-and-node-js/    
https://lucymarmitchell.medium.com/using-then-catch-finally-to-handle-errors-in-javascript-promises-6de92bce3afc    
   
