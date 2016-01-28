from Mastermind import *

server_ip = 'localhost'
port = 42042

connected_clients = 0

class ServerGame(MastermindServerTCP):
    def __init__(self):
        MastermindServerTCP.__init__(self, 0.5,0.5,30.0) #Server refresh, Connection refresh, Connection timeout

        #Grunddaten
        self.data_Player1 = None  # Data ist jetzt ein 3er Tupel mit Links/Rechts pos, Koords und erschaffener Kugel
        self.data_Player2 = None
        self.data_to_send = [None,None] # Liste der Tupel


        #Für die Objekte
        self.stuff_data_Player1 = None
        self.stuff_data_Player2 = None
        self.stuff_data_to_send = [None,None]
        
    def callback_client_handle(self, connection_object,data):
        if data[0] == 0: # Verbindungsaufbau, Spielerzuweisung
            self.callback_client_send(connection_object, self.data_to_send)
            
        elif data[0] == -42: # Objektabgleich im Spiel
            if data[1] == 1:
                self.stuff_data_Player1 = None
                self.stuff_data_to_send[0] = self.stuff_data_Player1
            else:
                self.stuff_data_Player2 = None
                self.stuff_data_to_send[1] = self.stuff_data_Player2
            self.callback_client_send(connection_object, self.stuff_data_to_send)
            
        else: # Datenaustausch im Spiel
            if data[0] == 1:
                self.data_Player1 = (data[1],data[2],data[3])
                self.data_to_send[0] = self.data_Player1
            else:
                self.data_Player2 = (data[1],data[2],data[3])
                self.data_to_send[1] = self.data_Player2
            self.callback_client_send(connection_object, self.data_to_send)
        
    def callback_connect_client(self,connection_object):
        global connected_clients
        #print ("A new client connected!")
        connected_clients += 1
        return super(MastermindServerTCP,self).callback_connect_client(connection_object)
    
    def callback_disconnect_client(self,connection_object):
        global connected_clients
        #print("the client disconnected!")
        connected_clients -= 1
        if connected_clients == 0:
            self.data_Player1 = None
            self.data_Player2 = None
            self.data_to_send = [None,None] 
        return super(MastermindServerTCP,self).callback_disconnect_client(connection_object)


if __name__ == "__main__":
    server = ServerGame()
    server.connect(server_ip,port)
    try:
        server.accepting_allow_wait_forever()
    except:
        pass
    server.disconnect_clients()
    server.disconnect()
