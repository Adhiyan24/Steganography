import cv2
import os

# Function to embed text into an image using OpenCV
def encode_text_opencv(secret_text, password):
    image_path = "example.jpg"
    output_image = "encoded_example.png"
    
    img = cv2.imread(image_path)
    if img is None:
        print("Cover image not found!")
        return
    
    with open("pass.txt", "w") as f:
        f.write(password)
    
    n, m, z = 0, 0, 0
    for char in secret_text:
        if n >= img.shape[0] or m >= img.shape[1]:
            print("Message is too long for the image!")
            break
        img[n, m, z] = ord(char)
        n += 1
        m += 1
        z = (z + 1) % 3
    
    cv2.imwrite(output_image, img)
    os.system(f"start {output_image}")  # Adjust for OS compatibility
    print("Secret message embedded into image!")

# Function to decrypt text from an image using OpenCV
def decode_text_opencv():
    image_path = "encoded_example.png"
    
    img = cv2.imread(image_path)
    if img is None:
        print("Encrypted image not found!")
        return
    
    try:
        with open("pass.txt", "r") as f:
            correct_pass = f.read().strip()
    except FileNotFoundError:
        print("Password file not found!")
        return
    
    pas = input("Enter passcode for Decryption: ")
    if pas != correct_pass:
        print("Incorrect passcode. Access denied!")
        return
    
    try:
        length = int(input("Enter secret message length: "))
    except ValueError:
        print("Invalid length input!")
        return
    
    message = ""
    n, m, z = 0, 0, 0
    for i in range(length):
        if n >= img.shape[0] or m >= img.shape[1]:
            print("Reached image boundary before reading the full message.")
            break
        message += chr(img[n, m, z])
        n += 1
        m += 1
        z = (z + 1) % 3
    
    print("Decrypted message:", message)

# Example usage
if __name__ == "__main__":
    choice = input("Do you want to encode (e) or decode (d)? ")
    
    if choice == 'e':
        secret_text = input("Enter secret message: ")
        password = input("Enter a passcode: ")
        encode_text_opencv(secret_text, password)
    elif choice == 'd':
        decode_text_opencv()
    else:
        print("Invalid choice.")

