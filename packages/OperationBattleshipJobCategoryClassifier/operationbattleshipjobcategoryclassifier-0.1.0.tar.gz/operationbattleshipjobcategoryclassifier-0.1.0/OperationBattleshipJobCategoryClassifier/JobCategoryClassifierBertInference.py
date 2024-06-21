import os
import sys
from pathlib import Path
import torch
import requests
import zipfile
import logging
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from joblib import load
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

log_file_path = os.path.join(Path(__file__).parent.absolute(), 'logfile.log')
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(threadName)s - %(filename)s - %(funcName)s - %(message)s',
                    filename=log_file_path,
                    filemode='w')


class JobCategoryClassifierBertInference:
    def __init__(self, s3_url):
        logging.info("Initializing JobCategoryClassifierBertInference class.")
        self.s3_url = s3_url
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        # Determine the working directory and set model_dir
        working_dir = os.getcwd()
        self.model_dir = os.path.join(working_dir, 'tmp', 'model')
        os.makedirs(self.model_dir, exist_ok=True)
        
        # Download and extract model files from S3
        self.download_and_extract_model(s3_url, self.model_dir)
        
        # Load model
        try:
            self.model = DistilBertForSequenceClassification.from_pretrained(self.model_dir)
            self.model.to(self.device)
            logging.info("Model loaded successfully.")
        except Exception as e:
            logging.error(f"Failed to load model: {e}")
            raise
        
        # Load tokenizer
        try:
            self.tokenizer = DistilBertTokenizer.from_pretrained(self.model_dir)
            logging.info("Tokenizer loaded successfully.")
        except Exception as e:
            logging.error(f"Failed to load tokenizer: {e}")
            raise
        
        # Load label encoder
        try:
            label_encoder_path = os.path.join(self.model_dir, 'label_encoder.joblib')
            self.label_encoder = load(label_encoder_path)
            logging.info("Label encoder loaded successfully.")
        except Exception as e:
            logging.error(f"Failed to load label encoder: {e}")
            raise
    
    def download_and_extract_model(self, s3_url, download_dir):
        """
        Downloads the zip file from the specified S3 URL and extracts it to the given directory.
        """
        logging.info(f"Downloading and extracting model from {s3_url} to {download_dir}.")
        zip_path = os.path.join(download_dir, 'model.zip')
        
        try:
            # Download the zip file
            response = requests.get(s3_url, stream=True)
            if response.status_code == 200:
                with open(zip_path, 'wb') as f:
                    f.write(response.content)
                logging.info(f"Downloaded {s3_url} to {zip_path}")
            else:
                logging.error(f"Failed to download {s3_url}. Status code: {response.status_code}")
                return
        
            # Extract the zip file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(download_dir)
            logging.info(f"Extracted {zip_path} to {download_dir}")
        
            # Remove the zip file after extraction
            #os.remove(zip_path)
        except Exception as e:
            logging.error(f"Error in download_and_extract_model: {e}")
            raise
    
    def preprocess(self, job_title):
        job_title = job_title.lower()
        job_title = ''.join([c for c in job_title if c.isalnum() or c.isspace()])
        return job_title
    
    def predict(self, job_title):
        job_title = self.preprocess(job_title)
        inputs = self.tokenizer(job_title, return_tensors="pt", padding=True, truncation=True, max_length=512)
        inputs = {key: val.to(self.device) for key, val in inputs.items()}
        
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        logits = outputs.logits
        pred_label_id = torch.argmax(logits, axis=1).item()
        pred_label = self.label_encoder.inverse_transform([pred_label_id])[0]
        
        return pred_label

