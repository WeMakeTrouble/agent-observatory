const terminalOutput = document.getElementById('terminal-output');
const rabbitHoleContent = document.getElementById('rabbit-hole-content');
const rabbitHoleBtn = document.getElementById('rabbitHoleBtn');
const simulationFeed = document.getElementById('simulation-feed');
const blinkingCursor = document.querySelector('.blinking-cursor');
let isInRabbitHole = false;

rabbitHoleBtn.addEventListener('click', () => {
    isInRabbitHole = !isInRabbitHole;
    if (isInRabbitHole) {
        terminalOutput.style.display = 'none';
        rabbitHoleContent.style.display = 'block';
        rabbitHoleBtn.textContent = 'RETURN';
        rabbitHoleBtn.style.background = 'linear-gradient(135deg, #ff6b6b, #ff5252)';
        rabbitHoleBtn.style.color = '#fff';
    } else {
        terminalOutput.style.display = 'block';
        rabbitHoleContent.style.display = 'none';
        rabbitHoleBtn.textContent = 'RABBIT HOLE';
        rabbitHoleBtn.style.background = 'linear-gradient(135deg, #e8e0d5, #d0c8bd)';
        rabbitHoleBtn.style.color = '#333';
    }
});

const API_URL = 'http://127.0.0.1:5000/api/simulation-state';

async function fetchAndUpdateFeed() {
    if (isInRabbitHole) return;

    try {
        const response = await fetch(API_URL);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();
        simulationFeed.innerHTML = `<pre>${data.terminal_output}</pre>`;
        terminalOutput.appendChild(blinkingCursor);
        terminalOutput.scrollTop = terminalOutput.scrollHeight;

    } catch (error) {
        const feedText = simulationFeed.textContent;
        if (!feedText.includes("CONNECTION LOST")) {
           simulationFeed.innerHTML += `<p style='color:red;'>\n> CONNECTION TO MULTIVERSE ENGINE LOST...</p>`;
        }
    }
}

setInterval(fetchAndUpdateFeed, 3000);
console.log("✅ Observatory initialized. Attempting to connect to live simulation engine...");
