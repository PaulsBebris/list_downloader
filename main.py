import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import subprocess

# commandline parameters
# -youtube chanel name -playlist name OR -filename with CSV formatted lines as per commandline parameters
chanel = 'NetworkDirection'
playlist = 'ccna training'
playlist_file = []

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
## get container list
time.sleep(1)
titles = driver.find_elements(By.ID, 'video-title')
playlist = driver.find_elements(By.CSS_SELECTOR, 'a.yt-simple-endpoint.style-scope.yt-formatted-string')
# TODO create logic to read from file if present in current dir
# parse list
for i, j in enumerate(titles):
    title = j.text
    if i <= len(playlist)-1:
        href = playlist[i].get_attribute('href')
        playlist_file.append((i+1, title, href))
for i in playlist_file:
    print(f'{i[0]} : {i[1]}\n')

selection = input('Enter desired downloads separated by comma or single number')
selection_numbers = selection.split(',')
str = open('playlist.txt','wt')
for i in selection_numbers:
    str.write(playlist_file[int(i)-1][1] + ':' + playlist_file[int(i)-1][2] + '\n')
    os.chdir('./downloads')
    os.mkdir(playlist_file[int(i)-1][1])
    os.chdir(playlist_file[int(i)-1][1])
    subprocess.run(['youtube-dl', playlist_file[int(i)-1][2]])
    os.chdir('../')
#style-scope ytd-grid-renderer
# parsle datastructure to find list to download
# get url from current page
# pass url to youtube-dl as list
# create folder with downloadable files
# TODO pass a text file with download channel name + list name


print('-----DONE-----')



