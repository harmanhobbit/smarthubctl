# smarthubctl
A simple python script for controlling Blackmagic Design Smart Videohub unit. This script is intended to allow for the control of a single unit over TCP/IP from the show control software QLab. However, it can also be run manually from a shell, where it should be cross-platform compatible.

This script is written in python V2, as this the default version that ships with macOS. If you have a different version of python running on your mac or PC I believe it will still work, however, I haven't had the chance to test it.

Input and output numbers are normalized by the script to allow for human numbering to be used.

# Usage
All methods of use require the <IP ADDRESS> placeholder to be changed for the IP address of the Smart Videohub unit. For example the line `address = "<IP ADDRESS>"` should read something like `address = "192.168.1.100"`.

Using the script from the command line called in the following way:
`python smarthubctl.py *input* *output*`

To allow the script to run from QLab, you need to call the python script from an AppleScript cue like so: 
`'do shell script "python /path/to/script/smarthubctl.py *input* *output*"'`
  
More details can be found here https://blog.allaway.tech/qlab/controlling-blackmagic-design-smart-videohubs-from-qlab/
