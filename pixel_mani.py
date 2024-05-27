from gooey import Gooey, GooeyParser
import os

@Gooey(program_name="Image Encryptor", 
       program_description="Encrypt and decrypt an image using XOR encryption")
def main():
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
    
    if not os.path.isfile(file_name):
        print("File does not exist.")
        return
    
    print(file_name, key)
    
    with open(file_name,'rb') as fi:
        image = fi.read()
    
    image = bytearray(image)
    
    for index,values in enumerate(image):
        image[index] = values^(key)
    
    with open(file_name,'wb') as fi1:
        fi1.write(image)
        
    print("Operation complete.")
    
if __name__ == "__main__":
    main()