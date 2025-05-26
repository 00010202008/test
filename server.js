const express = require('express');
const path = require('path');
const { spawn } = require('child_process');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files like index.html
app.use(express.static(__dirname));

// Handle PHP requests manually
app.get('/store.php', (req, res) => {
    const php = spawn('php-cgi', ['store.php'], {
        env: {
            ...process.env,
            REQUEST_METHOD: 'GET',
            QUERY_STRING: req.url.split('?')[1] || '',
            SCRIPT_FILENAME: path.join(__dirname, 'store.php'),
        }
    });

    let output = '';
    php.stdout.on('data', (data) => {
        output += data.toString();
    });

    php.stderr.on('data', (data) => {
        console.error('PHP error:', data.toString());
    });

    php.on('close', () => {
        // Remove headers if they exist
        const [, body] = output.split('\r\n\r\n');
        res.send(body || output); // fallback to raw output
    });
});

app.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}`);
});
