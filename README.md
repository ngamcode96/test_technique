# README

## ☁️ Running on Google Colab
You can quickly test the scripts on **Google Colab**:

[Run on Google Colab](YOUR_NOTEBOOK_LINK_HERE)

##  Prerequisites

Before starting, make sure you have installed the required dependencies.

###  Installing System Dependencies
These packages are necessary for processing PDF files and performing OCR:
```bash
sudo apt-get install poppler-utils
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
```

###  Installing Python Dependencies
Install the required Python libraries from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

##  (Optional) Creating and Activating a Virtual Environment
It is recommended to use a virtual environment to avoid dependency conflicts:
```bash
python -m venv venv  # Create the virtual environment
source venv/bin/activate  # Activate (Linux/Mac)
# venv\Scripts\activate  # Activate (Windows)
```

##  Running the Scripts

### 1 Extracting Text from PDF
Run the following command to extract text from the provided PDF file:
```bash
python extract_text_from_pdf.py
```

### 2️ Running Occurrence Tests
Run the tests using `pytest`:
```bash
python -m pytest _etl_a9number_v3.py
```
**Expected result:** Success **2/2**