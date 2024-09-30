# TextVision OCR Project

## Overview

TextVision is a web-based Optical Character Recognition (OCR) application that extracts text from images containing both Hindi and English text. The application also supports keyword search functionality to highlight specific words within the extracted text. It is built with a simple, intuitive interface and supports five languages: Hindi, English, Spanish, French, and Punjabi.

This project was developed as part of an assignment for a job application.

Live Demo: https://huggingface.co/spaces/Prabhjotschugh/OCR-TextVision

## Features

- **Image Upload**: Upload an image and extract text using OCR.
- **Multi-language Support**: Supports Hindi, English, Spanish, French, and Punjabi.
- **Keyword Search**: Search for specific keywords in the extracted text, with results highlighted if the keyword is found.
- **User-friendly Interface**: Built using Gradio, offering an intuitive and simple user experience.

## Technology Stack

- **Python 3.9+**
- **Gradio 3.50.2** for the web interface
- **PyTesseract 0.3.10** for OCR functionality
- **Pillow 10.0.1** for image processing
- **Tesseract OCR 5.3.1** as the OCR engine

## Languages Supported
- English
- Hindi
- Punjabi
- French
- Spanish

## Setup and Installation (Windows)

### Installation Steps

1. **Clone or Download the Repository**:
   - Using Git:
     ```bash
     git clone https://huggingface.co/spaces/Prabhjotschugh/OCR-TextVision
     cd OCR-TextVision
     ```
   - Alternatively, download the ZIP from Hugging Face and extract it.

2. **Set up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Required Python Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tesseract OCR**:
   - Download the Tesseract installer from [UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
   - Install it and note the installation path (default: `C:\Program Files\Tesseract-OCR`).
   - Add Tesseract to your system PATH:
     - Search for "Environment Variables" in the Start menu.
     - Under "System variables", find "Path", click "Edit", and add the Tesseract installation path.

5. **Install Language Data for Tesseract**:
   - Download language data files for Hindi (hin), Spanish (spa), French (fra), and Punjabi (pan) from [Tesseract GitHub](https://github.com/tesseract-ocr/tessdata).
   - Place them in the `tessdata` folder of your Tesseract installation directory.

6. **Configure the Application**:
   - Open `app.py` in a text editor.
   - Find the line:
     ```python
     pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
     ```
   - Replace it with:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
     ```

## Running the Application

1. Open a command prompt in the project directory.

2. Activate the virtual environment (if using one):
   ```bash
   venv\Scripts\activate
   ```

3. Start the application:
   ```bash
   python app.py
   ```

4. Open a web browser and navigate to `http://localhost:7860` to access the web interface.

## Usage Instructions

1. **Upload an Image**:
   - Click on the image upload area or drag and drop an image file.
   - Supported formats: JPEG, PNG, and other common image formats.

2. **Extract Text**:
   - After uploading the image, click "Extract Text."
   - The extracted text will be displayed in the output area.

3. **Keyword Search**:
   - Check the "Do you want to search for a keyword?" box.
   - Enter a keyword, then click "Search Keyword."
   - The keyword, if found, will be highlighted in the extracted text.

4. **Clear Results**:
   - Click "Clear" to reset the interface and upload a new image.


## Demo Video

https://github.com/user-attachments/assets/cb1a9de4-fb9a-42e5-a587-91ae67b7128f


## Example Outputs

![1](https://github.com/user-attachments/assets/a119b024-e745-410b-bc85-0344abfedc38)

![2](https://github.com/user-attachments/assets/0126a94f-bfa9-4aa6-94b8-f475a739f4ca)

![3](https://github.com/user-attachments/assets/369b38bf-0d9f-4026-b3db-ffe12037b412)

![4](https://github.com/user-attachments/assets/7a20da95-d6b3-4ac6-823f-ae96d82e2985)

![5](https://github.com/user-attachments/assets/94f257ec-e12a-43af-a123-831534a2ea90)

![6](https://github.com/user-attachments/assets/90874383-f8f8-4e24-91b9-717b30329e9e)














