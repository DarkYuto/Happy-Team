const mongodb = require('mongodb');
const MongoClient = mongodb.MongoClient;

const mongoConnect = callback => {
    MongoClient.connect('mongodb://127.0.0.1:27017/database-ml')
    .then(result =>{
        console.log('Connected! - database');
    })
    .catch(err=>{
        console.log(err);
    });
};

module.exports = mongoConnect;

