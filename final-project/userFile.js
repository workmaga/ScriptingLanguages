var request = require('request-promise'); 

async function gpacalc() { 
    
    
    // Predicted GPA quality points entered into an array(using the UC GPA calculation chart)
    var gpaQP = { 

        array: [4.0, 4.0, 3.6667, 3.6667, 4.0]

    }

    //Parametrs on what to do with the data (eg. POST to the python server containing the script)
    var parameters = { 
        method: 'POST', 
          // http:flaskserverurl:port/route 
        uri: 'http://127.0.0.1:5000/gpacalc', 
        //Puts the data in the 'data' variable into the 'body' option to pass to the flask server 
        body: gpaQP, 

        //Converts data to JSON
        json: true
    }; 

    var send = await request(parameters) 

        //We parse the body containing the JSON data from the Flask server then display returned results
        .then(function (parsedBody) { 
            
            //*local* variable 'result'
            let result; 
            result = parsedBody['result']; 
            console.log("Your predicted semseter GPA: ", result); 
        }) 
        //Standard Node JS error prediction
        .catch(function (err) { 
            console.log(err); 
        }); 
} 

gpacalc(); 