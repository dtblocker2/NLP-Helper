// const express = require('express');

// app = express();

async function getOllamaResponse() {
    prompt = document.getElementById('prompt').value;
    console.log(prompt);
    document.getElementById('response_text').innerHTML = 'fetching...';
    const response = await fetch('http://localhost:11434/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model: 'gemma3:4b', prompt: prompt, stream: true })
    });
    const text = await response.text();
    const lines = text.trim().split('\n');
    const responses = lines.map(line => JSON.parse(line));
    const fullResponse = responses.map(r => r.response).join('');
    console.log(fullResponse);
    document.getElementById('response_text').innerHTML = fullResponse;
}

// app.set('view engine', 'ejs')

// app.get('/', (req,res) => {
//     app.use(express.static(path.join(__dirname, '/public')));
//     res.render('index');
// })

// app.listen(3000, () => console.log('app running at port: 3000'))