const SOCK_PORT = 8084;
const io = require('socket.io')(SOCK_PORT);
console.log(`Socket Server started on ${SOCK_PORT}`);

io.on('connection', client=>{
    console.log(`Client : ${client.id} has connected.`)

    client.on('disconnect',()=>{
        console.log(`[CLIENT] : ${client.id}  has disconnected`);
    });
});

module.exports = io;