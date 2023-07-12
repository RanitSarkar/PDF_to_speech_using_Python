import PyPDF2
from gtts import gTTS
import os

def pdf_to_speech(pdf_path):
    # Open the PDF file in read binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        # Initialize an empty string to store the extracted text
        extracted_text = ''

        # Iterate over each page in the PDF and extract the text
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            extracted_text += page.extract_text()

        # Create a gTTS object and specify the language
        tts = gTTS(text=extracted_text, lang='en')

        # Save the speech as an MP3 file
        tts.save('output.mp3')

        # Play the audio file
        os.system('start output.mp3')

# Provide the path to your PDF file
pdf_file_path = 'path_to_your_pdf_file.pdf'

# Convert the PDF to speech
pdf_to_speech(pdf_file_path)
