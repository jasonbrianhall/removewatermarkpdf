#!/usr/bin/env python

import argparse
from PyPDF2 import PdfReader, PdfWriter

def remove_watermark(input_path, output_path):
    """
    Remove watermarks from a PDF file
    
    Args:
        input_path (str): Path to input PDF file
        output_path (str): Path where modified PDF will be saved
    """
    try:
        # Create PDF reader and writer objects
        reader = PdfReader(input_path)
        writer = PdfWriter()

        # Process each page
        for page in reader.pages:
            # Remove annotations (which might contain watermarks)
            if '/Annots' in page:
                del page['/Annots']

            # Remove XObject forms (another common way watermarks are implemented)
            if '/Resources' in page:
                resources = page['/Resources']
                if '/XObject' in resources:
                    xobject = resources['/XObject']
                    # Remove each form XObject
                    for key in list(xobject.keys()):
                        if '/Subtype' in xobject[key]:
                            if xobject[key]['/Subtype'] == '/Form':
                                del xobject[key]

            # Add the modified page
            writer.add_page(page)

        # Write the modified content to the output file
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
            
        print(f"Successfully processed PDF. Output saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

def main():
    parser = argparse.ArgumentParser(
        description='Remove watermarks from PDF files'
    )
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Path to input PDF file'
    )
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Path where modified PDF will be saved'
    )
    
    args = parser.parse_args()
    remove_watermark(args.input, args.output)

if __name__ == "__main__":
    main()
