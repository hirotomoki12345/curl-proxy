import express from 'express';
import fetch from 'node-fetch';
import 'fetch-blob';
import 'formdata-polyfill';

const app = express();
const port = 3000;

app.get('/fetch', async (req, res) => {
    try {
        const url = req.query.url;

        if (!url) {
            return res.status(400).json({ error: 'URL parameter is missing' });
        }

        // fetchリクエスト
        const response = await fetch(url);

        // レスポンスをJSON形式で返す
        const data = await response.json();
        res.json(data);
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
