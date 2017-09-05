import socket, os, pickle, re, sys

HOST = "localhost"
PORT = 1604


result_dict = {}

result_dict['next']= 'next'

conn=socket.socket(socket.AF_INET)
conn.connect((HOST,PORT))
conn.send(pickle.dumps(result_dict))
response = conn.recv(1024)
#uresponse= response.decode("UTF-8")
print (response)



conn.close()
