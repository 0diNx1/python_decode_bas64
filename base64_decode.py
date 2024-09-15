
import base64
import argparse

def print_banner():
   
    banner = '''
                    _       _ 
 _ __ ___  _ __ __| |_ __ (_)
| '_ ` _ \| '__/ _` | '_ \| |
| | | | | | | | (_| | |_) | |
|_| |_| |_|_|(_)__,_| .__/|_|
                    |_|      
                                 
    '''
    print(banner)

def decode_base64(encoded_str: str) -> str:
   
    try:
        
        print(f"Input string: '{encoded_str}'")
        encoded_str = encoded_str.strip()
        missing_padding = len(encoded_str) % 4
        if missing_padding:
            encoded_str += '=' * (4 - missing_padding)
        print(f"String after padding adjustment: '{encoded_str}'")
        decoded_bytes = base64.b64decode(encoded_str, validate=True)
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    except Exception as e:
        raise ValueError(f"Invalid Base64 input or decoding error: {e}")

def main():
    """
    Main function for command-line execution.
    """
    # Print the banner
    print_banner()
    
    # argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("encoded_string", help="Base64 encoded string to decode")
    args = parser.parse_args()

    # Perform decoding
    try:
        decoded_str = decode_base64(args.encoded_string)
        print(f"Decoded string: {decoded_str}")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
