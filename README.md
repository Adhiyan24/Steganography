# Steganography


## Overview
This project implements a simple image steganography technique using the Least Significant Bit (LSB) method. It allows users to hide a secret message inside an image and retrieve it later using OpenCV.

## Features
- Encode a secret message into an image
- Password-protected message embedding
- Retrieve and decrypt the hidden message
- Uses OpenCV for image processing

## Requirements
- Python 3.x
- OpenCV (`cv2`)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/steganography-lsb.git
   cd steganography-lsb
   ```
2. Install dependencies:
   ```sh
   pip install opencv-python
   ```

## Usage
### Encoding a Message
1. Place the cover image in the project directory and rename it to `example.jpg`.
2. Run the script and choose encoding mode:
   ```sh
   python steganography.py
   ```
3. Enter the secret message and a passcode.
4. The encoded image will be saved as `encoded_example.png`.

### Decoding a Message
1. Run the script and choose decoding mode:
   ```sh
   python steganography.py
   ```
2. Enter the correct passcode.
3. Provide the length of the hidden message.
4. The message will be displayed.

## Notes
- Ensure the message is not too long for the image size.
- The encoding process modifies pixel values slightly, but the change is imperceptible to the human eye.

## License
This project is open-source and available under the MIT License.

