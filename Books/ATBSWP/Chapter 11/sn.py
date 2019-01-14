#! python3
import sys, webbrowser

if sys.argv[1].lower() == 'vk':
    webbrowser.open('https://vk.com/feed')
elif sys.argv[1].lower() == 'yt':
    webbrowser.open('https://www.youtube.com/')
