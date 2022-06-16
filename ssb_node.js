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

        //var date1 = new Date(n * 1000);
var datetime = new Date()
//console.log(j);

var n = j.indexOf("-");
var device_id = j.substring(0,n);
var consumption = j.substring((n+1));
//var s = parseFloat(k);
//var ss = s;
//var zzzz = z.substring(0,5);
//var zzz =  z.substr(z.length - 4)
//var zz = zzz.substring(0,2);
// console.log(j);
var m = moment().unix()
var n = m+19800

//console.log("device_id:",device_id);
//console.log("consumption:",consumption);
//l= consumption.length
//c=consumption[l-1]
//console.log("c", c)

var datetime = new Date().toISOString().slice(0, 10);
console.log(datetime);
var date = new Date(new Date().setDate(new Date().getDate() - 170));
        var yesterday1 = date.toISOString().slice(0, 10);
             var datestart = datetime + "T00:00:00.000Z";
               var dateend = yesterday1 + "T00:00:00.000Z";
               //console.log(z);
var query = { device_id: device_id, date: {$gte:new Date(dateend),$lt:new Date(date1)}};
db.collection("admin_inlet_consumptions").find(query).sort({date:-1}).toArray(function (err, result) {
if (err) throw err;
var len = result.length
last= result[len-1]
//console.log("result",result)
//console.log("last",last)
if (len != 0){

var cons= parseFloat(result[0].consumption)
last_c= last.consumption
consumption= result[0].consumption
console.log("res",result[0].device_id)
console.log("res[0]",result[0].consumption)
val= cons-last_c
console.log("cons",consumption)
console.log("cons",cons)
console.log("last_c",last.consumption)
//val= cons-last;
//console.log("val",consumption-last );
console.log("value",consumption-last_c);
//var con = cons>s;
//if(cons>s){
if(last_c<cons){ 
var myobj1 = { device_id:z,consumption:s,date:date};
db.collection("ssb_node_test").insertOne(myobj1, function (err, res) 
{
if (err) throw err;
console.log("successfully calculated difference and inserted");
}

);
}else{
  console.log("error");
}
}
});         
});
});
});