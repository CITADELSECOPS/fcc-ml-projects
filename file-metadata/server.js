// FCC File Metadata Microservice
const express = require("express");
const cors = require("cors");
const multer = require("multer");

const app = express();
app.use(cors({ optionsSuccessStatus: 200 }));
app.use(express.static("public"));

const upload = multer({ storage: multer.memoryStorage() });

app.post("/api/fileanalyse", upload.single("upfile"), (req, res) => {
  if (!req.file) return res.status(400).json({ error: "no file" });
  res.json({
    name: req.file.originalname,
    type: req.file.mimetype,
    size: req.file.size,
  });
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`listening on ${port}`));
