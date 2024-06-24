import os
import pymupdf4llm
import PyPDF2
import json
import requests
import uuid
import time
import fitz
import pytesseract
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

class PDFConverter:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def analyze_page(self, page):
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Increase resolution for better OCR
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        ocr_result = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
        page_text = " ".join(ocr_result["text"])

        page_confidence = sum(ocr_result["conf"]) / len(ocr_result["conf"])
        confident_page = 1 if page_confidence >= 70 else 0

        return page_text, page_confidence, confident_page

    def needs_ocr(self, file_path, num_pages_to_analyze=10, min_text_length=100, min_confidence=70):
        doc = fitz.open(file_path)
        num_pages = doc.page_count
        page_indices = [i * (num_pages // num_pages_to_analyze) for i in range(num_pages_to_analyze)]

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.analyze_page, doc.load_page(page_num)) for page_num in page_indices]
            with tqdm(total=len(futures), desc="Analyzing pages", unit="page") as pbar:
                total_text = ""
                confidence_sum = 0
                num_confident_pages = 0

                for future in futures:
                    page_text, page_confidence, confident_page = future.result()
                    total_text += page_text
                    confidence_sum += page_confidence
                    num_confident_pages += confident_page
                    pbar.update(1)

        doc.close()

        if len(total_text.strip()) < min_text_length:
            return True

        avg_confidence = confidence_sum / num_pages_to_analyze
        confident_page_ratio = num_confident_pages / num_pages_to_analyze

        print(f"\nExtracted Text Length: {len(total_text.strip())}")
        print(f"Average OCR Confidence: {avg_confidence:.2f}")
        print(f"Confident Page Ratio: {confident_page_ratio:.2f}")

        if avg_confidence < min_confidence or confident_page_ratio < 0.5:
            return True

        return False

    def upload_to_cloudflare(self, file_path):
        os.environ["CLOUDFLARE_API_URL"] = "https://workspace.askjunior2023.workers.dev/upload/"
        os.environ["CLOUDFLARE_CDN_URL"] = "https://pub-cc8438e664ef4d32a54c800c7c408282.r2.dev/"
        unique_id = str(uuid.uuid4())
        upload_url = os.environ["CLOUDFLARE_API_URL"] + unique_id + ".pdf"
        with open(file_path, 'rb') as f:
            headers = {'Content-Type': 'application/pdf'}
            upload_response = requests.put(upload_url, data=f.read(), headers=headers)
            upload_response.raise_for_status()
        new_url = f"{os.environ['CLOUDFLARE_CDN_URL']}{unique_id}.pdf"
        return new_url, unique_id
    
    def poll_and_get_markdown_text_url(self, file_id):
        url = "https://marker--xata-verification-verifier.modal.run"
        payload = json.dumps({
            "file_id": file_id,
            "workspace_id": "ws123",
            "collection_name": "test_collection"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        for i in range(20):
            response = requests.request("POST", url, headers=headers, data=payload)
            response_text = response.text
            response_json = json.loads(response_text)
            if response_json["status"] == "error":
                return response_json["error_message"]
            if response_json["status"] == "completed":
                return response_json["content"]
            print(response_json["pending_count"], " is pending")
            time.sleep(15)
    
    def ocr_routing_service(self, pdf_url, file_id):
        url = "https://marker--convertor-convert.modal.run"
        payload = json.dumps({
        "pdf_url": pdf_url,
        "file_id": file_id,
        "workspace_id": "ws123",
        "collection_name": "test_collection",
        "callback_url": "index_url.com"
        })
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text

    def convert(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        need_ocr = self.needs_ocr(self.file_path)
        if need_ocr:
            pdf_url, file_id = self.upload_to_cloudflare(self.file_path)
            md_content = self.ocr_routing_service(pdf_url, file_id)
            md_url = self.poll_and_get_markdown_text_url(file_id)
            return md_url
        else:
            md_content = pymupdf4llm.to_markdown(self.file_path)
            return md_content