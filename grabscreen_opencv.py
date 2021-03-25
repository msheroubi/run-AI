import numpy as np
import cv2
from PIL import ImageGrab
import time

def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            return cv2.line(img,(coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 3)
    except:
        pass
           

#Get region of interest given an image and vertices
def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def auto_canny(image, sigma=0.33):
    #compute median
    v = np.median(image)

    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    return edged


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img,threshold1=100,threshold2=200)
    processed_img = cv2.GaussianBlur(processed_img, (3, 3), 0)

    kernel = np.ones((3,3),np.uint8)
    #processed_img = cv2.erode(processed_img,kernel,iterations = 1)

    #see ROI notes in notebook
    vertices = np.array([[100,400],[650,400],[488,200],[213,200]])
    processed_img = auto_canny(processed_img)
    processed_img = roi(processed_img, [vertices])
    
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 100,minLineLength,maxLineGap)

    newIm = np.zeros(processed_img.shape)
    try:
        for x1,y1,x2,y2 in lines[0]:
            cv2.line(newIm,(x1,y1),(x2,y2),(0,255,0),2)
    except:
        print("Type Err")

    return newIm

def main():
    last_time = time.time()
    while(True):
        screen = ImageGrab.grab(bbox=(0, 100, 750, 600)) #x, y, w , h)

        screen_np= np.array(screen)
        
        new_screen = process_img(screen_np)
        #print('Loop took {} seconds'.format(time.time() -last_time))
        last_time = time.time()
        try:
            cv2.imshow('window', new_screen)
        except:
            print("Imshow none error")

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
