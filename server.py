from socket import *
from os import listdir
from os.path import isfile
import urllib.parse

port = 8082

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    
    
    serversocket.bind(('localhost',port))
    serversocket.listen(5)
    while(1):
        try:
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])

            file_requested = rd.split(' ')[1][1:]                             # Captura somente a parte pós '/' que forma o nome do arquivo
            file_requested = urllib.parse.unquote(file_requested).strip(' ')  # Decodifica a codificação da url
            print(file_requested)

            if file_requested in filter(isfile, listdir()):                   # Compara o nome do arquivo pedido na url com os nomes dos arquivos no servidor
                data = "HTTP/1.1 200 OK\r\n"
                data += "Accept-Ranges: bytes\r\n\r\n"
                print('=========||' + 'Serving ' + file_requested + '||=========')  # Se estiver presente o arquivo é enviado
                clientsocket.sendall(data.encode('utf-8') + open('./' + file_requested, 'rb').read())
            else:
                data = "HTTP/1.1 404 Not Found\r\n"
                data += "Content-Type:; charset=utf-8\r\n\r\n"
                print('=========||' + 'Serving 404 Not Found' + '||=========')       # Caso contrário é servida uma página de erro 404
                clientsocket.sendall(data.encode('utf-8') + "<html><body><h1>404</h1><h4>Page not found</h4></body></html>\r\n\r\n".encode('utf-8'))
            
            clientsocket.close();
        except:
            continue
    
    serversocket.close()
    

print("Access http://localhost:" + str(port))
createServer()
