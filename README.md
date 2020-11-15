## Microbit - Flask WebApp

A Flask WebApp receiving serial data from microbit & updates realtime with SocketIO and publishes states to a configurable MQTT Server (Adafruit IO).

#### Demo

![Normal](https://github.com/abish7643/microbit-serial-bluetooth/blob/master/Demo/WebApp_Demo/WebApp_Demo_0.png)

#### Run Flask

Navigate to Flask Web App Folder & Open Terminal

- Install Dependencies
  
  ```bash
  pip3 install flask flask_socketio flask_serial flask_mqtt
  ```
- Add Environment Variables
  
  ```bash
  export FLASK_APP=app FLASK_ENV=development FLASK_DEBUG=1
  ```
- Run Flask App
  
  ```bash
  flask run
  ```


## Blocks

Microbit is connected to a PIR Sensor, & inbuilt Light Sensor (Microbit's LED Array) & Accelerometer (To Detect Movement).

![A rendered view of the blocks](https://github.com/abish7643/microbit-serial-bluetooth/raw/master/MicroBit/.github/makecode/blocks.png)

#### Note

- Replace Radio With Bluetooth
- Enable "Anyone Can Pair" in Project Settings
  ![Project Settings](https://github.com/abish7643/Microbit-Surveillance-System/blob/master/MicroBit/Bluetooth%20ProjectSetting.png)

## BLE Test

Download [Nrf Connect For Mobile](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp&hl=en_IN&gl=US)

![Connect](https://github.com/abish7643/microbit-serial-bluetooth/raw/master/Demo/BLE_Demo/BLE_Demo.png)


## Adafruit Dashboard

Create a new dashboard and add feeds. Feeds will be automatically created if the WebApp Published to an Adafruit Feed. Or else you can manually create two feeds, then add it to the dashboard. Make sure that you replace the topic with the new feed name if you're following the latter.

![Adafruit IO](https://github.com/abish7643/microbit-serial-bluetooth/raw/master/Demo/Adafruit-IFTTT_Demo/AdafruitDash_Demo.png)

## IFTTT

Create a Adafruit Feed - Notification Applet
![IFTTT Config](https://github.com/abish7643/microbit-serial-bluetooth/raw/master/Demo/Adafruit-IFTTT_Demo/IFTTT_Demo.png)

## Miscellaneous

#### Serial Client (Python)

Note : Tested only on Linux (Ubuntu 20.10)

Navigate to the Serial Client Folder & Open Terminal

- Install PySerial
  ```bash
  pip3 install pyserial
  ```
- Run Python Client
  ```bash
  python3 SerialMicrobBit.py
  ```
