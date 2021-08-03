from time import sleep

def write_message(sock, channel, refresh_rate, path, mode):
    response = ""
    while True:
        response = sock.recv(2048).decode("utf-8")
        if(response.find("PRIVMSG") != -1):
            message = response.split(channel + " :")[1]
            print(message)
            f = open(path, mode)
            f.write(message)
            f.close()
        else:
            print(response)  
        if response == "PING :tmi.twitch.tv\r\n":
            sock.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        sleep(refresh_rate)