from converter import PDFConverter, ImageConverter
import os

class FileConverter:
    def __init__(self):
        self.pdf_converter = PDFConverter()
        self.image_converter = ImageConverter()
        
    def convert_file(self, input_path: str, output_path: str) -> bool:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
        
        input_format = input_path.split('.')[-1].lower()
        
        if input_format == 'pdf':
            return self.pdf_converter.convert(input_path, output_path)
        elif input_format in self.image_converter.supported_formats:
            return self.image_converter.convert(input_path, output_path)
        else:
            raise ValueError(f"Unsupported input format: {input_format}") 