bluetooth.onBluetoothConnected(function () {
    bluetooth_connected = true
    bluetooth.uartWriteNumber(0)
    basic.showIcon(IconNames.Heart)
})
bluetooth.onBluetoothDisconnected(function () {
    bluetooth_connected = false
    basic.showIcon(IconNames.TShirt)
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(input.lightLevel())
})
input.onGesture(Gesture.Shake, function () {
    serial.writeLine("Shaked")
    basic.showIcon(IconNames.Butterfly)
    if (bluetooth_connected) {
        bluetooth.uartWriteNumber(5)
    }
})
let lastLightState = false
let lightState = false
let lightlevel = 0
let lastState = false
let presentstate = false
let bluetooth_connected = false
basic.showIcon(IconNames.SmallSquare)
serial.writeLine("Intruder Detection")
basic.forever(function () {
    presentstate = input.pinIsPressed(TouchPin.P0)
    if (lastState != presentstate) {
        if (presentstate == true) {
            serial.writeLine("Released")
            if (bluetooth_connected) {
                bluetooth.uartWriteNumber(1)
            }
            basic.showIcon(IconNames.No)
        } else {
            serial.writeLine("Pressed")
            if (bluetooth_connected) {
                bluetooth.uartWriteNumber(2)
            }
            basic.showIcon(IconNames.Yes)
        }
    }
    lastState = presentstate
    lightlevel = input.lightLevel()
    // serial.write_line("" + str((lightlevel)))
    if (lightlevel <= 15) {
        lightState = false
    } else {
        lightState = true
    }
    if (lastLightState != lightState) {
        if (lightState == true) {
            serial.writeLine("Lighton")
            if (bluetooth_connected) {
                bluetooth.uartWriteNumber(3)
            }
            basic.showIcon(IconNames.Asleep)
        } else {
            serial.writeLine("Lightoff")
            if (bluetooth_connected) {
                bluetooth.uartWriteNumber(4)
            }
            basic.showIcon(IconNames.SmallDiamond)
        }
    }
    lastLightState = lightState
})
