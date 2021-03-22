import socket
f = open("URLsList.txt", "r")  # opening the file with the URLs
for line in f:  # reading the file line per line
    url = line.strip()  # parsing the URL that was read in a variable
    ip = socket.gethostbyname(url)  # getting the IP address of this URL

    print(ip)  # printing the IP
    # check if port is open on host
    socket.setdefaulttimeout(200)  # setting default timeout for our program
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating our socket object, which will help us to check for open ports
    try:
        for x in range(70, 90):  # checking the port range from port 70 to port 90
            port = x  # getting the port which we will want to test  into a variable
            result = socket_obj.connect_ex((ip, port))  # trying to make a connection to this port,
                                                        # will return 0 if port is open and 1 if port is closed

            if result == 0:  # if port is open
                print('open port detected:' + str(ip) + '\t-- Port:' + str(port))  # show a message to user that this specific port is open
                banner = socket_obj.recv(1024)  # making a banner grapping to gain information about the computer system
                print(banner)  # printing this returned informations
            else:  # if port is closed
                print('port ' + str(port) + ' closed..cannot connect')  # print a message to user to inform that this port is closed
    except socket.error as socketerror:  # if the default timeout ends
        print('Oops...there is no results')
