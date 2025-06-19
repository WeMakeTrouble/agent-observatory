const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const path = require('path');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

const PORT = process.env.PORT || 3000;

// Serve static files
app.use(express.static('.'));

// Serve main page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// WebSocket for live streaming
wss.on('connection', function connection(ws) {
    console.log('🌌 Public viewer connected');
    ws.send('Public viewer connected to Echo Genesis!');
    
    ws.on('close', function() {
        console.log('👁️ Viewer disconnected');
    });
});

// Function to broadcast simulation data to public viewers
global.broadcastToViewers = function(simulationData) {
    console.log('📡 Broadcasting to viewers');
    wss.clients.forEach(function each(client) {
        if (client.readyState === WebSocket.OPEN) {
            client.send(simulationData);
        }
    });
};

server.listen(PORT, () => {
    console.log(`🖥️ Agent Observatory running on port ${PORT}`);
});
