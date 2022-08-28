def client():
    try:
        import socket
        c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        serverIP='127.0.0.1'#input("[+]Enter server IP you wont to connect: ")
        serverPort=1234#int(input("enter server port:"))
        c.connect((serverIP,serverPort))
        a=True
        while a:
            msgSend=input("enter message:> ")
            c.send(msgSend.encode())
            msg=c.recv(2048).decode()
            print("response:}>",msg)
            print("please wait for response.............")
            if msgSend == 'exit':
                c.close()
            elif msg == 'exit':
                c.close()
    except OSError:
        print(".................Program has been finished..client disconnect the network.............")
    except KeyboardInterrupt:
        print("keyboard interrupt error caught.")
    except ValueError:
        print("please enter proper value!!!!! or get some help.")
client()