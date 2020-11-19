from socket import *
import os

port = 9028

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    
    try:
        serversocket.bind(('localhost',port))
        serversocket.listen(5)
        BUFFER_SIZE = 4096 # send 4096 bytes each time step
        
        while(1):
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])

            file_requested = rd.split(' ')[1]
            if file_requested == "/":
                # data = "HTTP/1.1 200 OK\r\n"
                # data += "Content-Type: text/html; charset=utf-8\r\n"
                # data += "\r\n"
                # data += "<html><body><h1>Hello World</h1></body></html>\r\n\r\n"
                # print("Server Working: Root")
                
                # Tentativa de jogar um arquivo
                # filename = "index.html"
                # file = open(filename, "r")
                # data = file.read()
                # print(data)

                data = "HTTP/1.1 200 OK\r\n"
                data += "Content-Type: application/octet-stream; \r\n"
                data += "\r\n"
                data += open("./file.txt", encoding="ISO-8859-1").read()
                # data += "<html><body><h1>Hello World</h1></body></html>\r\n\r\n"
                # print("Server Working: Root")

            elif file_requested == "/professor":
                data = "HTTP/1.1 200 OK\r\n"
                data += "Content-Type: text/html; charset=utf-8\r\n"
                data += "\r\n"
                data += "<html><body><h1>Andson Marreiros Balieiro</h1></body></html>\r\n\r\n"
                # print("Server Working: Professor")

            elif file_requested == "/monitor":
                data = "HTTP/1.1 200 OK\r\n"
                data += "Content-Type: text/html; charset=utf-8\r\n"
                data += "\r\n"
                data += "<html><body><h1>Dario</h1></body></html>\r\n\r\n"
                # print("Server Working: Monitor")

            else:
                data = "HTTP/1.1 404 page not found\r\n"
                data += "Content-Type: text/html; charset=utf-8\r\n"
                data += "\r\n"
                data += "<html><body><h1>404</h1><h4>Page not found</h4></body></html>\r\n\r\n"
                # print("File not found. Serving 404 page.")
            
            clientsocket.send(data.encode())
            clientsocket.close()
            

    except KeyboardInterrupt :
        clientsocket.shutdown(SHUT_WR)

    serversocket.close()

print("Access http://localhost:" + str(port))
createServer()
