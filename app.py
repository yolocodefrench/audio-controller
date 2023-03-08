from flask import Flask, render_template, request
from correspondance import db_list
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

app = Flask(__name__)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

@app.route('/', methods=['POST', 'GET'])
def index():
    error = None
    if request.method == 'POST':
        volume.SetMasterVolumeLevel(db_list[int(request.form['volume'])], None)
    
    return render_template('index.html', volume=get_nearest_volume_index(volume.GetMasterVolumeLevel()))

def get_nearest_volume_index(value):
    list_items = tuple(db_list.items())

    for index, v in list_items:
        if value <= v:
            return index
            