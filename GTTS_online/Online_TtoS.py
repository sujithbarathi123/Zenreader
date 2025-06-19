# Thinkerdyne Technologies
# -----------------------------------------------------------------------------------
# pip install pytesseract
# pip install pillow
# pip install gTTS
# pip install pygame
# pip install google-cloud-texttospeech
# pip install playsound==1.2.2
# Tesseract OCR Download and install: https://github.com/tesseract-ocr/tesseract
#------------------------------------------------------------------------------------

from PIL import Image
from pytesseract import pytesseract
from gtts import gTTS
from tempfile import NamedTemporaryFile
import os

# Defining paths to Tesseract-OCR
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Defining paths to your image
# image_path = r"E:\ItoT_python\english.jpg"
image_path = r"E:\ItoT_python\kannada01.jpg"

# Opening the image & storing it in an image object
img = Image.open(image_path)

# Providing the Tesseract-OCR
# executable location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract

lang = 'eng+kan'  # e.g., English and Kannada

# extract the text from the image
# text = pytesseract.image_to_string(img)
text = pytesseract.image_to_string(img, lang=lang)

# Displaying the text
print(text)

# Specify the language for text-to-speech
# lang = 'en' 
lang = 'kn' 

# Converting the text to speech
tts = gTTS(text=text, lang=lang, tld='co.in')

def play_audio():
    # Create a named temp file and close it
    temp_file = NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_file_path = temp_file.name
    temp_file.close()  

    # Save audio and play
    tts.save(temp_file_path)
    os.system(f'start "" "{temp_file_path}"')  # For Windows

# tts.save("output.mp3")
# os.system("start output.mp3")

play_audio()

# ##########################################################################################################################################################################

# from PIL import Image
# from pytesseract import pytesseract
# from gtts import gTTS
# from tempfile import NamedTemporaryFile
# import pygame
# import time

# # Path to Tesseract-OCR
# pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # Path to image
# image_path = r"E:\ItoT_python\english.jpg"
# # image_path = r"E:\ItoT_python\kanBook.jpg"

# # Load image and OCR
# img = Image.open(image_path)
# text = pytesseract.image_to_string(img, lang='eng+kan')

# print("\n--- Extracted Text ---\n")
# print(text)

# lang = 'en'
# # lang = 'kn'
# # Convert to speech using gTTS
# tts = gTTS(text=text, lang=lang, tld='com')

# # Save to temp file and play fast with pygame
# def play_audio():
#     with NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
#         tts.save(temp_file.name)
#         audio_path = temp_file.name

#     pygame.init()
#     pygame.mixer.init()
#     pygame.mixer.music.load(audio_path)
#     pygame.mixer.music.play()

#     while pygame.mixer.music.get_busy():
#         time.sleep(0.1)

# play_audio()

