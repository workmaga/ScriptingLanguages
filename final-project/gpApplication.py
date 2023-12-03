import json 
from flask import Flask, request 

# Setup flask server 
app = Flask(__name__) 

# We set up the URL route as /gpacalc for the Node JS script to communicate with 
@app.route('/gpacalc', methods = ['POST']) 
def predicted_scores():
	
    #data with a POST tag will get placed into this 'data' variable
    receivedData = request.get_json()

    # formmattedData variable to store list of data - receivedData is converted to a list using the name of our array in the Node JS script (['array'])
    formattedData = receivedData['array']  
    result = ((sum(formattedData * 3))/15) # calculate the sum (assumes 5 classes of 3.0 credit hours are being taken)

    # Return data in json format  
    return json.dumps({"result":result}) 

#Running flask server on port 5000
if __name__ == "__main__": 
	app.run(port=5000)
