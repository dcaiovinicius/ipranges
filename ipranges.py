from bs4 import BeautifulSoup
import requests
import sys
import argparse

def get_asn(target):
    url = f'https://bgp.he.net/search?search%5Bsearch%5D={target}&commit=Search'.format(target)

    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data")
        sys.exit(1)
    
    html = BeautifulSoup(response.text, 'html.parser')
    for row in html.find_all('td'):
        for link in row.find_all('a'):
            print(link.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Search by IP range')
    parser.add_argument('--domain', help='Specify a domain ex: tesla')

    arguments = parser.parse_args()
    if arguments.domain:
        get_asn(arguments.domain)
    else:
        parser.print_help()