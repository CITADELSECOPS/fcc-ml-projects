// FCC Request Header Parser Microservice
const express = require("express");
const cors = require("cors");
const app = express();
app.enable("trust proxy");
app.use(cors({ optionsSuccessStatus: 200 }));
app.use(express.static("public"));

app.get("/api/whoami", (req, res) => {
  res.json({
    ipaddress: req.ip,
    language: req.headers["accept-language"],
    software: req.headers["user-agent"],
  });
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`listening on ${port}`));
