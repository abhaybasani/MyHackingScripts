def server():
    try:
        import socket
        print("Loading msg from client....../.....")
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientIP='127.0.0.1'#input("[+]Enter client IP: ")
        open_port=1234#int(input("[+]Enter port: "))
        s.bind((clientIP,open_port))
        limit_of_connection=5#int(input("[+]Enter limit of connection: "))
        s.listen(limit_of_connection)
        client,address=s.accept()
        print("[/]This is address of client:> ",address)
        a=True
        while a:
            msg=client.recv(2048).decode()
            print(f"{address}:>",msg)
            sendmsg=input("enter msg:>")
            print("please wait for client respond!.............")
            client.send(sendmsg.encode())
            if msg == 'exit':
                client.close()
                s.close()
            if sendmsg == 'exit':
                client.close()
                s.close()
    except OSError:
        print(".................Program has been finished...client disconnect the network.............")
    except KeyboardInterrupt:
        print("keyboard interrupt error caught.")
    except ValueError:
        print("please enter proper value!!!!! or get some help.")
server()