from main import FileConverter

def main():
    converter = FileConverter()
    
    # Convert PDF to DOCX
    converter.convert_file('sample.pdf', 'output.docx')
    
    # Convert PDF to images
    converter.convert_file('sample.pdf', 'output.jpg')
    
    # Convert image formats
    converter.convert_file('image.png', 'converted.jpg')
    converter.convert_file('image.jpg', 'converted.webp')

if __name__ == "__main__":
    main() 