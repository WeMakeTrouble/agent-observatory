
// Add WebSocket support for live streaming
const WebSocket = require('ws');
const wss = new WebSocket.Server({ server: require('http').createServer(app) });

wss.on('connection', function connection(ws) {
    console.log('Public viewer connected');
    ws.send('Public viewer connected to Echo Genesis!');
});

// Function to broadcast simulation data to public viewers
global.broadcastToViewers = function(simulationData) {
    wss.clients.forEach(function each(client) {
        if (client.readyState === WebSocket.OPEN) {
            client.send(simulationData);
        }
    });
};
