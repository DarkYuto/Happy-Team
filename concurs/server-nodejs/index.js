var redis = require("redis");

const express = require("express");
// const mongoConnect = require("./util/database");
const path = require("path");
const app = express();
const io = require("./util/socket");
const bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({extended:false}));

app.set("views", path.join(__dirname, "views/pages"));
app.use(express.static(path.join(__dirname, "views/public")));
app.set("view engine", "pug");


// get '/camera' page route
app.get("/", (req,res) => {
  res.render("camera");
});




app.listen(8082, ()=> {
  console.log("Server started on port 8082... ");
});

