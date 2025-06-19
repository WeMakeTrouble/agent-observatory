// --- Make the window draggable ---
const windowElement = document.getElementById('simulation-window');
const titleBar = windowElement.querySelector('.title-bar');
let isDragging = false;
let offsetX, offsetY;

titleBar.addEventListener('mousedown', (e) => {
    isDragging = true;
    offsetX = e.clientX - windowElement.offsetLeft;
    offsetY = e.clientY - windowElement.offsetTop;
    document.body.style.userSelect = 'none'; // Prevent text selection while dragging
});

document.addEventListener('mousemove', (e) => {
    if (isDragging) {
        windowElement.style.left = `${e.clientX - offsetX}px`;
        windowElement.style.top = `${e.clientY - offsetY}px`;
    }
});

document.addEventListener('mouseup', () => {
    isDragging = false;
    document.body.style.userSelect = 'auto';
});

// --- Simulate Live Data Feed ---
const logElement = document.getElementById('simulation-log');
let step = 0;

// This function simulates receiving data from our Python engine.
// In the future, this would be replaced with a real data fetch.
function updateLog() {
    step++;
    const mockData = `
=========================================
| SIMULATION STATE | STEP: ${String(step).padStart(4, '0')}
=========================================

[-- WORLD STATUS --]
  > ENVIRONMENT: The White (Still, Silent)
  > LIGHT LEVEL: Bright [||||||||||] 100%

[-- AGENT DASHBOARD: One --]
  > LOCATION: {x: ${Math.floor(Math.random() * 20 - 10)}, y: ${Math.floor(Math.random() * 20 - 10)}}
  > COGNITIVE STATE: Exploring
  > IKIGAI LEVEL: [■□□□□□□□□□] 1.0 / 10.0

[-- EVENT BUS: LIVE FEED --]
  [${step}] EVENT: One chose action 'Explore'.
  [${step+1}] EVENT: One moved to new location.
`;
    logElement.textContent = mockData;
}

// Update the log every 2 seconds to simulate a live feed.
setInterval(updateLog, 2000);

// Initial call to populate the log
updateLog();
