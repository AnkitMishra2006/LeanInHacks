const express = require("express");
const app = express();
const port = 8080;
const path = require("path");

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static(path.join(__dirname, "/public")));

app.get("/", (req, res) => {
  res.sendfile("index.html");
});

app.post("/predict", (req, res) => {
  let data = req.body["userData"];
  res.send(data);
});

app.listen(port, () => {
  console.log(`app is listening on port ${port}`);
});
