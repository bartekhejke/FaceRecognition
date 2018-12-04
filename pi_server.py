import konf
from socket import *
from time import ctime
import generate
import cv2
import io
from time import sleep
import picamera
import errno

ctrCmd = ['generuj','rozpoznawaj']

HOST = ''
PORT = 21578
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
#tcpSerSock.listen(5)

def image()
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        # Construct a stream to hold the image data and read the image
        # data from the connection
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        # Rewind the stream, open it as an image with PIL and do some
        # processing on it
        image_stream.seek(0)
        image = np.array(Image.open(image_stream))
        #print('Image is %dx%d' % image.size)
        image.verify()
        print('Image is verified')

while True:
	tcpSerSock.listen(5)
        print 'Waiting for connection'
        tcpCliSock,addr = tcpSerSock.accept()
        print '...connected from :', addr
        try:
                while True:
                        data = []
                        data = tcpCliSock.recv(BUFSIZE)
			data = data.split()
                        if not data:
                                break
                        if data[0] == ctrCmd[1]:
				print"Zaczynam rozpoznawanie"
				while True:
                                        try:
                                                image()
                                                algwyb = data [2]
                                                y=aglorytmy.Id
                                                with picamera.PiCamera() as camera:
                                                	camera.resolution = (test_rozp.CAMERA_WIDTH, test_rozp.CAMERA_HEIGHT)				
                                                	try:
                                                        	while(True):
                                                                        if (algwyb=1)
                                                                                import detector_eigen_gornoprzepustowy
                                                                                detector_eigen_gornoprzepustowy.main(y,camera)
                                                                                x=detector_eigen_gornoprzepustowy.main(y,camera)
                                                                                nazwa=detector_eigen_gornoprzepustowy.getProfile(x)
                                                                                print(nazwa)
                                                                                print(nazwa[1])
                                                                                tcpCliSock.send(nazwa[1])
                                                                        if (algwyb=2)
                                                                                import detector_eigen_median
                                                                                detector_eigen_median.main(y,camera)
                                                                                x=detector_eigen_median.main(y,camera)
                                                                                nazwa=detector_eigen_median.getProfile(x)
                                                                                print(nazwa)
                                                                                print(nazwa[1])
                                                                                tcpCliSock.send(nazwa[1])
                                                                        if (algwyb=3)
                                                                                import detector_eigen_sobel
                                                                                detector_eigen_sobel.main(y,camera)
                                                                                x=detector_eigen_sobel.main(y,camera)
                                                                                nazwa=detector_eigen_sobel.getProfile(x)
                                                                                print(nazwa)
                                                                                print(nazwa[1])
                                                                                tcpCliSock.send(nazwa[1])
                                                                        if (algwyb=4)
                                                                                import detector_eigen_laplacea
                                                                                detector_eigen_laplacea.main(y,camera)
                                                                                x=detector_eigen_laplacea.main(y,camera)
                                                                                nazwa=detector_eigen_laplacea.getProfile(x)
                                                                                print(nazwa)
                                                                                print(nazwa[1])
                                                                                tcpCliSock.send(nazwa[1])
                                                                        if (algwyb=5)
                                                                                import detector_fisher_gornoprzepustowy
                                                                                detector_fisher_gornoprzepustowy.main(y,camera)
                                                                                x=detector_fisher_gornoprzepustowy.main(y,camera)
                                                                                nazwa=detector_fisher_gornoprzepustowy.getProfile(x)
                                                                                print(nazwa)
                                                                                print(nazwa[1])
                                                                                tcpCliSock.send(nazwa[1])
                                                                        if (algwyb=6)
                                                                                import detector_fisher_median
                                                                                detector_fisher_median.main(y,camera)
                                                                                x=detector_fisher_median.main(y,camera)
                                                                                nazwa=detector_fisher_median.getProfile(x)
                                                                                print(nazwa)
                                                                                print(nazwa[1])
                                                                                tcpCliSock.send(nazwa[1])
                                                                        if (algwyb=7)
                                                                                import detector_fisher_sobel
                                                                                detector_fisher_sobel.main(y,camera)
                                                                                x=detector_fisher_sobel.main(y,camera)
                                                                                nazwa=detector_fisher_sobel.getProfile(x)
                                                                                print(nazwa)
                                                                                print(nazwa[1])
                                                                                tcpCliSock.send(nazwa[1])
                                                                        if (algwyb=8)
                                                                                import detector_fisher_laplacea
                                                                                detector_fisher_laplacea.main(y,camera)
                                                                                x=detector_fisher_laplacea.main(y,camera)
                                                                                nazwa=detector_fisher_laplacea.getProfile(x)
                                                                                print(nazwa)
                                                                                print(nazwa[1])
                                                                                tcpCliSock.send(nazwa[1])
                                                                        if (algwyb=9)
                                                                                import detector_lbph_gornoprzepustowy
                                                                                detector_lbph_gornoprzepustowy.main(y,camera)
                                                                                x=detector_lbph_gornoprzepustowy.main(y,camera)
                                                                                nazwa=detector_lbph_gornoprzepustowy.getProfile(x)
                                                                                print(nazwa)
                                                                                print(nazwa[1])
                                                                                tcpCliSock.send(nazwa[1])
                                                                        if (algwyb=10)
                                                                                import detector_lbph_median
                                                                                detector_lbph_median.main(y,camera)
                                                                                x=detector_lbph_median.main(y,camera)
                                                                                nazwa=detector_lbph_median.getProfile(x)
                                                                                print(nazwa)
                                                                                print(nazwa[1])
                                                                                tcpCliSock.send(nazwa[1])
                                                                        if (algwyb=11)
                                                                                import detector_lbph_sobel
                                                                                detector_lbph_sobel.main(y,camera)
                                                                                x=detector_lbph_sobel.main(y,camera)
                                                                                nazwa=detector_lbph_sobel.getProfile(x)
                                                                                print(nazwa)
                                                                                print(nazwa[1])
                                                                                tcpCliSock.send(nazwa[1])
                                                                        if (algwyb=12)
                                                                                import detector_lbph_laplacea
                                                                                detector_lbph_laplacea.main(y,camera)
                                                                                x=detector_lbph_laplacea.main(y,camera)
                                                                                nazwa=detector_lbph_laplacea.getProfile(x)
                                                                                print(nazwa)
                                                                                print(nazwa[1])
                                                                                tcpCliSock.send(nazwa[1])
						
                                                        except KeyboardInterrupt:
                                                                pass
                                                        except InterruptedError:
                                                                pass	
									
                                        if data[0] == ctrCmd[0]:
                                                generate.insertOrUpdate(data[3],data[1],data[2])
                                                generate.main(data[3])
                                                tcpCliSock.send(generate.inf)
                                                import trainer
                                                trainer.main()
                                                tcpCliSock.send(trainer.inf)
                                                print 'Tworzenie bazy'
        except KeyboardInterrupt:
                detector.close()
                GPIO.cleanup()
tcpSerSock.close();

