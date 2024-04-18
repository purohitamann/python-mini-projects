const express = require('express');
const cors = require('cors'); // Add CORS for development
const app = express();
const port = process.env.PORT || 5000;

app.use(cors()); // Enable CORS for all origins during development
app.use(express.json());

// Routes (replace with your actual implementation)
app.use('/captions-ai', require('./routes/captions-ai'));

app.listen(port, () => console.log(`Server listening on port ${port}`));
