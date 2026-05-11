// FCC Exercise Tracker
const express = require("express");
const cors = require("cors");
const { randomUUID } = require("crypto");

const app = express();
app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.static("public"));

const users = []; // {_id, username}
const exercises = []; // {user_id, description, duration, date}

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

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`listening on ${port}`));
