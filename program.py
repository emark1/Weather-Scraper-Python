import requests
import bs4

def main():
    #print header
    print_header()
    #get zipcode
    code = input("Please enter zipcode for weather: ")
    #get html from website
    html = get_url(code)
    #parse the html text
    parse_html(html)
    #display forecast

def print_header():
    print('-------')
    print('WEATHER APP')
    print('-------')

def get_url(zipcode):
    url = 'https://www.wunderground.com/weather/us/tx/houston/{}'.format(zipcode)
    response = requests.get(url)
    return response.text

def parse_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    # print(soup)

if __name__ == '__main__':
    main()