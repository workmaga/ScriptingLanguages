var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');



http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        myIpAddress=ip.address();
        uptime=os.uptime();
        uptimeDays = Math.floor(uptime / 86400);
        uptimeHours = Math.floor(uptime / 3600) - (uptimeDays * 24);
        uptimeMinutes = Math.floor(uptime / 60) - (uptimeHours * 60);
        uptimeSeconds = Math.floor(uptime % 60);
        tMem=os.totalmem() / 1000000;
        fMem=os.freemem() / 1000000;
        numberCpu=os.cpus().length;
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${myIpAddress}</p>
            <p>Server Uptime: Days: ${uptimeDays}, Hours: ${uptimeHours}, Minutes: ${uptimeMinutes}, Seconds: ${uptimeSeconds}</p>
            <p>Total Memory: ${tMem.toPrecision(7)} MB</p>
            <p>Free Memory: ${fMem.toPrecision(5)} MB</p>
            <p>Number of CPUs: ${numberCpu}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");