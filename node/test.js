var path = require("path");
var hello = "Hello from Nde JS Variable!"
console.log(hello)
console.log("Using PATH module:");
console.log(`Hello from file ${path.basename(__filename)}`);
console.log(`Process args: ${process.argv}`)
