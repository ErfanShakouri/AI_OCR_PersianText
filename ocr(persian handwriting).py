!apt install tesseract-ocr -y
!apt install tesseract-ocr-fas -y
!pip install pytesseract
!pip install easyocr
# Import required libraries
import pytesseract  # Tesseract OCR library
import easyocr      # EasyOCR library for multilingual OCR
from PIL import Image  # For image loading

class OCRProcessor:
    def __init__(self):
        # Initialize the EasyOCR reader for Persian language
        self.easy_reader = easyocr.Reader(['fa'])

    def ocr_with_tesseract(self, img_path):
        """
        Perform OCR on a Persian text image using Tesseract
        """
        try:
            img = Image.open(img_path)  # Load the image
            text = pytesseract.image_to_string(img, lang='fas')  # Extract text with Persian language model
            return text.strip()
        except Exception as e:
            return f"[Tesseract Error] {str(e)}"

    def ocr_with_easyocr(self, img_path):
        """
        Perform OCR on a Persian text image using EasyOCR
        """
        try:
            results = self.easy_reader.readtext(img_path)  # Read text with bounding boxes
            extracted_text = "\n".join([res[1] for res in results])  # Extract just the text content
            return extracted_text.strip()
        except Exception as e:
            return f"[EasyOCR Error] {str(e)}"


# Instantiate the OCR processor
ocr = OCRProcessor()

# Path to Persian text image
img_path_fa = "/content/sample_data/ocr_fa1.jpg"

# OCR using Tesseract
text_tesseract = ocr.ocr_with_tesseract(img_path_fa)
print("Text with Tesseract:\n", text_tesseract)

# OCR using EasyOCR
text_easyocr = ocr.ocr_with_easyocr(img_path_fa)
print("\nText with EasyOCR:\n", text_easyocr)
