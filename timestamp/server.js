// FCC Timestamp Microservice
const express = require("express");
const cors = require("cors");
const app = express();
app.use(cors({ optionsSuccessStatus: 200 }));
app.use(express.static("public"));

app.get("/api/:date?", (req, res) => {
  const param = req.params.date;
  let d;
  if (!param) d = new Date();
  else if (/^\d+$/.test(param)) d = new Date(parseInt(param, 10));
  else d = new Date(param);
  if (isNaN(d.getTime())) return res.json({ error: "Invalid Date" });
  res.json({ unix: d.getTime(), utc: d.toUTCString() });
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`listening on ${port}`));
