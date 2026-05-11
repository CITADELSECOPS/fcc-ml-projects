// FCC URL Shortener Microservice
const express = require("express");
const cors = require("cors");
const dns = require("dns");
const { URL } = require("url");

const app = express();
app.use(cors({ optionsSuccessStatus: 200 }));
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));

const urls = []; // index 0..n => original_url

app.post("/api/shorturl", (req, res) => {
  const input = req.body.url || "";
  let parsed;
  try { parsed = new URL(input); }
  catch { return res.json({ error: "invalid url" }); }
  if (!/^https?:$/.test(parsed.protocol)) return res.json({ error: "invalid url" });
  dns.lookup(parsed.hostname, (err) => {
    if (err) return res.json({ error: "invalid url" });
    const idx = urls.indexOf(input);
    const short = idx === -1 ? urls.push(input) - 1 : idx;
    res.json({ original_url: input, short_url: short });
  });
});

app.get("/api/shorturl/:short", (req, res) => {
  const short = parseInt(req.params.short, 10);
  const original = urls[short];
  if (!original) return res.json({ error: "No short URL found for the given input" });
  res.redirect(original);
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`listening on ${port}`));
