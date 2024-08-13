const User = require('../models/userModel');

exports.updatePassword = async (req, res) => {
  const { username, newPassword } = req.body;
  try {
    const user = await User.updatePassword(username, newPassword);
    res.json({ message: 'Password updated successfully', user });
  } catch (error) {
    res.status(500).json({ error: 'Error updating password' });
  }
};

exports.deleteAccount = async (req, res) => {
  const { username } = req.body;
  try {
    await User.delete(username);
    res.json({ message: 'Account deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Error deleting account' });
  }
};
