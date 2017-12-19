# makey-rpi-lights

# INSTALL

```
sudo apt install python3-pigpio
```

Allow remote GPIO in dest raspberry pi

# RUN

## in dest raspberry pi

```
sudo pigpiod
```

## local

```
PIGPIO_ADDR=192.168.1.3 python intell.py
```
