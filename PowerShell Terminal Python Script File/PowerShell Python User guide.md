Before attempting to run a Python script file, verify Python is installed on the Windows. Python package 'pyserial' is also required.

- From the Windows PowerShell terminal, Verify Python is installed by typing on command line:  'python --version'
     If Python is already installed, you should see a reply like:  'Python 3.14.6'

- From the Windows PowerShell terminal, Verify Python 'pyserial' package is installed, type command line: 'pip list'
   If Python 'pyserial' is installed, you should see something like: 'pyserial 3.5'

- To install Python from the Windows PowerShell terminal, type on command line:  'winget install Python.Python.3.14'

- To install Python package 'pyserial', from the Window PowerShell terminal, type command: 'python -m pip install pyserial'

Two Python script files are provided for binary streaming from Pico over USB. 
- One Python script file is for capturing binary streaming samples
and saving them to a CSV file named: 'capture.csv'.
- The second Python script file is for converting data in file 'capture.csv' and converting the timestamp from microseconds
since boot, to elapsed time in seconds, which KST Plot can directly read.
