import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010/lecture-videos/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    links = map(lambda a: a.string, soup.find_all('a'))
    lectures = filter(lambda s: str(s).startswith('Lecture'), links)

    for lecture in lectures:
        print(lecture)


if __name__ == '__main__':
    main()
