import asrtoolkit
from asrtoolkit import wer, cer
import numpy as np
import pytesseract
from rapidfuzz import fuzz
from skimage import io
import skimage.io
from skimage.transform import rotate
import cv2

from deskew import determine_skew

def deskew_process(image):
    image = io.imread(image)
    grayscale = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    angle = determine_skew(grayscale)
    rotated = rotate(image, angle, resize=True) * 255
    return rotated


image_deskew = deskew_process("img_3.png")
# save the rotated image to a imagae .png file
io.imsave("output_deskewed.png", image_deskew.astype(np.uint8))


def pre_process_image(image):
    """This function will pre-process a image with: cv2 & deskew
    so it can be process by tesseract"""
    img = cv2.imread(image)
    img = cv2.resize(img, None, fx=.3, fy=.3)  # resize using percentage
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # change color format from BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # format image to gray scale
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5,
                                11)  # to remove background
    return img


# pass the deskew image
processed_img = pre_process_image("output_deskewed.png")
# save the processed image to a imagae .png file
cv2.imwrite("output_processed.png", processed_img)



ground_truth = """xin CHAO"""

hypothesis = pytesseract.image_to_string("output_deskewed.png")
print("CER, WER, Rate :",cer(ground_truth, hypothesis),wer(ground_truth, hypothesis),fuzz.ratio(ground_truth, hypothesis))
print(hypothesis)




