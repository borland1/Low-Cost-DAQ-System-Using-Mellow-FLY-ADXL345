This is a quick start guide is for setting up KST Plot on a Windows PC.

The KST Plot web site is found at the following URL address: https://kst-plot.kde.org/  You'll also find
the Application Documentation and links to several tutorial videos.

KST Plot (Windows 32-bit) can be downloaded from this repository, or from the following 
link:  https://github.com/Kst-plot/kst-build/tree/Kst-32bit-3rdparty-plugins-Qt5

This is a Windows binary standalone copy.  So, there is no typical Windows installation required. Using the Windows File Manager, right click the downloaded zipped file, and choose 'Extract All'.  Move the file folder named 'Kst-2.0.x-2019.02.06-17.17-win32 to a location where you wish to run the program.

You should have the following main folder, and three sub-folders:

<img width="483" height="171" alt="image" src="https://github.com/user-attachments/assets/788d96c3-029f-4769-bdb6-d2b71da4e7b4" />

Next, migrate in File Explorer to the bin folder and find file 'kst.exe', click on 'kst.exe' to highlight the file, then right click on it and select 'create a shortcut'. Then click and drag the short cut to your desktop.

When running KST Plot for the first time, right click on the KST shortcut you created, and select 'Run as administrator'. After a security warning, select 'more info', select 'run anyway', then in the popup asking if you want to run application, select 'Yes'.  Two windows should appear. Ignore the blank screen window (that blank screen is normal for KST Plot), and enlarge the program window, so it overlaps the blank screen window. The next time you want to run kst.exe, just double click on the shortcut, or right click and select 'Open'; you can won't be prompted with those security warnings the next time you run KST Plot.

- Loading a CSV capture file in KST Plot (after converting the capture file to a CSV file using the Python script file.

The simplest way to load a CSV file in Windows KST Plot, is to drag and drop a file onto the Session window.  This brings up the programs 'Data Wizard' popup dialog window, which shows the 
file path already selected.  Click on the button 'Configure' to configure the ASCII CSV file.

<img width="1175" height="730" alt="image" src="https://github.com/user-attachments/assets/2cd35c8a-8e35-47b7-8a4b-d057c6637b6a" />

In the Configure ASCII dialog, observe your data file already read by KST Plot and configure the file as appropriate using the 'First lines of file' preview.  

<img width="1171" height="722" alt="image" src="https://github.com/user-attachments/assets/2f63de90-8353-4b1f-87c0-d6d4e0d4037d" />

After configuring ASCII file, click on 'OK' button to return to the Data Wizard file selection window, then click on 'Next'.  This next dialog window
allow selecting the Y-axis data vectors to be plotted. Select them individually or in a group from the available vectors list and move them to the Selected vectors list on the right side.   

<img width="1171" height="725" alt="image" src="https://github.com/user-attachments/assets/88119409-6b76-4260-9119-0107a20f17de" />

Click 'Next'. Then configure the data range and X axis data type.  If you want additional plots, select those and configure them here.

<img width="1170" height="729" alt="image" src="https://github.com/user-attachments/assets/24ebcc4a-b0f4-4763-bc12-6330e1e6257d" />

Click 'Next.  Finally select Curve placement and Style, Plot placement, and Labeling details. 

<img width="1173" height="730" alt="image" src="https://github.com/user-attachments/assets/6faad1d3-faad-4202-b464-aec7f96004ff" />

Click 'Finish'.  You'll now see your plots available for exploring. Here's tab 1 plots

<img width="1176" height="729" alt="image" src="https://github.com/user-attachments/assets/eb565e84-05ac-4e58-ab38-7c79c9331551" />

And Tab 2, of the Power Spectral Density (PSD) plots.

<img width="1174" height="727" alt="image" src="https://github.com/user-attachments/assets/92558e6d-664c-4c17-ac35-78e0ab711462" />

You can explore the data, using the Zoom features to zoom in on random events. In this case high g-force in z-axis channel.

<img width="1170" height="728" alt="image" src="https://github.com/user-attachments/assets/ec38c983-017a-4330-9579-2b488c8b4e2c" />

Or, on Tab 2, zooming in on lower frequencies of the PSD plots.

<img width="1175" height="727" alt="image" src="https://github.com/user-attachments/assets/2fd4f1a0-a1fe-4636-ad45-be0b70067fb2" />




