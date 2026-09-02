This is a guide for installing Pi Pico firmware.

Installing the firmware on the Raspberry Pi Pico does not require any special programming hardware.
All that is necessary is to place the FLY Pi Pico in bootloader mode. This is done by attaching a USB data cable
to the FLY Pi Pico USB-C port, then pressing down on the Boot button switch on the Pico PCB while plugging in
the other end of the USB cable into the PC while running Windows.  A File Manager Window should appear on
the Windows desktop identifying a new device being installed called 'RP2 Boot'.  To install the firmware, simply 
copy and paste or drag and drop the file from another File Manager Window from the directory where the firmware 
file is located.  This will immediately flash the firmware onto the FLY Pi Pico, exits the boot loader mode, which closes
the Windows File Manager Window device, and boots the program on the FLY Pi Pico.

You can verify the FLY Pi Pico device and Windows assigned COM Port using the Windows Device Manager.  Look for it
under 'Ports (COM & LPT), as 'USB Serial Device', with the COM number assigned.  Mine shows up as COM3.
