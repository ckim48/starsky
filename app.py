from flask import Flask, render_template, redirect, url_for, flash

from flask import request
import cv2;
import numpy as np;
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.secret_key = b'_5#y2L'

@app.route('/', methods = ['POST', 'GET'])
def index():
	return render_template('index.html')

@app.route('/mainpro', methods = ['POST', 'GET'])
def mainpro():
	return render_template('mainpro.html')


@app.route('/mainpro2', methods = ['POST', 'GET'])
def mainpro2():
	    if request.method == 'POST':
	    	if request.files['file'].filename == '':
		          flash('No image file! Please upload the file.') 
		          return redirect(url_for('mainpro2'))
	    	file = request.files.get('file',None)
	    	

	    	print("AAAAAAAAAAAAAAA",file)
	    	filename = "mysite/starsky1/static/assets/img/abc_b.jpg"
	    	file.save(os.path.join(filename))

	    	img = cv2.imread('mysite/starsky1/static/assets/img/abc_b.jpg')
	    	template  = cv2.imread('mysite/starsky1/static/assets/img/template.png',0)
	    	w,h = template.shape[::-1]
	    	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	    	result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
	    	threh = 0.4
	    	loc = np.where(result>=threh)
	    	for pt in zip(*loc[::-1]):
	    		cv2.rectangle(img, pt, (pt[0]+w,pt[1]+h),(0,255,255),1)
	    	cv2.imwrite('mysite/starsky1/static/assets/img/abc_a.jpg', img, params=None)
	    	return render_template('mainpro2.html')
	    elif request.method == 'GET':
	    	return render_template('mainpro2.html')

if __name__ == '__main__':
	app.run(debug = True)


