import asyncio
import websockets
import webbrowser
import os
import platform

# Funktion zum Löschen des Bildschirms basierend auf dem Betriebssystem
def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:  # Anderes Betriebssystem (z. B. MacOS, Linux)
        os.system('clear')

def upp(msg):
    ops = msg.split(',')
    result = 0
    for i in ops:
        result += int(i)
    result = str(result)
    return result

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)
        
        
async def main():
    # Aufruf der Funktion zum Löschen des Bildschirms
    clear_screen()

    # Ausgabe, die den Start des Servers anzeigt
    print("WebSocket-Server wird gestartet und lauscht auf 'http://localhost:8765'...")

    server = await websockets.serve(echo, 'localhost', 8765)

    # Öffne den Browser-Link, nachdem der Server gestartet wurde
    url = 'http://localhost:2406'  # Ändere die URL entsprechend deiner Anforderungen
    webbrowser.open(url)

    await server.wait_closed()

# Ereignisschleife erstellen und main-Funktion ausführen
if __name__ == "__main__":
    asyncio.run(main())
