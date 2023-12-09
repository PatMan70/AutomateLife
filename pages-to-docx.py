import os
from pathlib import Path
from pyth.plugins.plaintext.writer import PlaintextWriter
from pyth.plugins.xhtml.writer import XHTMLWriter
from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth import Document

def convert_pages_to_docx(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".pages"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.docx")

            # Convert Pages to XHTML
            document = Document(Rtf15Reader.read(open(input_path, "rb")))
            xhtml_content = XHTMLWriter.write(document).getvalue()

            # Convert XHTML to DOCX
            docx_content = PlaintextWriter.write(Document(xhtml_content)).getvalue()

            # Save the result to a DOCX file
            with open(output_path, "w", encoding="utf-8") as output_file:
                output_file.write(docx_content)

            print(f"Converted: {filename} -> {os.path.basename(output_path)}")

if __name__ == "__main__":
    # Specify the input and output folders
    input_folder_path = "path/to/input/folder"
    output_folder_path = "path/to/output/folder"

    # Call the conversion function
    convert_pages_to_docx(input_folder_path, output_folder_path)
