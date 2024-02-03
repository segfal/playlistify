const router = require("express").Router();

router.get("/", (req, res) => {
  res.send("in auth");
});

router.use("/login", require("./login"));
router.use("/callback", require("./callback"));

router.use((req, res, next) => {
  const error = new Error("404 Not Found");
  error.status = 404;
  next(error);
});

module.exports = router;
