import chardet
import os
import sys

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def convert_to_utf8(input_file):
    # Detect the encoding of the input file
    detected_encoding = detect_encoding(input_file)
    
    if detected_encoding is None:
        print("Unable to detect encoding.")
        return
    
    try:
        # Read the file with the detected encoding
        with open(input_file, 'r', encoding=detected_encoding) as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"Error reading file with detected encoding {detected_encoding}. Trying 'windows-1256' instead.")
        try:
            with open(input_file, 'r', encoding='windows-1256') as f:
                content = f.read()
        except UnicodeDecodeError:
            print("Error reading file with fallback encoding 'windows-1256'. Exiting.")
            return
    
    # Create the output file path
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_utf8{ext}"
    
    # Write the content to the output file with utf-8 encoding
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Converted '{input_file}' from {detected_encoding} to UTF-8 and saved as '{output_file}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file.srt>")
    else:
        input_file_path = sys.argv[1]
        convert_to_utf8(input_file_path)

