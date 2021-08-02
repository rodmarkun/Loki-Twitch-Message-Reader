"""
Loki is a very simple script made in python to read Twitch Chat messages in real time
and write them down in a file. In this version it only writes the last message sent, but
feel free to modify its behaviour as you want.
"""
import socket
from pathlib import Path
from time import sleep

server = 'irc.chat.twitch.tv' # Twitch server
port = 6667 # Twitch port

# In order to connect to Twitch, you must complete the following fields:
nickname = '' # Your nickname goes here (Example: 'RodmarKun')
token = '' # Oauth token (You can get it at https://twitchapps.com/tmi/)
channel = '' # Channel you want to receive messages from, must start with '#' (Example: '#ninja')
absolute_path = r"" # Path of text file to write last message (Example: r"C:\Users\A\TwitchMessage.txt")
refresh_rate = 0.5 # Should be enough to catch up with fast-writing chats

sock = socket.socket()
sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8')) 
sock.send(f"NICK {nickname}\n".encode('utf-8')) 
sock.send(f"JOIN {channel}\n".encode('utf-8')) 

response = ""
p = Path(absolute_path)

while True:
    response = sock.recv(2048).decode("utf-8")
    if(response.find("PRIVMSG") != -1):
        message = response.split(channel + " :")[1]
        # After getting the message, you can now do as you want with it,
        # by default it writes only the last message in a file:
        print(message)
        f = open(p, 'w')
        f.write(message)
        f.close()
    else:
        print(response)  
    if response == "PING :tmi.twitch.tv\r\n":
        sock.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    sleep(refresh_rate)