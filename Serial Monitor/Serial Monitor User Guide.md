This is a guide for using Serial Monitor with Pi Pico firmware

You'll need a serial monitor program to connect with the Pi Pico firmware over USB. Once connected, you will be able to performing sensor calibration, adjusting sensor settings, and for obtaining acceleration sample data while running the Pi Pico in data streaming modes less than 1600 Hz.  For data streaming at 1600 Hz and 3200 Hz, I have included a Python script file that handles streaming data logging to a capture CSV file.

There are many simple Serial Monitor programs available (like: PuTTY, ArduinoIDE's Serial Monitor), which will work with the Pi Pico firmware here.

I have been using 'CoolTerm' serial monitor in Windows, which can be downloaded and used free of charge, here:   https://freeware.the-meiers.org/

Here's a screenshot of the program's workspace.

<img width="529" height="447" alt="CoolTerm1" src="https://github.com/user-attachments/assets/87c9f63c-3200-43c2-b918-dbc747abb1dd" />

Setting up Connection Options.  From the Connection dropdown menu, select Connection -> Options. 

Here are some screenshots showing the settings I used.

<img width="386" height="428" alt="CoolTerm2" src="https://github.com/user-attachments/assets/13161c46-13c7-421c-90c0-e9c78ccb5bc9" />

<img width="383" height="428" alt="CoolTerm3" src="https://github.com/user-attachments/assets/6980d789-74cf-4b60-b4cc-2f759f016508" />

<img width="385" height="431" alt="CoolTerm4" src="https://github.com/user-attachments/assets/f150865b-7559-4bad-bb11-d86c24ef3463" />

After pressing 'Connect', and then re-plugging in the FLY Pi Pico, you should see this screen, or maybe a warning about 'no calibration data found'.

<img width="530" height="446" alt="CoolTerm5" src="https://github.com/user-attachments/assets/e50a2c73-dd5e-40bd-afb4-82321cca03f2" />

During firmware built-in calibration, orientation of the Y-axis is correctly handled. However the axis orientation markings (Silkscreen) on the
FLY PCB incorrectly shows the wrong direction of the Y-axix.

Note the differences between this photo of the FLY PCB, as compared with the orientation shown in the Analog Devices ADXL345 datasheet.

<img width="601" height="595" alt="image" src="https://github.com/user-attachments/assets/f2e000f4-1075-4eb5-b31d-02b0159fabc4" />

<img width="1097" height="509" alt="image" src="https://github.com/user-attachments/assets/5cb9dd8b-d0d8-4b32-b38f-22f4e7d765f6" />


