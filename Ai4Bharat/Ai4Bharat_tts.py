from pytesseract import pytesseract
from PIL import Image
from TTS.utils.synthesizer import Synthesizer

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Image OCR
img_path = r"E:\indic_tts\Indic-TTS-master\english.jpg"
img = Image.open(img_path)
pytesseract.tesseract_cmd = path_to_tesseract

lang="eng+kan"

text = pytesseract.image_to_string(img, lang=lang)

print(text)

# Paths to model files
fastpitch_model_path = "models/v1/en/fastpitch/best_model.pth"
fastpitch_config_path = "models/v1/en/fastpitch/config.json"
hifigan_model_path = "models/v1/en/hifigan/best_model.pth"
hifigan_config_path = "models/v1/en/hifigan/config.json"

# Initialize synthesizer
synthesizer = Synthesizer(
    tts_checkpoint=fastpitch_model_path,
    tts_config_path=fastpitch_config_path,
    vocoder_checkpoint=hifigan_model_path,
    vocoder_config=hifigan_config_path,
    use_cuda=False
)

# Print speaker names (this works!)
print("Available speakers:", synthesizer.tts_model.speaker_manager.speaker_names)

# Use a valid speaker name from above list
wav = synthesizer.tts(text, speaker_name="female")  # or "male", etc.

# Save the output
synthesizer.save_wav(wav, "output.wav")
print("Audio saved to output.wav")

###########################################################################################################################################

# from pytesseract import pytesseract
# from PIL import Image
# from TTS.utils.synthesizer import Synthesizer

# path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # Image OCR
# img_path = r"E:\indic_tts\Indic-TTS-master\kannada01.jpg"
# img = Image.open(img_path)
# pytesseract.tesseract_cmd = path_to_tesseract

# lang="eng+kan"

# text = pytesseract.image_to_string(img, lang=lang)

# print(text)

# # Paths to model files
# fastpitch_model_path = "models/v1/kn/fastpitch/best_model.pth"
# fastpitch_config_path = "models/v1/kn/fastpitch/config.json"
# hifigan_model_path = "models/v1/kn/hifigan/best_model.pth"
# hifigan_config_path = "models/v1/kn/hifigan/config.json"

# # Initialize synthesizer
# synthesizer = Synthesizer(
#     tts_checkpoint=fastpitch_model_path,
#     tts_config_path=fastpitch_config_path,
#     vocoder_checkpoint=hifigan_model_path,
#     vocoder_config=hifigan_config_path,
#     use_cuda=False
# )

# # Print speaker names (this works!)
# print("Available speakers:", synthesizer.tts_model.speaker_manager.speaker_names)

# # Use a valid speaker name from above list
# wav = synthesizer.tts(text, speaker_name="female")  # or "male", etc.

# # Save the output
# synthesizer.save_wav(wav, "output.wav")
# print("Audio saved to output.wav")

