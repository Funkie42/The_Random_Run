from Mastermind import *


#Connection Mastermind

server_ip = 'localhost'
client_ip = 'localhost'
port = 42042

client_timeout_connect = 5.0
client_timeout_receive = 10.0


client = MastermindClientTCP(client_timeout_connect,client_timeout_receive)

def send_data(data): # Data ist ein 4er Tupel mit Spieler, Links/Rechts pos, Koords und erschaffener Kugel
    client.send(data)
    if data[0] == 1:
        return client.receive(True)[1]
    else:
        return client.receive(True)[0]
    

def get_player_number():
    player = 0
    client.send([0])
    if client.receive(True) == [None,None]:
        player = 1
    else:
        player = 2
    return  player
    
