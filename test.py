import time

address = '00:55:DA:B0:0B:30' #Address Muse

#Funcion para tomar los datos del EEG
def eeg(data,time):
	print "EEG:",data
  print "Time:",time
	


#Funcion para tomar los datos del ACC
def acc(data):
	print "Acc: ",data

#Funcion para tomar los datos del Gyro
def gyro(data):
	print "Gyro: ",data	
	
#Iniciamos Clase Muse
muse = Muse(address=direc,eeg=True,callback=eeg,acc_data=acc,accelero=True,giro=True,gyro_data=gyro)

print "muse Iniciado"
muse.connect()
print "muse Conectado"

muse.start()
print "Comienza captura de datos Muse"

# Creamos un Bucle infinito para que recolecte los datos
while True:
	try:
		time.sleep(1)
	except Exception,e:
		print e

muse.stop()
print "Muse stop"
muse.disconnect()
print "Muse Desconectado"
