# Import libraries
import fitz
from utils.logger import get_logger

# Initialize module-level logger
logger = get_logger(__name__)

class PDFparser:
    """Utility class for extracting text from PDF documents
    """
    @staticmethod
    def extract_text(pdf_path: str) -> str:
        """Extract text from all pages of a pdf document 

        Args:
            pdf_path (str): Path of the pdf file

        Returns:
            str: Extracted text from pdf
        """

        logger.info(f"Extracting text from {pdf_path}")
        try:
            text = ""
            
            # Open document
            document = fitz.open(pdf_path)

            # Interate through all the pages
            for page in document:
                text += page.get_text() + '\n'

            document.close()

            return text.strip()
        
        
        except Exception as e:
            raise Exception (f"Error extracting text from PDF: {e}")
