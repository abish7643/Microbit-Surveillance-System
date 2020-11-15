from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_serial import Serial
from flask_mqtt import Mqtt
from datetime import datetime

now = datetime.now()
date = now.strftime('%B %d')
time = now.strftime('%H : %M')
print("date_time:", date, time)

pir_state = False
light_state = False
shake_state = False
formated_msg = ''

# Replace 'username' With Adafruit Username
topic_pir = 'username/feeds/microbitpir'
topic_light = 'username/feeds/microbitlight'
topic_shake = 'username/feeds/microbitshake'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
app.config['SERIAL_TIMEOUT'] = 0
app.config['SERIAL_PORT'] = '/dev/ttyACM1'
app.config['SERIAL_BAUDRATE'] = 115200
app.config['SERIAL_BYTESIZE'] = 8
app.config['SERIAL_PARITY'] = 'N'
app.config['SERIAL_STOPBITS'] = 1

# Adafruit IO
# Replace MQTT_USERNAME and MQTT_PASSWORD with Adafruit Username & AIO Key
app.config['MQTT_BROKER_URL'] = 'io.adafruit.com'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'username'
app.config['MQTT_PASSWORD'] = 'aio_key'
app.config['MQTT_REFRESH_TIME'] = 1.0

# Eclipse
# app.config['MQTT_BROKER_URL'] = 'mqtt.eclipse.org'
# app.config['MQTT_BROKER_PORT'] = 1883
# app.config['MQTT_USERNAME'] = 'mircobit'
# app.config['MQTT_PASSWORD'] = 'bbcmicrobit78'
# app.config['MQTT_REFRESH_TIME'] = 1.0

ser = Serial(app)
mqtt = Mqtt(app)
socketio = SocketIO(app)

@app.route('/')
def index():
    global date, time
    data = {
        'title': 'MicroBit \n Surveillance',
        'running_since_date': date,
        'running_since_time': time
    }
    return render_template('index.html', data=data)

@socketio.on('get_state')
def on_create(data):
    print(data)
    socketio.sleep()
    # socketio.emit('state_from_server', {'pir_state': pir_state}, broadcast=True)

@ser.on_message()
@socketio.on('serial_message')
def handle_message(msg):
    msg = msg.decode('Ascii')
    # msg = msg.strip()
    global pir_state, light_state, shake_state
    global formated_msg
    global topic_pir, topic_light
    # global prev_now

    # print(msg)
    if ("Pressed" in msg):
        formated_msg = 'Pressed'
        pir_state = True
        print("receive a message:", formated_msg)
        socketio.emit('pir_state', {"pir_state": pir_state})
        mqtt.publish(topic=topic_pir, payload=pir_state)
    elif ("Released" in msg):
        formated_msg = 'Released'
        pir_state = False
        print("receive a message:", formated_msg)
        socketio.emit('pir_state', {"pir_state": pir_state})
        mqtt.publish(topic=topic_pir, payload=pir_state)
    elif ("Lighton" in msg):
        formated_msg = 'Lighton'
        light_state = True
        print("receive a message:", formated_msg)
        socketio.emit('light_state', {"light_state": light_state})
        mqtt.publish(topic=topic_light, payload=light_state)
    elif ("Lightoff" in msg):
        formated_msg = 'Lightoff'
        light_state = False
        print("receive a message:", formated_msg)
        socketio.emit('light_state', {"light_state": light_state})
        mqtt.publish(topic=topic_light, payload=light_state)
    elif ("Shaked" in msg):
        formated_msg = 'Shaked'
        shake_state = True
        print("receive a message:", formated_msg)
        socketio.emit('shake_state', {"shake_state": shake_state})
        mqtt.publish(topic=topic_shake, payload=shake_state)


@ser.on_log()
def handle_logging(level, info):
    # print(level, info)
    pass

if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', debug=True)
