import pytesseract
import cv2
from PIL import Image

# delare the tesseract exectuable path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# load the image and convert it into grayscale
img_to_ocr = cv2.imread('Testing\\7.jpg')

# Step1: Convert into Gray
preprocessed_img = cv2.cvtColor(img_to_ocr, cv2.COLOR_BGR2GRAY)
# Step2: Do Binary and Thresholding
preprocessed_img = cv2.threshold(preprocessed_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[
    1]  # index 1 is used to avoid error in step 3

# Step3: Median Blur to remove noise in the image
preprocessed_img = cv2.medianBlur(preprocessed_img, 3)

# Save the preprocessed image and convert into PIL image
cv2.imwrite('img.jpg', preprocessed_img)

# load the image as a PIL image
preprocessed_img = Image.open('img.jpg')

# Do OCR Tesseract
text_extracted = pytesseract.image_to_string(Image.open('img.jpg'))

# Print Extracted Text
print(text_extracted)

# Display the original image
cv2.imshow('Image', img_to_ocr)
cv2.waitKey(0)
