import serial
import webbrowser
import pyautogui
from pycaw.pycaw import AudioUtilities

#Port
ser = serial.Serial('COM4', 115200)

device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume


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
            print("Number received:", number)
            if number >= 20:
                volume.SetMasterVolumeLevelScalar((number-20) / 100.0, None)
            else:
                actions[number]()
        except ValueError:
            print("No valid int:", line)
