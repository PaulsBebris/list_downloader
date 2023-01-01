from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# commandline parameters
# -youtube chanel name -playlist name OR -filename with CSV formatted lines as per commandline parameters
chanel = 'NetworkDirection'
playlist = 'ccna training'

driver = webdriver.Firefox()
driver.get('https://www.youtube.com/@' + format(str(chanel)) + '/playlists')
time.sleep(1)
# TODO important dialog set language as EN !!!
reject_btn = driver.find_elements(By.CLASS_NAME, 'VfPpkd-vQzf8d')
btn_index = None
for i in range(len(reject_btn)):
    if reject_btn[i].text.upper() == 'Reject All'.upper():
        btn_index = i
        break
reject_btn[btn_index].click()

# get needed container
    # get container list

    # parse list
#style-scope ytd-grid-renderer
# parsle datastructure to find list to download
# get url from current page
# pass url to youtube-dl as list
# create folder with downloadable files
# TODO pass a text file with download channel name + list name




print("testing .... ")



