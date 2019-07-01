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
    report = parse_html(html)
    print("It is currently {} {} in {}. The conditions are {}.".format(report[2], report[3], report[1], report[0].lower()))
    #display forecast

def print_header():
    print('-------')
    print('WEATHER APP')
    print('-------')

def get_url(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text

def parse_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    return condition, loc, temp, scale

def cleanup_text(text : str):
    if not text:
        return text
    
    text = text.strip()
    return text

if __name__ == '__main__':
    main()
