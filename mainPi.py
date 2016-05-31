import cv2
from classes import frameAnalyzer
import time
from classes.capture import capture
from classes.PiVideoStream import PiVideoStream

def run_program():

	# initialize the camera and grab a reference to the raw camera capture
	camera = PiVideoStream().start()
	# allow the camera to warm up
	time.sleep(2.0)

	cap = capture(640, 480)

	# run cardigan proccesses
	try:
		while True:
			# load frame from camera
			frame = camera.read()

			# start record
			cap.captureFrame(frame)

			# Start ADAS process
			frameAnalyzer.analyze_frame(frame, True, True, True)


	except KeyboardInterrupt:
		print "\nattempting to close."
		camera.stop()
		print "\nBye Bye ;-)"



	camera.stop();

if __name__ == '__main__':
	run_program()