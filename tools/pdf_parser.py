# Import libraries
import fitz

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
