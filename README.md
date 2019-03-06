# raspberry-temp-sensor
Raspberry Pi temperature recording

## Hardware Installation
Add 
```
w1-gpio
w1-therm
```
to ```/etc/modules```
and
```
dtoverlay=w1-gpio
```
to ```/boot/config.txt```

## Systemd Timer
Copy temp.timer to
	/etc/systemd/system/temp.timer

Copy temp.service to
	/etc/systemd/system/temp.service

Copy temp.py to
	/etc/systemd/system/temp.py
	
Copy temp.sh to
	/etc/systemd/system/temp.sh

Enable Timer
	systemctl enable temp


