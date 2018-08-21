#!/usr/bin/env python3
# from tryOn import TryOn as tryOn
from flask import Flask, render_template, Response,redirect,request
from camera import VideoCamera
import os
app = Flask(__name__)

@app.route('/tryon/<file_path>',methods = ['POST', 'GET'])
def tryon(file_path):
    file_path = file_path.replace(',','/')
    print(file_path)
    os.system('python3 tryOn.py ' + file_path)
    return redirect('http://127.0.0.1:5000/',code=302, Response=None)

@app.route('/pendant', methods=['POST', 'GET'])
def pendant():
    if request.method == 'GET':
        #users = mongo.db.users
        item = mongo.db.flipkart
        cart = mongo.db.cart
        existing_user = item.find_one({"Name" : "Pendant"})
        existing_user['Add_To_Cart'] = "1"
        item.save(existing_user)

        user = cart.find_one({"User" : "123"})
        user['Name'] = existing_user['Name']
        cart.save(user)
        #if existing_user['accept_request'] == "1" :
            #return render_template('StudentAccepted.html',student_status = existing_user)
        return render_template('pendant.html',final_cart = existing_user)

@app.route('/hangings', methods=['POST', 'GET'])
def hangings():
    if request.method == 'GET':
        #users = mongo.db.users
        item = mongo.db.flipkart
        cart = mongo.db.cart
        existing_user = item.find_one({"Name" : "Hangings"})
        existing_user['Add_To_Cart'] = "1"
        item.save(existing_user)

        user = cart.find_one({"User" : "123"})
        user['Name'] = existing_user['Name']
        cart.save(user)
        if existing_user['Add_To_Cart'] == "1" :
            return render_template('hangings.html',final_cart = existing_user)


@app.route('/place_order', methods=['POST', 'GET'])
def place_order():
    if request.method == 'GET':
        item = mongo.db.flipkart
        cart = mongo.db.cart
        existing_user = item.find_one({"Name" : "Pendant"})
        existing_user['Add_To_Cart'] = "1"
        item.save(existing_user)

        user = cart.find_one({"User" : "123"})
        user['Name'] = existing_user['Name']
        cart.save(user)
        if existing_user['Add_To_Cart'] == "1" :
            return render_template('FinalCart.html',final_cart = existing_user)

	
@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)