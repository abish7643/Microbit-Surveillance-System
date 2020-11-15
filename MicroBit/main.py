def on_bluetooth_connected():
    global bluetooth_connected
    bluetooth_connected = True
    bluetooth.uart_write_number(0)
    basic.show_icon(IconNames.HEART)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global bluetooth_connected
    bluetooth_connected = False
    basic.show_icon(IconNames.TSHIRT)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    basic.show_number(input.light_level())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    serial.write_line("Shaked")
    basic.show_icon(IconNames.BUTTERFLY)
    if bluetooth_connected:
        bluetooth.uart_write_number(5)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

lastLightState = False
lightState = False
lightlevel = 0
lastState = False
presentstate = False
bluetooth_connected = False
basic.show_icon(IconNames.SMALL_SQUARE)
serial.write_line("Intruder Detection")

def on_forever():
    global presentstate, lastState, lightlevel, lightState, lastLightState
    presentstate = input.pin_is_pressed(TouchPin.P0)
    if lastState != presentstate:
        if presentstate == True:
            serial.write_line("Released")
            if bluetooth_connected:
                bluetooth.uart_write_number(1)
            basic.show_icon(IconNames.NO)
        else:
            serial.write_line("Pressed")
            if bluetooth_connected:
                bluetooth.uart_write_number(2)
            basic.show_icon(IconNames.YES)
    lastState = presentstate
    lightlevel = input.light_level()
    # serial.write_line("" + str((lightlevel)))
    if lightlevel <= 15:
        lightState = False
    else:
        lightState = True
    if lastLightState != lightState:
        if lightState == True:
            serial.write_line("Lighton")
            if bluetooth_connected:
                bluetooth.uart_write_number(3)
            basic.show_icon(IconNames.ASLEEP)
        else:
            serial.write_line("Lightoff")
            if bluetooth_connected:
                bluetooth.uart_write_number(4)
            basic.show_icon(IconNames.SMALL_DIAMOND)
    lastLightState = lightState
basic.forever(on_forever)
