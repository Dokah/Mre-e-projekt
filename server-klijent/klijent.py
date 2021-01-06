import cv2
import pickle
import struct
import socket

clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect(('localhost',8000))
print("Spojeno na server!")

print("----------------------------------------------------")
print("Odaberite 1 za strujanje lokalno pohranjenog videa")
print("Odaberite 2 za strujanje uzivo!")
print("----------------------------------------------------")
odabir = int(input("Unesite broj opcije koju želite koristiti!: "))

if(odabir == 1):
    cap=cv2.VideoCapture('sample.mp4')
    while (cap.isOpened()):

        # Return (True ili false ako je okvir dostupan), uzmi jedan okvir
        ret,okvir=cap.read()
    
        # Serijalizacija okvira ((Pretvaranje objekta u tok bajtova))
        podaci = pickle.dumps(okvir)

        # Serijalizacija objekta koji sadrži veličinu naših podataka
        #L je unsigned long
        velicina_poruke = struct.pack("L", len(podaci)) 

        # Slanje veličine podataka i podatke
        clientSocket.sendall(velicina_poruke + podaci)
    
else:
    cap=cv2.VideoCapture(0)
    while (1):

        # Return (True ili false ako je okvir dostupan), uzmi jedan okvir
        ret,okvir=cap.read()

        
        # Serijalizacija okvira ((Pretvaranje objekta u tok bajtova))
        podaci = pickle.dumps(okvir)

        # Serijalizacija objekta koji sadrži veličinu naših podataka
        #L je unsigned long
        velicina_poruke = struct.pack("L", len(podaci)) 

        # Slanje veličine podataka i podatke
        clientSocket.sendall(velicina_poruke + podaci)
