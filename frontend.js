function reloadCSS() {
    const stylesheet = document.getElementById('meineCSS');
    const timestamp = new Date().getTime(); // Ein Zeitstempel, um eine neue Anforderung zu erzwingen
  
    // Füge eine zufällige Query-Parameter mit dem aktuellen Zeitstempel hinzu, um das Caching zu vermeiden
    stylesheet.href = `style.css?timestamp=${timestamp}`;
  }
reloadCSS();

const socket = new WebSocket('ws://localhost:8765');

socket.onopen = function(event) {
    console.log('WebSocket opened');
};

socket.onmessage = function(event) {
    console.log('Received message:', event.data);
    const div = document.createElement('div')
    div.id = 'element'
    div.textContent = event.data
    const zieldiv = document.getElementById('container')
    zieldiv.appendChild(div)
};

function send() {
    const eingabe = document.getElementById("eingabe").value
    console.log(eingabe)
    let op = "add"
    socket.send(op.concat(" ", eingabe))
}

function calc() {
    socket.send("calc")
}