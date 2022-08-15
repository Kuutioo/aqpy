import numpy as nm

import pytesseract
import time
import cv2

from PIL import ImageGrab

def im_to_string():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    
    
    cap = ImageGrab.grab(bbox=None)
        
    tesstr = pytesseract.image_to_string(cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), lang='eng')
    time.sleep(1)
    print(tesstr)
        
im_to_string()