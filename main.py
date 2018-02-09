import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/lecture-videos/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.prettify())
    for link in soup.find_all('a'):
        print(link)

if __name__ == '__main__':
    main()
