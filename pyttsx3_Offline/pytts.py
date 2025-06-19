# Thinkerdyne Technologies
# -----------------------------------------------------------------------------------
# pip install pytesseract
# pip install pillow
# pip install pyttsx3
# Tesseract OCR Download and install: https://github.com/tesseract-ocr/tesseract
#------------------------------------------------------------------------------------
from PIL import Image
from pytesseract import pytesseract
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# set voice male = 0 or female = 1
engine.setProperty('voice', engine.getProperty('voices')[1].id)

# Defining paths to Tesseract-OCR
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Defining paths to Image
image_path = r"E:\ItoT_python\english.jpg"

# Opening the image 
img = Image.open(image_path)


pytesseract.tesseract_cmd = path_to_tesseract

lang = 'eng+kan' # e.g., English and Kannada

# extract the text from the image
# text = pytesseract.image_to_string(img)
text = pytesseract.image_to_string(img, lang=lang)

# Displaying text
print(text)

# Set properties (optional)
engine.setProperty('rate', 150)     # Speed of words per minute
engine.setProperty('volume', 1.0)   # Volume

engine.say(text)

# Run the speech engine
engine.runAndWait()


