var mqtt = require('mqtt');
var client = mqtt.connect('mqtt://35.154.14.203:1883');
var mongoose = require('mongoose');
mongoose.connect('mongodb://exozen:exozen123@35.154.14.203:25713/zengap');

//mongoose.connect('mongodb://admin:admin123@ds123834.mlab.com:23834/newapp');

var db = mongoose.connection;
var moment = require('moment');
 
db.on('error', console.error.bind(console, 'connection error:'));
 
db.once('open', function() {
    console.log("Connection to Database Successful!");
    });
client.on('connect', function() { // When connected
  console.log('Connection to MQTT Broker Established');
    // subscribe to a topic
    client.subscribe('ssb', function() {
        // when a message arrives, do something with it
        client.on('message', function(topic, message, packet) {
            var j = ""+message+"";
            //var j = i.substring(1);
               var n = j.indexOf("-");
            var z = j.substring(0,n);
            var k = j.substring((n+1));
            var s = parseFloat(k);
           var ss = s;
         var zzzz = z.substring(0,5);
         var zzz =  z.substr(z.length - 4)
         var zz = zzz.substring(0,2);
           console.log(j);
           var m = moment().unix()
        var n = m+19800
        var date1 = new Date(n * 1000);
var datetime = new Date();

var date = new Date(new Date().setDate(new Date().getDate()));
        var yesterday1 = date.toISOString().slice(0, 10);
             var datestart = datetime + "T00:00:00.000Z";
               var dateend = yesterday1 + "T00:00:00.000Z";
               console.log(date);
var query = { device_id: z, date: {$gte:new Date(dateend),$lt:new Date(date1)}};
db.collection("admin_inlet_consumptions").find(query).sort({date:1}).toArray(function (err, result) {

var len = result.length
last= result[len-1]
last_c=result[len-1].consumption
p_last=result[len-2].consumption
//console.log(result)
if (err) throw err;
var len = result.length
if (len != 0){
var cons = parseFloat(result[-1])
console.log("last_c", last_c)
console.log("p_last", p_last)
console.log("s", s)

//console.log("con",result)
console.log(date);
//console.log("last",last[consumption]);
//var con = cons>s;
//if((s>last_c)||(s==last_c)){
if(s>last_c){
var myobj1 = { device_id:z,consumption:s,date:date1};
var format = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;
db.collection("ssb_demo").insertOne(myobj1, function (err, res) {
if (err) throw err;
console.log("successfully calculated difference and inserted");
}
);
}else if((device_id.match(format))||(consumption.match(format))){
    
    console.log("Nan error");
    
  }else{
    console.log("error");
  }
}
});         
});
});
});



