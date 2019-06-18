from flask import Flask, render_template, request
from werkzeug import secure_filename
import main
app = Flask(__name__)

@app.route('/')
def upload_file1():
   return render_template('home.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      #try:
      print(f.filename)
      return main.main_run(f.filename)
      #except:
      print('error')
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = False)
