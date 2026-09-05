This is a guide for installing Python on Windows PowerShell terminal. However Microsoft PowerShell terminal is also available
as an option for Apple Mac OS and Linux OS, and these systems also offer similar terminal capabilities.

Before attempting to run Python script files from the Windows PowerShell terminal, verify Python has been installed.
 Python package 'pyserial' is also required to run these Python scripts.  
 
 The easiest and cleanest method to install Python is from
 the PowerShell terminal, and requires no manual browser downloads. 

- From the Windows PowerShell terminal, Verify Python is installed by typing on command line:  'python --version'
     If Python is already installed, you should see a reply like:  'Python 3.14.6'

- From the Windows PowerShell terminal, Verify Python 'pyserial' package is installed, type command line: 'pip list'
   If Python 'pyserial' is installed, you should see something like: 'pyserial 3.5'

- To install Python from Windows, 'exit' any open PowerShell terminal, then open it again, choosing 'Run As Administrator'. To install Python
  with Administrative privliges, type on the command line:  'winget install Python.Python.3'.  This command installs the latest version
  of Python 3.x.  'Exit' the terminal to allow Python to initialize on the next terminal startup.

- After installing Python, Install Python package 'pyserial' from the PowerShell terminal by typing the
   command: 'python -m pip install pyserial'

Two Python script files are provided for binary streaming from Pico over USB and for re-formatting the timestamp, from micro-seconds
to seconds, for direct loading into KST Plot.

- Python script file 'capture_calibrated_csv_V2.py' is for capturing binary streaming mode samples (up to 3200 Hz output data rates)
and saving capture data to a CSV file named: 'capture.csv'.  You may need to edit the script's COM port number, to match your
Pico's Windows assignment COM number.

- The second Python script file 'convert_tus_to_elapsed.py', is for converting file 'capture.csv' with timestamp from microseconds
since boot, to elapsed time in seconds. The resultant file created is named 'capture_elapsed.csv', which can be renamed and directly
read by KST Plot as a CSV file.

To get started logging data from the sensor, first use a Serial Monitor to both: calibrate the ADXL345 sensor, and to configure
the Pico settings for binary streaming. Then, using Windows File Explorer, create a folder where data logging files will reside.
Copy the two edited Python script files: 'capture_calibrated_csv_V2.py' and 'convert_tus_to_elapsed2.py' to that folder. Then open
a Windows PowerShell terminal, by either, right clicking in the directory list's blank space and selecting open Terminal, or
in the path block at the top of the File Explorer, click in the blank space there to highlight the entire path and type 'powershell'.

You should see a terminal with the same path as the File Explorer.  With the pico connected to the USB port, type in the PowerShell
terminal:  'py capture _calibrated_csv_V2.py'.

<img width="1030" height="754" alt="PowerShellCapture" src="https://github.com/user-attachments/assets/5f4ff1fb-1e67-4fdc-943b-8549b8cf05bc" />

After typing the Enter key, you should see a prompt saying 'Capturing verified samples to ....  Press Cntl+C to stop' and data progress.

After stopping the capture, you can convert the resultant capture file named 'capture.csv' with timestamps in microseconds to elapsed time
in seconds, by running the Python script file 'convert_tus_to_elapsed2.py'.  In the same PowerShell terminal, type: 'py convert_tus_to_elapsed2.py'
and type the Enter key.
<img width="1038" height="759" alt="PowerShellConvert" src="https://github.com/user-attachments/assets/000e5c02-202a-4639-957a-8a78003f4368" />

One consideration when running capture files with millisecond timestamps, is that there is a firmware limitation the total sampling time before of clock rollover. This is not a system clock rollover limitation, but due to the timestamp formatting as a unsigned 32-bit integer for binary transfers over USB. This done to keep the data packet size more compact. The Timestamp formatting in milliseconds rolls over every 71.6 minutes after processor bootup when system clock is set to zero.

Another consideration, is resultant capture file size while data logging.  As an example, using Python script file 'capture_calibrated_csv_V2.py', using settings of 3200 Hz sample rate, binary sampling for approximately 15 minutes, results in a CSV file size of 105,946 KB (106 MB).
