This is a guide for using Serial Monitor with Pi Pico firmware

You'll need a serial monitor program to connect with the Pi Pico firmware over USB. Once connected, you will be able to performing sensor calibration, adjusting sensor settings, and for obtaining acceleration sample data while running the Pi Pico in data streaming modes less than 1600 Hz.  For data streaming at 1600 Hz and 3200 Hz, I have included a Python script file that handles streaming data logging to a capture CSV file.

There are many simple Serial Monitor programs available (like: PuTTY, ArduinoIDE's Serial Monitor), which will work with the Pi Pico firmware here.

I have been using 'CoolTerm' serial monitor in Windows, which can be downloaded and used free of charge, here:   https://freeware.the-meiers.org/


During firmware built-in calibration, orientation of the Y-axis is correctly handled. However the axis orientation markings (Silkscreen) on the
FLY PCB incorrectly shows the wrong direction of the Y-axix.

Note the differences between this photo of the FLY PCB, as compared with the orientation shown in the Analog Devices ADXL345 datasheet.

<img width="601" height="595" alt="image" src="https://github.com/user-attachments/assets/f2e000f4-1075-4eb5-b31d-02b0159fabc4" />

<img width="1097" height="509" alt="image" src="https://github.com/user-attachments/assets/5cb9dd8b-d0d8-4b32-b38f-22f4e7d765f6" />


