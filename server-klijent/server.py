import struct
import cv2
import pickle
import socket

HOST = '127.0.0.1'
PORT = 8000

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket stvoren!')

socketServer.bind((HOST, PORT))
print('Socket povezan na: '+str(HOST)+' : '+str(PORT))

socketServer.listen(10) #može biti 10 neprihvaćenih konekcija prije nego prestane prihvaćati konekcije
print('Slušam!')

konekcija, adresaKlijenta = socketServer.accept() #vraća objekt konekcije i adresu s koje dolazi

podaci = b'' #neka data bude tipa bajtova
velicina_tereta = struct.calcsize("L") #velicina tereta koja je velicine structa tipa unsigned long

while True:

    # Dohvati veličinu poruke
    while len(podaci) < velicina_tereta:
        podaci += konekcija.recv(4096)
    
    #Parsiraj veličinu poruke
    zapakirana_velicina_poruke = podaci[:velicina_tereta] #zapakirana velicina poruke je početak iz podataka veličine tereta
    podaci = podaci[velicina_tereta:] #podaci se postavljaju na mjesto nakon zapakirane veličine poruke
    velicina_poruke = struct.unpack("L", zapakirana_velicina_poruke)[0] #unpack vraća n-torku pa zato mora biti [0] taman da je i jedan response
 
    # Dohvati sve podatke na temelju veličine poruke
    while len(podaci) < velicina_poruke:
        podaci += konekcija.recv(32768)

    #Parsiraj podatke
    podaci_okvira = podaci[:velicina_poruke] #Podaci okvira se nalaze na početku podataka veličine poruke
    podaci = podaci[velicina_poruke:] #Podatke postavljamo na mjesto iza veličine poruke

    # Izdvoji okvir
    okvir = pickle.loads(podaci_okvira) #Odserijaliziraj niz bajtova u vektorsku sliku

    # Prikaz
    cv2.imshow('okvir', okvir)
    cv2.waitKey(1)
