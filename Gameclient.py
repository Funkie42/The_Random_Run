from Mastermind import *


#Connection Mastermind

server_ip = 'localhost'
client_ip = 'localhost'#192.168.178.37'
port = 42042

client_timeout_connect = 5.0
client_timeout_receive = 10.0

client = None

def create_Client(mainport,mainclient_ip):
    global client,server_ip,client_ip, port
    port = mainport
    client_ip = mainclient_ip
    client = MastermindClientTCP(client_timeout_connect,client_timeout_receive)
    client.connect(client_ip,port)

def send_data(data):
    client.send(data)
    recieved_data = client.receive(True)
    if data == "gg" or recieved_data == "gg":
        return "gg"
    elif recieved_data[0] == "level finished":
        return recieved_data
    elif data[0] == 1: # Spieler 1 oder 2
        return recieved_data[1]
    else:
        return recieved_data[0]



def get_player_number(ghostmode):
    global p2_ghostmode
    player = 0
    client.send([0,ghostmode])
    x = client.receive(True)
    if x == [None,None]:
        player = 1
    else:
        player = 2
        if x == "duell":
            return (player,False)
    return  (player,True)
    
