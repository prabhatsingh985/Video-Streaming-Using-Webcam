from flask import Flask,redirect,url_for,render_template,Response
import cv2
# WSGI APPLILCTION
app = Flask(__name__)

app=Flask(__name__)
camera = cv2.VideoCapture(0) 

def func():
     while True:
    #  read the camera frame
        success , frame=camera.read()
        if not success:
            break
        else:
            #  incode the frame
             ret,buffer = cv2.imencode('.jpg',frame)
             frame=buffer.tobytes()
        
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')         
             

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
       return Response(func(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    app.run(debug=True)
 
 

