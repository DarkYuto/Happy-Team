var redis = require("redis");
var http = require("http");
var redisClient = redis.createClient();

http
  .createServer(function (req, res) {
    res.writeHead(200, {
      "Content-Type": "multipart/x-mixed-replace; boundary=frame",
    });
    upd(res);
  })
  .listen(8083);

function upd(res) {
  redisClient.get("rtsp_//mlview_MLview2021_192.168.2.200/cam/realmonitor_channel_5_subtype_1", (err, reply) => {
    if (!err && res) {
      res.write("--frame1" + "\r\n");
      res.write("Content-Type: image/jpeg,\r\n\r\n");
      try {
        res.write(Buffer.from(reply, "base64"));
      } catch (err) {}
      res.write("\r\n\r\n");
    }
  });
  setTimeout(() => upd(res), 30);
}
console.log("Running Streaming at port 8083");
