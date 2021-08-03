import socket
from pathlib import Path

server = 'irc.chat.twitch.tv' # Twitch server
port = 6667 # Twitch port

# In order to connect to Twitch, you must complete the following fields:
nickname = '' # Your nickname goes here (Example: 'RodmarKun')
token = '' # Oauth token (You can get it at https://twitchapps.com/tmi/)
channel = '' # Channel you want to receive messages from, must start with '#' (Example: '#ninja')
absolute_path = r"" # Path of text file to write last message (Example: r"C:\Users\A\TwitchMessage.txt")
refresh_rate = 0.5 # Should be enough to catch up with fast-writing chats

def connect():
    print("Connecting...")
    sock = socket.socket()
    sock.connect((server, port))

    sock.send(f"PASS {token}\n".encode('utf-8')) 
    sock.send(f"NICK {nickname}\n".encode('utf-8')) 
    sock.send(f"JOIN {channel}\n".encode('utf-8')) 

    path = Path(absolute_path)
    return sock, path