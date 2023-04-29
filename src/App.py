#!/usr/bin/env python3
import requests


def main():
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://tor-service:9050',
        'https': 'socks5h://tor-service:9050'
    }

    response = session.get(f"http://httpbin.org/ip")
    print(response.json())


if __name__ == "__main__":
    main()
