const connection = require("./model");
const express = require("express");
const application = express();
const path = require("path");
const expressHandlerbars = require("express-handlebars");
const bodyparser = require("body-parser");
const CourseController = require("./controllers/courses");
const { handle } = require("express/lib/application");

application.use(bodyparser.urlencoded({
  extended: true
}));

application.set('views',path.join(__dirname,"/views/"));



application.engine("hbs", expressHandlerbars.engine(
  {
 
  extname:"hbs",
  defaultLayout: "mainlayout",
  layoutsDir: __dirname +"/views/layouts"
}));

application.set("view engine","hbs");

application.get("/",(req,res) =>{
  //res.send('<h1>Hi welcome</h1>')
  res.render("index",{})
});

application.use("/course", CourseController ); 
 

application.listen('3000', ()=> {
  console.log("server started")
});