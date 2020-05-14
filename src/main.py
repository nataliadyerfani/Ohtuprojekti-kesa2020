# image downloaded from: https://www.apa.org/monitor/2020/04/nurtured-nature
# code from https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#goals

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Module to experiment with tests
from module_totest import calculate_sum

def show_image():
    '''
    Load and convert an image from disk to grayscale. draw a line and show the result. OpenCV with pyplot
    '''
    img = cv2.imread('nature.png', cv2.IMREAD_GRAYSCALE)
    #cv2.imshow('image', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
    plt.show()

    #cv2.imwrite('naturegray.png', img) #save image

def show_video():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read() #ret is boolean indicating if we have any image returned, will be None if no image is returned
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # convert frame to grayscale. Opencv uses BGR-colors as oposed to RGB

        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def record_video():
    '''
    Show video and also save as xvid-encoded
    '''
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame) #in colors
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def read_img():
    '''
    OpenCV
    '''
    img = cv2.imread('nature.png', cv2.IMREAD_COLOR)

    #x,y, start coords, end coords, color (bgr), line thickness
    cv2.line(img, (0,0), (130,130), (255,255,255), 10)

    #top left, bottom right
    cv2.rectangle(img, (135,45), (230,130), (0,255,0), 5)
    #center of circle, radius, color and linewidth, negative fills the circle
    cv2.circle(img, (350,250), 55, (0,0,255), -1)
    
    # Polygons
    # List of points
    #pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
    pts = np.array([[50,30], [150,30], [100,90]], np.int32)
    #pts = pts.reshape((-1,1,2)) # correct shape of points array
    cv2.polylines(img, [pts], True, (0,255,255),3)
    
    #Writing text
    font = cv2.FONT_HERSHEY_SIMPLEX
    #place, size, color, text thickness, antialiazing
    cv2.putText(img, 'OpenCV testing', (0,130), font, 3, (200,255,255), 2, cv2.LINE_AA)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # exit all methods with pressing q
    # show_image()
    #show_video()
    #record_video()
    #read_img()

    
    print(calculate_sum([1,2,3]))

if __name__ == '__main__':
    main()
