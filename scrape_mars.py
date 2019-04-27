import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    # visit mars mews site
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    # scape page into soup
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # find the title and body of first news article
    result = soup.find('li', class_='slide') 
    title = result.find('h3').text
    body = result.find('div', class_= 'rollover_description_inner').text

    news_title = title
    news_p = body

    # visit mars featured image site
    img_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(img_url)

    # scrape page into soup
    img_html = browser.html
    img_soup = BeautifulSoup(img_html, 'html.parser')

    # find the url for the featured image
    footer = img_soup.find('footer')
    featured_image_url = img_url + footer.a['data-fancybox-href']

    # visit the mars weather twitter page
    twit_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twit_url)

    # scrape page into soup
    twit_html = browser.html
    twit_soup = BeautifulSoup(twit_html, 'html.parser')

    # get the latest weather from a tweet
    container = twit_soup.find('div', class_='js-tweet-text-container')
    weather = container.find('p').text

    mars_weather = weather

    # visit the mars facts site and scrape for table using pandas
    mars_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(mars_url)

    # turn table into pandas dataframe
    mars_df = tables[0]
    mars_df.columns = ['Profile', 'Value']
    mars_df.set_index('Profile', inplace=True)

    # convert table into html
    mars_html_table = mars_df.to_html()
    mars_html_table = mars_html_table.replace('\n', '')

    # visit USGS site for mars info
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)

    # scrape page into soupt
    hem_html = browser.html
    hem_soup = BeautifulSoup(hem_html, 'html.parser')

    # find the name of mars hemispheres
    hem_title_result = hem_soup.find_all('div', class_='description')

    for hem_title in hem_title_result:
        title = hem_title.find('h3').text

    # get images
    hem_image1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(hem_image1)
    hem1 = browser.html
    hem1_soup = BeautifulSoup(hem1, 'html.parser')

    img_results_1 = hem1_soup.find_all('img', class_="wide-image")

    for img_url_1 in img_results_1:
        img1 = img_url_1['src']
    img1 = "https://astrogeology.usgs.gov" + img1

    hem_image2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(hem_image2)
    hem2 = browser.html
    hem2_soup = BeautifulSoup(hem2, 'html.parser')

    img_results_2 = hem2_soup.find_all('img', class_="wide-image")

    for img_url_2 in img_results_2:
        img2 = img_url_2['src']
    img2 = "https://astrogeology.usgs.gov" + img2

    hem_image3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(hem_image3)
    hem3 = browser.html
    hem3_soup = BeautifulSoup(hem3, 'html.parser')

    img_results_3 = hem3_soup.find_all('img', class_="wide-image")

    for img_url_3 in img_results_3:
        img3 = img_url_3['src']
    img3 = "https://astrogeology.usgs.gov" + img3

    hem_image4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(hem_image4)
    hem4 = browser.html
    hem4_soup = BeautifulSoup(hem4, 'html.parser')

    img_results_4 = hem4_soup.find_all('img', class_="wide-image")

    for img_url_4 in img_results_4:
        img4 = img_url_4['src']
    img4 = "https://astrogeology.usgs.gov" + img4

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_html_table": mars_html_table,
        "title": title,
        "title": title,
        "title": title,
        "title": title,
        "img1": img1,
        "img2": img2,
        "img3": img3,
        "img4": img4
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
