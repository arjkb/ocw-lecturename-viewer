import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/lecture-videos/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    links = map(lambda x: x.string, soup.find_all('a'))

    for s in links:
        if str(s).startswith('Lecture'):
            print(s)

if __name__ == '__main__':
    main()
