from flask import Flask
from flask import request, jsonify
#from flask_cors import CORS, cross_origin
from werkzeug import secure_filename
import os, subprocess, json
from subprocess import call
import base64

app = Flask(__name__)
#CORS(app)

app.config['UPLOAD_FOLDER'] = '/tmp/inception_img/'

temp_image = app.config['UPLOAD_FOLDER'] + 'tempimage'

ALLOWED_EXTENSIONS = set(['ppm', 'png', 'jpg', 'jpeg', 'gif', 
    'PNG', 'JPG', 'JPEG'])
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/image', methods=['GET', 'POST', 'OPTIONS'])
def index():
    if request.method == 'GET':
        imgstring = request.args.get('key', '')
        #if not (f and allowed_file(f.filename)):
        #    app.logger.info('image format not supported.')
        #    return [] #jsonify(error='ext name error')

        imagedata = base64.b64decode(imgstring)
        print "fuck!"
        print len(imagedata)
        with open('/home/jz402/Desktop/foo.jpg', "wb") as img:
            img.write(imagedata)
        #    imagedata = base64.b64decode(imgstring)
        #    encoded_string = base64.b64encode(img.read())
        # filename = secure_filename(f.filename)
        # file_addr = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # f.save(file_addr)

        #img_addr, img_extension = os.path.splitext(file_addr)
        new_img_addr = 'temp.ppm'
        comm = "convert " + temp_image +  " -resize " + "299x299\\! " + new_img_addr
        os.system(comm)
        ##resp = subprocess.check_output(['inception_service', new_img_addr])
        resp = subprocess.check_output(['ls', app.config['UPLOAD_FOLDER']])
        return jsonify(resp)
    return ""

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)