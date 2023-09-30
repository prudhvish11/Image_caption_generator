from flask import Flask, render_template, url_for, request, redirect
from caption import *
import warnings
warnings.filterwarnings("ignore")



app = Flask(__name__)




@app.route("/predict", methods=['GET'])
def text2():
    return render_template('index.html')


@app.route('/', methods = ['GET', 'POST'])
def upload_file():
	result_dic = {}
	if request.method == 'POST':
		img = request.files['image']

		# print(img)
		# print(img.filename)

		img.save("static/"+img.filename)

	
		caption = caption_this_image("static/"+img.filename)



		
		result_dic = {
			'image' : "static/" + img.filename,
			'description' : caption
			#'url': /ans
		}
	return render_template('index.html', results = result_dic)



