const User = require('../models/userModel');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

exports.signup = async (req, res) => {
  const { username, password } = req.body;
  console.log(username);
  console.log(password);
  const hashedPassword = await bcrypt.hash(password, 10);
  try {
    const user = await User.create(username, hashedPassword);
    res.status(201).json({ message: 'User created successfully', user });
  } catch (error) {
    console.log(error);
    res.status(500).json({ error: 'Error creating user' });
  }
};

exports.login = async (req, res) => {
  const { username, password } = req.body;
  
  try {
    const userRecord = await User.findByUsername(username);
    if (!userRecord) {
      return res.status(404).json({ error: 'User not found' });
    }
    const validPassword = await bcrypt.compare(password, userRecord.properties.password);
    if (!validPassword) {
      return res.status(400).json({ error: 'Invalid password' });
    }
    const token = jwt.sign({ username: userRecord.properties.username }, 'secretkey', { expiresIn: '1h' });
    res.json({ message: 'Login successful', token });
  } catch (error) {
    res.status(500).json({ error: 'Error logging in' });
  }
};
