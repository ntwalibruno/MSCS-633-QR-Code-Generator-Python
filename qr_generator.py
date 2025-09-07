#!/usr/bin/env python3
"""
Simple QR Code Generator
Creates QR codes from URLs and saves them as images.
"""

import qrcode
from PIL import Image
import os
import sys
from datetime import datetime

def generate_qr_code(url, filename=None):
    """
    Generate a QR code from a URL and save it as an image.
    
    Args:
        url (str): The URL to encode in the QR code
        filename (str, optional): Custom filename for the output image
    
    Returns:
        str: The filename of the saved QR code image
    """
    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # About 7% error correction
            box_size=10,  # Size of each box in pixels
            border=4,  # Border size (minimum is 4)
        )
        
        # Add data to the QR code
        qr.add_data(url)
        qr.make(fit=True)
        
        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Generate filename if not provided
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"qr_code_{timestamp}.png"
        
        # Ensure filename has .png extension
        if not filename.lower().endswith('.png'):
            filename += '.png'
        
        # Save the image in the current directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(current_dir, filename)
        
        img.save(filepath)
        
        print(f" QR code generated successfully!")
        print(f" Saved as: {filepath}")
        print(f" URL encoded: {url}")
        
        return filepath
        
    except Exception as e:
        print(f" Error generating QR code: {str(e)}")
        return None

def validate_url(url):
    """
    Basic URL validation.
    
    Args:
        url (str): URL to validate
    
    Returns:
        str: Validated URL (with http:// prefix if needed)
    """
    url = url.strip()
    
    # Add protocol if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    return url

def main():
    """Main function to handle user input and generate QR code."""
    print(" Simple QR Code Generator ")
    print("=" * 40)
    
    try:
        # Get URL from user input
        if len(sys.argv) > 1:
            # URL provided as command line argument
            url = sys.argv[1]
            custom_filename = sys.argv[2] if len(sys.argv) > 2 else None
        else:
            # Interactive mode
            url = input("Enter the URL: ").strip()
            if not url:
                print(" No URL provided. Exiting.")
                return
            
            # Ask for optional custom filename
            custom_filename = input("Enter custom filename (optional, press Enter to auto-generate): ").strip()
            if not custom_filename:
                custom_filename = None
        
        # Validate and format URL
        url = validate_url(url)
        
        print(f"\n Generating QR code for: {url}")
        
        # Generate QR code
        result = generate_qr_code(url, custom_filename)
        
        if result:
            print(f"\n Done! You can now scan the QR code to visit the website.")
        else:
            print(f"\n Failed to generate QR code.")

    except KeyboardInterrupt:
        print("\n\n Goodbye!")
    except Exception as e:
        print(f"\n An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
