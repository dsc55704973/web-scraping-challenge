from splinter import Browser
from bs4 import BeautifulSoup

nasa_url = 'https://mars.nasa.gov/news/'

def scrape_one_piece():
    one_dictionary='blah'
    return one_dictionary

def scrape_second_piece():
    one_dictionary='blahblah'
    return one_dictionary

def scrape_third_piece():
    one_dictionary='blahblahblah'
    return one_dictionary

def scrape_all():
    all_data={}
    all_data['headlines']=scape_first_piece()
    all_data['images_url']=scrape_second_piece()
    all_data['url']=scrape_second_piece() 
    return all_data
    