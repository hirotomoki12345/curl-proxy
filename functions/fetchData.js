// 必要なモジュールのインポート
const express = require('express');
const fetch = require('node-fetch');

// Expressアプリケーションの初期化
const app = express();
const port = 3000;

// ルートハンドラー
app.get('/fetch', async (req, res) => {
    try {
        // クエリパラメーターからURLを取得
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

// サーバーの起動
app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
