import serial
import webbrowser
import pyautogui

#Port
ser = serial.Serial('COM4', 115200)

def callYoutube():
    url = "https://www.youtube.com/"
    webbrowser.open_new(url)

def playOrPause():
    pyautogui.press('playpause')

def skipPlayer():
    pyautogui.press('nexttrack')
    
def previousPlayer():
    pyautogui.press('prevtrack')
    
def callTwitch():
    url = "https://www.twitch.tv/"
    webbrowser.open_new(url)

actions = [callYoutube, playOrPause, skipPlayer, previousPlayer, callTwitch]

while True:
    line = ser.readline().decode('utf-8').strip()
    
    if line:
        try:
            number = int(line)
            print("Empfangene Zahl:", number)
            actions[number]()
        except ValueError:
            print("Kein gültiger int:", line)