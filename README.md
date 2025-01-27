# ImageProcessor
## Description of the Code:
This code defines a Python class ImageProcessor that automates the process of converting PDF files to images, copying images from an input folder to an output folder, and managing various image and PDF file operations. It integrates several libraries to achieve these # # tasks:

##pytesseract: 
A Python wrapper for Tesseract, an OCR engine for recognizing text in images (though it is not explicitly used in this code).
##pdf2image:
A library that converts PDF files to image files.
##shutil:
A module used for high-level file operations like copying files.
##os: 
A module that provides functions for interacting with the operating system, including file path management.
Breakdown of the Code:
# Imports:

pytesseract.pytesseract.tesseract_cmd: Specifies the path to the Tesseract executable (used for OCR).
##os:
Provides functions for interacting with the filesystem.
##shutil: 
Used to copy files.
##convert_from_path from pdf2image: 
Converts PDF pages into images.
# Class Definition: 
##ImageProcessor:

###__init__ Method:

Initializes the ImageProcessor class with paths for Poppler, input folder, and output folder.
Creates the output folder if it does not exist.
Defines valid image file extensions (.jpg, .jpeg, .png, .bmp, .gif, .tiff).
##process_pdfs Method:

Loops through all files in the input folder, identifying PDF files based on their extension.
Uses the convert_from_path function to convert each page of the PDF into an image (using the Poppler library for PDF rendering).
Saves each page as a separate image (in JPEG format) in the output folder, naming the files based on the original PDF name and page number.
##copy_images Method:

Loops through all files in the input folder, identifying image files based on the predefined image extensions.
Copies each image file from the input folder to the output folder, maintaining the original filename.
##process_all_files Method:

Calls both process_pdfs and copy_images methods to process all PDF and image files in the input folder.
Prints a message indicating the completion of processing.
##Example Usage:

The paths for Poppler, input folder, and output folder are set.
An instance of ImageProcessor is created with these paths.
The process_all_files() method is called to execute the file processing.
# Key Steps in the Workflow:
##Convert PDFs to Images:
If a PDF file is found in the input folder, it is converted into images (one per page) and saved in the output folder.
Copy Image Files: Any image files (JPG, PNG, etc.) found in the input folder are copied to the output folder.
Process All Files: The process_all_files() method orchestrates the entire process, converting PDFs and copying images in one go.
# Example Output:
If a PDF file named document.pdf is found, it will be converted into individual images, such as document_page_1.jpg, document_page_2.jpg, and so on.
Any image files in the input folder (e.g., photo.jpg) will be copied directly to the output folder with the same filename.
# Purpose:
This class is useful for automating the processing of a folder containing both PDFs and image files. It’s especially helpful for converting PDFs into image formats for further processing (e.g., OCR, image analysis) and organizing image files in one location.
