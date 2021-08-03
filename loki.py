import logic
from data import channel, refresh_rate, connect

def main():
    sock, path = connect()
    print("(Remember to fill \"data.py\"!")
    option = 0
    while option != 1 or option != 2:
        option = int(input("Please select an option:\n1- Write only last message on file\n2- Write all messages to file\n"))
        if option == 1:
            logic.write_message(sock, channel, refresh_rate, path, 'w')
        elif option == 2:
            logic.write_message(sock, channel, refresh_rate, path, 'a')

main()