import fitz
import docx

from PIL import Image
import pytesseract
import os


class FileDataExtractor:

    def __init__(self):
        super().__init__()

    def extract_text_payload(self, file, file_path):

        ret = {'hash': '', 'payload': {'fileName': file, 'filePath': file_path, 'doc': '', 'type': 'unknown'}}
        if file.lower().endswith('.pdf'):
            #print(f"Reading PDF file: {file_path}")
            text = self.read_pdf(file_path)
            if text:
                hashed_val = hash(text[:1000])
                ret = {'hash': hashed_val,
                       'payload': {'fileName': file, 'filePath': file_path, 'doc': text, 'type': 'pdf'}}

        elif file.lower().endswith('.docx'):
            #print(f"Reading DOCX file: {file_path}")
            text = self.read_docx(file_path)
            if text:
                hashed_val = hash(text[:1000])
                ret = {'hash': hashed_val,
                       'payload': {'fileName': file, 'filePath': file_path, 'doc': text, 'type': 'docx'}}

        elif file.lower().endswith('.txt'):
            #print(f"Reading text file: {file_path}")
            text = self.read_txt(file_path)
            if text:
                hashed_val = hash(text[:1000])  # Print first 1000 characters of the content
                ret = {'hash': hashed_val,
                       'payload': {'fileName': file, 'filePath': file_path, 'doc': text, 'type': 'txt'}}

        elif file.lower().endswith('.jpg') or file.lower().endswith('.jpeg') or file.lower().endswith('.png'):
            #print(f"Reading image file file: {file_path}")
            file_extension = os.path.splitext(file_path)[1].lower()
            text = self.read_text_from_image(file_path)
            if text:
                hashed_val = hash(text[:1000])  # Print first 1000 characters of the content
                ret = {'hash': hashed_val,
                       'payload': {'fileName': file, 'filePath': file_path, 'doc': text, 'type': file_extension}}

        else:
            pass
            #print(f"Unknown  file: {file_path}")
        return ret

    def read_text_from_image(self, image_path, tesseract_cmd=None):
        # Set the tesseract command if provided (useful for Windows if tesseract is not in PATH)
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

        try:
            # Open the image file
            img = Image.open(image_path)

            # Use pytesseract to do OCR on the image
            text = pytesseract.image_to_string(img)

            return text
        except Exception as e:
            print(f"Error reading text from image {image_path}: {e}")
            return None

    def read_pdf(self, file_path):
        try:
            document = fitz.open(file_path)
            text = ""
            for page_num in range(len(document)):
                page = document.load_page(page_num)
                text += page.get_text()
            document.close()
            return text
        except Exception as e:
            print(f"Error reading PDF file {file_path}: {e}")
            return None

    def read_txt(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return None

    def read_docx(self, file_path):
        try:
            document = docx.Document(file_path)
            text = "\n".join([para.text for para in document.paragraphs])
            return text
        except Exception as e:
            print(f"Error reading DOCX file {file_path}: {e}")
            return None
