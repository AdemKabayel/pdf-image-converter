from abc import ABC, abstractmethod
from pdf2docx import Converter as PDFToDocx
from pdf2image import convert_from_path
from PIL import Image
import os


class BaseConverter(ABC):
    @abstractmethod
    def convert(self, input_path: str, output_path: str) -> bool:
        pass

class PDFConverter(BaseConverter):
    def __init__(self):
        self.supported_formats = ['docx', 'jpg', 'png']
    
    def convert(self, input_path: str, output_path: str) -> bool:
        try:
            output_format = output_path.split('.')[-1].lower()
            
            if output_format not in self.supported_formats:
                raise ValueError(f"Unsupported output format: {output_format}")
            
            if output_format == 'docx':
                return self._convert_to_docx(input_path, output_path)
            elif output_format in ['jpg', 'png']:
                return self._convert_to_image(input_path, output_path)
            
            return False  # Add default return for unsupported formats
                
        except Exception as e:
            print(f"Error converting PDF: {str(e)}")
            return False
    
    def _convert_to_docx(self, input_path: str, output_path: str) -> bool:
        converter = PDFToDocx(input_path)
        converter.convert(output_path)
        converter.close()
        return True
    
    def _convert_to_image(self, input_path: str, output_path: str) -> bool:
        images = convert_from_path(input_path)
        for i, image in enumerate(images):
            name, ext = os.path.splitext(output_path)
            current_output = f"{name}_{i+1}{ext}"
            image.save(current_output)
        return True

class ImageConverter(BaseConverter):
    def __init__(self):
        self.supported_formats = ['jpg', 'jpeg', 'png', 'webp', 'bmp', 'gif']
    
    def convert(self, input_path: str, output_path: str) -> bool:
        try:
            output_format = output_path.split('.')[-1].lower()
            
            if output_format not in self.supported_formats:
                raise ValueError(f"Unsupported output format: {output_format}")
            
            image = Image.open(input_path)
            
            # Convert RGBA to RGB if saving as JPEG
            if output_format in ['jpg', 'jpeg'] and image.mode == 'RGBA':
                image = image.convert('RGB')
                
            image.save(output_path, format=output_format.upper())
            return True
            
        except Exception as e:
            print(f"Error converting image: {str(e)}")
            return False 