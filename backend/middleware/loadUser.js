function loadUser(req, res, next) {
  if (req.session.user) {
    req.user = JSON.parse(req.session.user);
  }
  next();
}

module.exports = loadUser;
