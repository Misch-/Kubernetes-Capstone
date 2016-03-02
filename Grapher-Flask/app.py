from flask import Flask, render_template, request
import subprocess
import uuid
import os
app = Flask(__name__)

cmd1 = ["ansible-inventory-grapher", "-i", "hosts", "<hostname>"]
cmd2 = ["dot", "-Tpng"]
app.config['UPLOAD_FOLDER'] = '/tmp/'
app.config['ALLOWED_EXTENSIONS'] = set(['.tar.gz'])

def allowed_file(filename):
    return '.tar.gz' in filename

@app.route('/', methods=['GET', 'POST'])
def index(hostname=None):
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        print 1
        #file = request.files['tar']
        print 2
        #logging.debug('uploading file ' + file.filename)
        print 3
        #content = file.read()
        print 4
        #print content
        print 5
        #str() fixes bug where unicode output had an appended 'u' in python
        hostname = str(request.form['hostname'])
        cmd1[3] = hostname
        p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
        u = str(uuid.uuid4())
        fp = 'static/' + u + '.png'
        with open(fp , 'w') as png:
            p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stdout=png)
            p2.wait()
            size = os.path.getsize(fp)
        png.close()
        return render_template('output.html', hostname=hostname, u=u, size=size)
    #TODO, fix removal of files
        #time.sleep(5)
        #os.remove(fp)

        #tar tf ansible.tar | egrep "*hosts$" | head -n1

'''
@app.route('/import', methods= ['POST']) 
def import_objects():        
    file = request.files['file']
        logging.debug('uploading file ' + file.filename)
        if file and allowed_file(file.filename):
            #extract content 
            content = file.read()
            print content

            jsonResponse = json.dumps({'file_content':content})     
            response = Response(jsonResponse,  mimetype='application/json')
            return response
        else:
            abort(make_response("File extension not acceptable", 400))


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
'''

if __name__ == "__main__":
    app.run()
