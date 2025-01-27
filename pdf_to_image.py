import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import os
import shutil
from pdf2image import convert_from_path

class ImageProcessor:
    def __init__(self, poppler_path, input_folder, output_folder):
        """
        Initializes the ImageProcessor with paths for Poppler, input, and output folders.
        """
        self.poppler_path = poppler_path
        self.input_folder = input_folder
        self.output_folder = output_folder
        
        # Ensure output folder exists
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        
        # Define supported image file extensions
        self.image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')

    def process_pdfs(self):
        """
        Converts PDF files from the input folder to images and saves them in the output folder.
        """
        for filename in os.listdir(self.input_folder):
            file_path = os.path.join(self.input_folder, filename)

            if filename.lower().endswith(".pdf"):
                # Convert the PDF to images
                pages = convert_from_path(file_path, dpi=300, poppler_path=self.poppler_path)

                # Save each page as an image in the output folder
                for i, page in enumerate(pages):
                    output_image_path = os.path.join(self.output_folder, f"{os.path.splitext(filename)[0]}_page_{i+1}.jpg")
                    page.save(output_image_path, 'JPEG')

                print(f"Processed PDF: {filename}")

    def copy_images(self):
        """
        Copies image files from the input folder to the output folder.
        """
        for filename in os.listdir(self.input_folder):
            file_path = os.path.join(self.input_folder, filename)

            if filename.lower().endswith(self.image_extensions):
                # If it's an image file, copy it to the output folder
                output_image_path = os.path.join(self.output_folder, filename)
                shutil.copy(file_path, output_image_path)

                print(f"Copied image: {filename}")

    def process_all_files(self):
        """
        Processes both PDF and image files from the input folder.
        """
        self.process_pdfs()
        self.copy_images()
        print("All PDFs and image files have been processed.")

# Example usage:
poppler_path = r"C:\Program Files\poppler-24.08.0\Library\bin"  # Adjust this path for your system
input_folder = r'upload_files'
output_folder = r'output_images'

image_processor = ImageProcessor(poppler_path, input_folder, output_folder)
image_processor.process_all_files()
