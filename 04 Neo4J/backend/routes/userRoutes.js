const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');
const authMiddleware = require('../middleware/authMiddleware');

router.put('/update-password', authMiddleware, userController.updatePassword);
router.delete('/delete-account', authMiddleware, userController.deleteAccount);

module.exports = router;
