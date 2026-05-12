// Combined BE V8 services on single Express server
const express = require("express");
const cors = require("cors");
const { randomUUID } = require("crypto");
const { URL } = require("url");
const dns = require("dns");
const multer = require("multer");

const app = express();
app.enable("trust proxy");
app.use(cors({ optionsSuccessStatus: 200 }));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// ========== TIMESTAMP ==========
const timestamp = express.Router();
timestamp.get("/:date?", (req, res) => {
  const param = req.params.date;
  let d;
  if (!param) d = new Date();
  else if (/^\d+$/.test(param)) d = new Date(parseInt(param, 10));
  else d = new Date(param);
  if (isNaN(d.getTime())) return res.json({ error: "Invalid Date" });
  res.json({ unix: d.getTime(), utc: d.toUTCString() });
});

// ========== HEADER PARSER ==========
app.get("/api/whoami", (req, res) => {
  res.json({
    ipaddress: req.ip,
    language: req.headers["accept-language"],
    software: req.headers["user-agent"],
  });
});

// ========== URL SHORTENER ==========
const urls = [];
app.post("/api/shorturl", (req, res) => {
  const input = req.body.url || "";
  let parsed;
  try { parsed = new URL(input); } catch { return res.json({ error: "invalid url" }); }
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

// ========== EXERCISE TRACKER ==========
const users = [];
const exercises = [];
app.post("/api/users", (req, res) => {
  const user = { _id: randomUUID(), username: req.body.username };
  users.push(user);
  res.json(user);
});
app.get("/api/users", (req, res) => res.json(users));
app.post("/api/users/:_id/exercises", (req, res) => {
  const user = users.find((u) => u._id === req.params._id);
  if (!user) return res.status(404).json({ error: "user not found" });
  const date = req.body.date ? new Date(req.body.date) : new Date();
  const ex = {
    user_id: user._id,
    description: String(req.body.description),
    duration: parseInt(req.body.duration, 10),
    date: date.toDateString(),
  };
  exercises.push(ex);
  res.json({
    _id: user._id, username: user.username,
    description: ex.description, duration: ex.duration, date: ex.date,
  });
});
app.get("/api/users/:_id/logs", (req, res) => {
  const user = users.find((u) => u._id === req.params._id);
  if (!user) return res.status(404).json({ error: "user not found" });
  let log = exercises.filter((e) => e.user_id === user._id);
  const { from, to, limit } = req.query;
  if (from) log = log.filter((e) => new Date(e.date) >= new Date(from));
  if (to) log = log.filter((e) => new Date(e.date) <= new Date(to));
  if (limit) log = log.slice(0, parseInt(limit, 10));
  res.json({
    _id: user._id, username: user.username, count: log.length,
    log: log.map(({ user_id, ...e }) => e),
  });
});

// ========== FILE METADATA ==========
const upload = multer({ storage: multer.memoryStorage() });
app.post("/api/fileanalyse", upload.single("upfile"), (req, res) => {
  if (!req.file) return res.status(400).json({ error: "no file" });
  res.json({
    name: req.file.originalname,
    type: req.file.mimetype,
    size: req.file.size,
  });
});

// Mount timestamp last so /api/* doesn't conflict
app.use("/api", timestamp);

// Root
app.get("/", (req, res) => res.send("FCC BE V8 services live"));

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`BE all-in-one listening on ${port}`));
