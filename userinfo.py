import socket

# IRC server and channel
server = "irc.freenode.net"
channel = "#mychannel"

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to IRC server
sock.connect((server, 6667))

# Send login information
sock.sendall(b"USER myuser myuser myuser myuser\n")
sock.sendall(b"NICK mynick\n")

# Join channel
sock.sendall(f"JOIN {channel}\n".encode())

# Send message to channel
sock.sendall(f"PRIVMSG {channel} :Hello, World!\n".encode())

# Disconnect from server
sock.sendall(b"QUIT\n")

# Close socket
sock.close()
