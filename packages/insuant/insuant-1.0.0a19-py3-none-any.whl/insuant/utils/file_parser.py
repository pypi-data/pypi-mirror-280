# Install instruction https://unstructured-io.github.io/unstructured/installation/full_installation.html
# pip install "unstructured[all-docs]"

import os
import time

import PyPDF2
import pandas as pd
import pdfplumber

from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredExcelLoader
from unstructured.partition.auto import partition
from unstructured.partition.pdf import partition_pdf
from llama_parse import LlamaParse
import nest_asyncio

nest_asyncio.apply()


class File_Parser():

    def __init__(self):
        print("File_Parser Utils Init...")
        # Rest of the code remains unchanged
        load_dotenv()

    def processExcelFiles(self, files):
        text = ""
        print('Processing Files: ', files)

        for file in files:
            loader = UnstructuredExcelLoader(file)
            print('Loader: ', loader)
            docs = loader.load()
            print('Docs: ', docs)
            #for page in pdf_reader.pages:
            text += docs
        return text

    # Extract elements from PDF
    def extract_pdf_unstructured(self, path, fname):
        """
        Extract images, tables, and chunk text from a PDF file.
        path: File path, which is used to dump images (.jpg)
        fname: File name
        """
        return partition_pdf(
            filename=path + fname,
            extract_images_in_pdf=False,
            infer_table_structure=False,
            chunking_strategy="by_title",
            max_characters=4000,
            new_after_n_chars=3800,
            combine_text_under_n_chars=2000,
            image_output_dir_path=path,
        )

    # Categorize elements by type
    def categorize_elements(self, raw_pdf_elements):
        """
        Categorize extracted elements from a PDF into tables and texts.
        raw_pdf_elements: List of unstructured.documents.elements
        """
        tables = []
        texts = []
        for element in raw_pdf_elements:
            if "unstructured.documents.elements.Table" in str(type(element)):
                tables.append(str(element))
            elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
                texts.append(str(element))
        return texts, tables

    # Open the PDF file
    def extract_pypdf_content(self, fname):
        # Open the PDF file
        pdf_file = PyPDF2.PdfReader(fname)

        # Extract the content from each page
        content = []
        for page in pdf_file.pages:
            content.append(page.extract_text())

        # Convert the content to JSON format
        # json_content = json.dumps(content)

        return content

    def getFileExt(self, file):
        return os.path.splitext(file)[1]

    def processFile(self, file, parcer="default"):
        # print('Processing Files: ', files)

        text = ""
        file_ext = self.getFileExt(file)

        if file_ext == '.pdf' and parcer == "llama":
            # Llama Partition
            print('Processing PDF File: ', file)
            # nest_asyncio.apply()

            starttime = time.time()
            documents = LlamaParse(
                result_type="markdown",
                api_key=os.getenv('LLAMA_CLOUD_API_KEY'),
                num_workers=4).load_data(file)
            print('Time to process PDF: ', time.time() - starttime)
            docs = documents[0].text
            text += docs

        elif file_ext == '.pdf':
            # Unstructured Partition
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    text += page.extract_text()

        else:
            # Unstructured Partition
            starttime = time.time()
            print('Processing Non-PDF File: ', file)
            elements = partition(filename=file)
            print('Time to process PDF: ', time.time() - starttime)

            for element in elements:
                text += element.text

        return text

    def processAllFiles(self, files, parcer="default", file_ext=None):
        files_text = []

        for file in files:
            text = self.processFile(file, parcer);
            files_text.append({"name": file, "format": file_ext, "text": text})

        return files_text


def main():
    fPath = '/Users/prem/Prem/projects/gds/ai-saas/data/in/'
    fName = '20240313_Bundlenull_DealCloud_BillowButler_v1-6.pdf'
    #fName = 'bank_customer.xls'
    files = [fPath + fName, fPath + 'bank_customer.xls', fPath + 'DC Bundle Example.pdf', fPath + 'bank_customer.csv']
    files = [fPath + 'Logo.ico']

    fp = File_Parser()
    # Method 1 - LC SQL Agent
    text = fp.processFile(files, "llama");

    print('Text: ', text)


if __name__ == "__main__":
    main()

### 
#print('File Ext: ', file_ext)
#if file_ext == '.pdf':
#    documents = LlamaParse(result_type="markdown").load_data(file)
#    docs = documents[0].text
#elif file_ext == '.xlsx' or file_ext == '.xls':
#    loader = UnstructuredExcelLoader(file)
#elif file_ext == '.csv':
#    loader = CSVLoader(file)
#elif file_ext == '.doc' or file_ext == '.docx':
#    loader = Docx2txtLoader(file)
#elif file_ext == '.txt':
#    loader = UnstructuredTextLoader(file)
#elif file_ext == '.json':
#    loader = JSONLoader(file)
#elif file_ext == '.xml':
#    loader = UnstructuredXmlLoader(file)
#elif file_ext == '.jpg' or file_ext == '.png' or file_ext == '.gif' or file_ext == '.jpeg':
#    loader = UnstructuredImageLoader(file)
#else:
#    print('Unsupported File Ext: ', file_ext)
