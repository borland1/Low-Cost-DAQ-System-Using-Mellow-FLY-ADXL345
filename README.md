# Low-Cost-DAQ-System-Using-Mellow-FLY-ADXL345
This project is a low cost Data Acquisition (DAQ) System, based on a re-purposed Mellow FLY-ADXL345 Digital 3-Axis Accelerometer Sensor, running custom
Raspberry Pi Pico firmware, Python script files for dataset logging as CSV capture files, and for using open source KST Plot analytical software.

The Mellow FLY-ADXL345 Accelerometer Sensor module was designed specifically for Klipper firmware, running on 3D printers, and used as a input shaper,
to compensation for resonance, and improving print quality. The unique property of this module is the Raspberry Pi Pico RP2040 processor, 2MB programmable flash memory, and the ability to be powered and communicate by USB-C serial port. The RP2040 operates as a Dual Core Cortex M0+ processor running at 133 MHz. The on board ADXL345 digital 3-axis accelerometer is capable of sampling rates of up to 3,200 samples per second.

The FLY-ADXL345 PCB connects the RP2040 processor pins with the Analog Devices ADXL345 sensor via four-wire SPI, and ADXL345 interrupt pin INT1 with RP2040's GPIO28.

<img width="654" height="549" alt="image" src="https://github.com/user-attachments/assets/a60c9aa8-47ce-4cd8-ab3d-b57737152a37" />
<img width="636" height="614" alt="image" src="https://github.com/user-attachments/assets/9978c39c-5510-48f9-929e-73fd4a2b3df7" />

With some simple mounting hardware, the FLY-ADXL345 can be quickly setup on magnetic surfaces, for data sampling purposes.

<img width="534" height="708" alt="image" src="https://github.com/user-attachments/assets/fb80ecd7-aec9-47d1-9c17-f24f6c9ecba6" />

<img width="615" height="666" alt="image" src="https://github.com/user-attachments/assets/50ae8424-ded6-4bab-acdc-b0eb8b16813a" />

With the custom Raspberry Pi Pico firmware provided in this repository, 3-axis acceleration sampling dataset with binary streaming, is possible at sampling rates up to 3,200 Hz.  And using Microsoft PowerShell terminal with Python script files provided, sampling data can be saved as CSV files, for direct loading in the high performance KST Plot analytical plotting software.

This project is described mostly for using a Windows PC, however Microsoft PowerShell terminal and KST Plot software are also available for Apple Mac OS and Linux OS.
