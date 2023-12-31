# -*- coding: utf-8 -*-
"""Drive-Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1axv2XyNjW_mJ9CN6IUmNrdFrfoIEzFXM
"""

import pdfplumber
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os

# Download the "punkt" and "stopwords" resources
nltk.download('punkt')
nltk.download('stopwords')

# Specify the folder path of the PDF files in Google Drive
folder_path = '/content/gdrive/MyDrive/application/'

# Initialize an empty string to store the extracted text
extracted_text = ""

# Iterate through the files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is a PDF
    if file_name.endswith('.pdf'):
        # Construct the full file path
        file_path = os.path.join(folder_path, file_name)

        # Open the PDF file
        with pdfplumber.open(file_path) as pdf:
            # Accept user input for the natural language query
            query = input("Enter your natural language query: ")

            # Tokenize the query into words
            query_tokens = word_tokenize(query)

            # Remove stopwords from the query tokens
            stop_words = set(stopwords.words('english'))
            query_tokens = [token for token in query_tokens if token.lower() not in stop_words]

            # Iterate through the pages of the PDF
            for page in pdf.pages:
                # Extract text from the page
                text = page.extract_text()

                # Tokenize the page text
                page_tokens = word_tokenize(text)

                # Check if any query token is present in the page tokens
                if any(token in page_tokens for token in query_tokens):
                    extracted_text += text

# Print the extracted text that matches the query
print("Extracted Text:", extracted_text)