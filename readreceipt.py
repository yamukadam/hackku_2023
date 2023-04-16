import pytesseract
import cv2

class ConvertImage:
    def __init__(self,image):
        self.image = image

    def return_text(self):
        img = cv2.imread(self.image)
        text = pytesseract.image_to_string(img)
        return text
