# MicroDeck

This project allows the BBC micro:bit to work like a "Stream Deck". However, all functionalities must be programmed before use.
The .hex file runs on the micro:bit, while the Python script runs on the PC. The micro:bit communicates with the PC via a USB connection (in this example, COM4 is used. If you use a different PC, you will need to check which COM port is assigned).
The micro:bit sends a number via a UART connection, and the Python script on the PC interprets this number as a specific function or action.

## Features (for Version 1.0)

- Y on microbit  -> opens Youtube in your browser
- ~ on microbit  -> pauses current media player
- > on microbit  -> skips current media player
- < on microbit  -> go to previous media
- T on microbit  -> opens Twitch in your browser

## Requirements

- Python 3.4
- pyautogui installed
- pyserial installed
- BBC microbit with micropython
