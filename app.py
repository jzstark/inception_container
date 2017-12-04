from flask import Flask
from flask import request, jsonify
#from flask_cors import CORS, cross_origin
from werkzeug import secure_filename
import os, subprocess, json
from subprocess import call
import base64

app = Flask(__name__)
#CORS(app)

app.config['UPLOAD_FOLDER'] = '/tmp/inception_img/' #os.path.expanduser('~/Desktop/')


temp = app.config['UPLOAD_FOLDER'] + 'tempimage'
temp_ppm   = app.config['UPLOAD_FOLDER'] + 'temp.ppm'

ALLOWED_EXTENSIONS = set(['ppm', 'png', 'jpg', 'jpeg', 'gif', 
    'PNG', 'JPG', 'JPEG'])

@app.route('/')
def hello_world():
    return 'Hello, World!\n'

@app.route('/image', methods=['GET', 'POST', 'OPTIONS'])
def index():
    if request.method == 'GET':
        imgstring = request.args.get('content', '')
        img_type  = request.args.get('type', '')

        if img_type not in ALLOWED_EXTENSIONS :
            app.logger.info('image format not supported.')
            return jsonify(error='image format not supported.')

        imagedata = base64.b64decode(imgstring)
        temp_image = temp + '.' + img_type
        with open(temp_image, "wb") as img:
            img.write(imagedata)

        comm = "convert " + temp_image +  " -resize " + "299x299\\! " + temp_ppm
        os.system(comm)
        resp = subprocess.check_output(['app/inception_classifier', temp_ppm])
        return jsonify(resp)
    return ""

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)