Before attempting to run a Python script files from the Windows PowerShell terminal, verify Python is installed on the Windows. 
 Python package 'pyserial' is also required to run these Python scripts.  The easiest and cleanest method to install Python is from
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

Two Python script files are provided for binary streaming from Pico over USB.

- Python script file 'capture_calibrated_CSV.py' is for capturing binary streaming mode samples (up to 3200 Hz output data rates)
and saving capture data to a CSV file named: 'capture.csv'.  You may need to edit the script's COM port number, to match your
Pico's Windows assignment COM number.

- The second Python script file is for converting data in file 'capture.csv' and converting the timestamp from microseconds
since boot, to elapsed time in seconds, which KST Plot can directly read.

One consideration when running capture files with millisecond timestamps, is that there is a firmware limitation the total sampling time before of clock rollover. This is not a system clock rollover limitation, but due to the timestamp formatting as a unsigned 32-bit integer for binary transfers over USB. This done to keep the data packet size more compact. Timestamp formatting in milliseconds, stored as a 32-bit unsigned integer, which rolls over every 71.6 minutes after processor bootup when system clock is set to zero.

Another consideration, is resultant capture file size while data logging.  As an example, using Python script file 'capture_calibrated_CSV.py', using settings of 3200 Hz sample rate, binary sampling for approximately 15 minutes, results in a CSV file size of 105,946 KB (106 MB).
