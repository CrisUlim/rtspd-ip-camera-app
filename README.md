# rtspd-ip-camera-app
App for ip camera using rtspd server


Hy, this application is for opening the rtspd and rtsp server.


# You need:
```
python 3.x.x,
customtkinter,
cv2.
```

# You can install them like this
For Linux, Ubuntu:
```
sudo apt install python3
pip3 install cv
pip3 install customtkinter
```
# RTSP and RTSPD format:
```
rtsp://admin:password@ip_address:port/cam/realmonitor?channel=1&subtype=1
rtsp://ip_address:port/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif
rtsp://ip_address:port/live
```

# RTSP routes:
```
/cam/realmonitor
/cam/realmonitor?channel=1&subtype=0
/cam/realmonitor?channel=1&subtype=1
/cam/realmonitor?channel=1&subtype=1&unicast=true&proto=Onvif

To change camera you must change channel=1, channel=2, channel=3, etc.
```
# Image

![Image](https://github.com/CrisUlim/rtspd-ip-camera-app/blob/main/Screenshot%20from%202022-08-08%2001-57-58.jpg)

You can add more camera changing the code.
