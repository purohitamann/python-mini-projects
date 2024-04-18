const express = require('express');
const router = express.Router();
const generateCaptions = require('../utils/generativeai');  // Replace with your implementation

router.post('/', async (req, res) => {
  try {
    const photoDescription = req.body.description;
    const captions = await generateCaptions(photoDescription);
    res.json({ captions });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Error generating captions' });
  }
});

module.exports = router;
