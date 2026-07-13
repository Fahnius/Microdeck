# MicroDeck (Version 1.1)

This project allows the BBC microbit to work like a "Stream Deck". However, all functionalities must be programmed before use.
The .hex file runs on the microbit, while the Python script runs on the PC. The microbit communicates with the PC via a USB connection (in this example, COM4 is used. If you use a different PC, you will need to check which COM port is assigned).
The micro:bit sends a number via a UART connection, and the Python script on the PC interprets this number as a specific function or action.

Version 1.1 added a new feature, that you can control the volume of your PC (Windows only) using an potentiometer with 50kΩ connected to your microbit.

## Features (for Version 1.1)

- 'Y' on microbit  -> opens Youtube in your browser
- '~' on microbit  -> pauses current media player
- '>' on microbit  -> skips current media player
- '<' on microbit  -> go to previous media
- 'T' on microbit  -> opens Twitch in your browser

- The potentiometer -> control the volume on your windows pc

## Requirements

- Python 3.8
- pyautogui installed
- pyserial installed
- pycaw installed
- potentiometer with 50kΩ
- BBC microbit with micropython
