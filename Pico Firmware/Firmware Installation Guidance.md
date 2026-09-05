This is a guide for installing Pi Pico firmware file.

First download the Pico firmware uf2 file from this repository.

Installing the firmware on the Raspberry Pi Pico does not require any special programming hardware.
All that is necessary is to place the FLY Pi Pico in bootloader mode. This is done by attaching a USB data cable
to the FLY Pi Pico USB-C port, then pressing down on the BOOTSEL button on the Pico PCB while plugging in
the other end of the USB cable into the PC running Windows.  A File Explorer window should appear on
the Windows desktop identifying a new device being installed called 'RP2 Boot'.  To install the firmware, simply 
copy and paste, or drag and drop, the uf2 file from another File Explorer window in the directory where the uf2
firmware file is located. This will immediately flash the firmware onto the FLY Pi Pico, cause the Pico to exit
the bootloader mode, closes the Windows File Explorer device window, and then boot the firmware program.  Windows
should then recognize the Pico as a USB device.

You can verify the FLY Pi Pico device and Windows assigned COM Port using the Windows Device Manager.  Look for it
in the Device Manager, listed under 'Ports (COM & LPT), as 'USB Serial Device', with the COM number assigned.
