import datetime, threading,  socket
import os, serial, time, sys

# def readGPS():

while True:

    try:
        ComPort = serial.Serial("com5", 9600)
        print('Подключение к COM5 .... ')
        while True:
            ComData = ComPort.readline()
            GPSData = str(ComData.rstrip()).split(sep = ',')
            if 'GPRMC' in GPSData[0]:
                if GPSData[1] == '':
                    print('GPS модуль не может определить всемя и дату')
                else:
                    GPSTime = f'{GPSData[1][:2]}:{GPSData[1][2:4]}:{GPSData[1][4:6]}'
                    GPSDate = f'{GPSData[9][:2]}-{GPSData[9][2:4]}-{GPSData[9][4:6]}'
                    os.system("tzutil /s \"UTC\"")
                    os.system("date "+ GPSDate)
                    os.system("time " + GPSTime)
                    os.system("tzutil /s \"Russia Time Zone 3\"")
                    print(f'Данные от GPS модуля: дата: {GPSDate}, время: {GPSTime}')
                    print('Синхронизация с системой')
                break
        ComPort.close()
    except (OSError, serial.SerialException):
        print('Ошибка открытия COM5 ...')

    try:
        time.sleep(300)
    except KeyboardInterrupt:
        print('Окончание работы ...')
        sys.exit(0)

#    except KeyboardInterrupt:
#        print('Окончание работы ...')
#        break

"""
GPS = threading.Thread(target=readGPS)
GPS.start()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as GPSsocket:
    GPSsocket.bind(('192.168.0.10', 123))
    print('Сервер запушен: ip: 192.168.0.10, port: 123')
    while True:
        try:
            Data, UDPaddr = GPSsocket.recvfrom(48)
            print(f'Запрос синхронизации с {UDPaddr[0]}:{UDPaddr[1]}')
            print(len(Data))
            print(Data)
            Data = time.gmtime(time.time())
            Data = f'{Data.tm_mday}-{Data.tm_mon}-{Data.tm_year}  {Data.tm_hour}:{Data.tm_min}:{Data.tm_sec}'
            GPSsocket.sendto(Data.encode('utf-8'), UDPaddr)

        except KeyboardInterrupt:
            print('Окончание работы ...')
            GPS.join()
            break
"""

