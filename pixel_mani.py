from gooey import Gooey, GooeyParser
import os

@Gooey(program_name="Image Encryptor/Decryptor", 
       program_description="Encrypt and decrypt an image using XOR encryption")
def main():
    """
    Main function that sets up the GUI for the Image Encryptor/Decryptor program.
    It parses the input arguments for the image file and encryption key,
    then determines whether to encrypt or decrypt the image based on the file name.
    """
    parser = GooeyParser()
    parser.add_argument(
        'image_file',
        widget='FileChooser',
        help='Select an image (jpg, jpeg, png)',
        type=str,
        )
    parser.add_argument(
        'encryption_key',
        help='Enter an encryption key (numeric)',
        type=int,
    )
    
    args = parser.parse_args()
    file_name = args.image_file
    key = args.encryption_key
    
    # Validation
    if not os.path.isfile(file_name):
        print("File does not exist.")
        return
    
    if not file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        print("Selected file is not a supported image type.")
        return
    
    if os.path.basename(file_name).startswith("crypt."):
         decrypt_image(file_name, key)
    else:
        encrypt_image(file_name, key)
    
def encrypt_image(file_name, key):
    """
    Encrypts the given image file using XOR encryption with the provided key.
    The encrypted file is saved with a "crypt." prefix in the file name.
    
    Args:
        file_name (str): The name of the image file to be encrypted.
        key (int): The encryption key.
    """
    with open(file_name, 'rb') as fi:
        image = fi.read()
        
    image = bytearray(image)

    for index, value in enumerate(image):
        image[index] = value^(key)
        
    # Rename the file to crypt.filename.extension
    path, extension = os.path.splitext(file_name)
    new_file_name = f"crypt.{os.path.basename(path)}{extension}"

    with open(new_file_name, 'wb') as fi1:
        fi1.write(image)

    print(f"Encryption complete. New file: {new_file_name}")

def decrypt_image(file_name, key):
    """
    Decrypts the given encrypted image file using XOR decryption with the provided key.
    The decrypted file is saved with the original file name, removing the "crypt." prefix.
    
    Args:
        file_name (str): The name of the encrypted image file to be decrypted.
        key (int): The decryption key.
    """
    with open(file_name, 'rb') as fi:
        image = fi.read()
    
    image = bytearray(image)
    
    for index, value in enumerate(image):
        image[index] = value ^ key
    
    # Rename the file to filename.extension
    new_file_name = os.path.basename(file_name)[6:]  # Remove 'crypt.' prefix
    
    with open(new_file_name, 'wb') as fi1:
        fi1.write(image)
    
    print(f"Decryption complete. New file: {new_file_name}")

    
if __name__ == "__main__":
    main()