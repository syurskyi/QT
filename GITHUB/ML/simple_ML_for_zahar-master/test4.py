import cv2
import time
import numpy as np
import imutils
import serial

radius = None
bp = 0
camera = cv2.VideoCapture(0)
colorLower = (70, 100, 100)
colorUpper = (120, 255, 255)
last_command = None


def forward(port):
    port.write("1\r\n".encode())


def left(port):
    port.write("3\r\n".encode())


def right(port):
    port.write("2\r\n".encode())


def stop(port):
    port.write("4\r\n".encode())


def backward(port):
    pass


ser = serial.Serial("/dev/ttyACM0", baudrate=9600)
while True:
    (grabbed, frame) = camera.read()
    frame = imutils.resize(frame, width=600)
    output = frame.copy()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, colorLower, colorUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    output = cv2.bitwise_and(output, output, mask=mask)
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 3, 500, minRadius=10, maxRadius=160, param1=100, param2=60)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, radius) in circles:

            cv2.circle(output, (x, y), radius, (0, 255, 0), 4)
            if radius > 10:
                bp = x
            else:
                bp = 0
    else:
        bp = 0

    if bp == 0 or radius > 100:
        if last_command != stop:
            stop(ser)
            time.sleep(0.05)
            last_command = stop
    else:
        if bp < 150:
            if last_command != left:
                left(ser)
                time.sleep(0.05)
                last_command = left
        elif bp > 450:
            if last_command != right:
                right(ser)
                time.sleep(0.05)
                last_command = right
        else:
            if last_command != forward:
                forward(ser)
                time.sleep(0.05)
                last_command = forward
        if radius is not None:
            print("radius = {}".format(radius))

    cv2.imshow("123", output)
    if cv2.waitKey(1) == ord("q"):
        break
stop(ser)
cv2.destroyAllWindows()
camera.release()
