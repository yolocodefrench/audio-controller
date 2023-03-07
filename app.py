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
    
    volume_level = [k for k, v in db_list.items() if v == volume.GetMasterVolumeLevel()][0]
    
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('index.html', volume=volume_level)