#!/usr/bin/env python3
"""
Multi-Format Encoder/Decoder
=============================
"""

import base64
import urllib.parse
import html
import binascii
import argparse
from colorama import Fore, Style, init

init(autoreset=True)

class EncoderDecoder:
    @staticmethod
    def base64_encode(data):
        return base64.b64encode(data.encode()).decode()
    
    @staticmethod
    def base64_decode(data):
        try:
            return base64.b64decode(data).decode()
        except:
            return "Invalid Base64"
    
    @staticmethod
    def url_encode(data):
        return urllib.parse.quote(data)
    
    @staticmethod
    def url_decode(data):
        return urllib.parse.unquote(data)
    
    @staticmethod
    def html_encode(data):
        return html.escape(data)
    
    @staticmethod
    def html_decode(data):
        return html.unescape(data)
    
    @staticmethod
    def hex_encode(data):
        return data.encode().hex()
    
    @staticmethod
    def hex_decode(data):
        try:
            return bytes.fromhex(data).decode()
        except:
            return "Invalid Hex"

def main():
    parser = argparse.ArgumentParser(description='Encoder/Decoder Tool')
    parser.add_argument('-d', '--data', required=True, help='Data to encode/decode')
    parser.add_argument('-t', '--type', required=True, 
                       choices=['b64e', 'b64d', 'urle', 'urld', 'htmle', 'htmld', 'hexe', 'hexd'],
                       help='Operation type')
    
    args = parser.parse_args()
    
    ed = EncoderDecoder()
    
    operations = {
        'b64e': ed.base64_encode,
        'b64d': ed.base64_decode,
        'urle': ed.url_encode,
        'urld': ed.url_decode,
        'htmle': ed.html_encode,
        'htmld': ed.html_decode,
        'hexe': ed.hex_encode,
        'hexd': ed.hex_decode
    }
    
    result = operations[args.type](args.data)
    print(f"{Fore.GREEN}Result: {result}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
