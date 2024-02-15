const router = require("express").Router();

router.use("/playlist", require("./playlist"));

router.get("/", (req, res, next) => {
  res.send("In API");
});

router.use((req, res, next) => {
  const error = new Error("404 Not Found");
  error.status = 404;
  next(error);
});

module.exports = router;
