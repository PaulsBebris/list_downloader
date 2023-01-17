import sys
from os import chdir, mkdir, getcwd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from multiprocessing import Process
from subprocess import call

# commandline parameters
# -youtube chanel name -playlist name OR -filename with CSV formatted lines as per commandline parameters
# chanel = 'NetworkDirection'
# playlist = 'ccna training'
chanel = sys.argv[1]
# playlist = sys.argv[2]
playlist_file = []

driver = webdriver.Firefox()
driver.get('https://www.youtube.com/@' + format(str(chanel)) + '/playlists')
sleep(1)
# TODO important dialog set language as EN !!!
reject_btn = driver.find_elements(By.CLASS_NAME, 'VfPpkd-vQzf8d')
btn_index = None
for i in range(len(reject_btn)):
    if reject_btn[i].text.upper() == 'Reject All'.upper():
        btn_index = i
        break
reject_btn[btn_index].click()

sleep(1)
titles = driver.find_elements(By.ID, 'video-title')
playlist = driver.find_elements(By.CSS_SELECTOR, 'a.yt-simple-endpoint.style-scope.yt-formatted-string')
# TODO create logic to read from file if present in current dir
# parse list
for i, j in enumerate(titles):
    title = j.text
    if i <= len(playlist) - 1:
        href = playlist[i].get_attribute('href')
        playlist_file.append((i + 1, title, href))
for i in playlist_file:
    print(f'{i[0]} : {i[1]}\n')

selection = input('Enter desired downloads separated by comma or single number: ')
selection_numbers = selection.split(',')
playlist_txt = open('playlist.txt', 'wt')


def youtubedl(resource):
    call(["youtube-dl", resource])


PATH = getcwd() + '/downloads/'
for i in selection_numbers:
    playlist_txt.write(playlist_file[int(i) - 1][1] + ':' + playlist_file[int(i) - 1][2] + '\n')
    try:
        chdir(PATH)
        mkdir(playlist_file[int(i) - 1][1])
    except FileExistsError:
        pass
    chdir(playlist_file[int(i) - 1][1])
    Process(target=youtubedl, args=(playlist_file[int(i) - 1][2],), name='XXX'+i).start()

    chdir(PATH)

print('-----Download in progress-----')
