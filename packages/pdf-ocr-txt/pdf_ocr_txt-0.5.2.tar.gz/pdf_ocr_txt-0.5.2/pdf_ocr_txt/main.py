import os
import shutil
from pdf2image import convert_from_path
import pytesseract


def pdf_to_text(pdf_file, out_dir):
    # Create the output directory if it doesn't exist

    txt_dir = os.path.join(out_dir, 'TXT')
    png_dir = os.path.join(out_dir, 'PNG')

    # derive name of outputfile
    output_file = os.path.join(out_dir, os.path.basename(pdf_file)) + ".txt"

    shutil.rmtree(txt_dir, ignore_errors=True)
    shutil.rmtree(png_dir, ignore_errors=True)

    if not os.path.exists(png_dir):
        os.makedirs(png_dir)
    if not os.path.exists(txt_dir):
        os.makedirs(txt_dir)

    assert os.path.exists(pdf_file), pdf_file

    # Convert PDF to images
    images = convert_from_path(pdf_file)

    # Perform OCR on each image
    for i, image in enumerate(images):
        # Save the image for debugging purposes (optional)
        image_path = os.path.join(png_dir, f'page_{i + 1}.png')
        image.save(image_path, 'PNG')

        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(image)

        # Save the text to a file
        text_path = os.path.join(txt_dir, f'page_{i + 1}.txt')
        with open(text_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text)

    # Concatenate all text files into one
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i in range(len(images)):
            text_path = os.path.join(txt_dir, f'page_{i + 1}.txt')
            with open(text_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write("\n")  # Add a newline between pages
    return output_file

def test_main():
    # Example usage
    pdf_file = '../IN/some.pdf'  # Replace with your PDF file path
    out_dir = '../OUT'  # Replace with your desired output directory
    output_file=pdf_to_text(pdf_file, out_dir)
    print("RESULTS IN:",output_file)


if __name__ == "__main__":
    test_main()
