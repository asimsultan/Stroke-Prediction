from flask import Flask, render_template, request
import pickle
import numpy as np
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
   result = ''
   if request.method == 'POST':
      # gender = request.form['gender']
      # age = request.form['age']
      # hypertension = request.form['hypertension']
      # heartdisease = request.form['heartdisease']
      # married = request.form['married']
      # worktype = request.form['worktype']
      # residence = request.form['residence']
      # glucoselevel = request.form['glucoselevel']
      # bmi = request.form['bmi']
      # smoking = request.form['smoking']
      int_features = [int(x) for x in request.form.values()]

      train = [int_features]

      with open('StrokePrediction.pkl','rb') as f:
         model = pickle.load(f)

      score = model.predict(train)
      score = score[0]*100

      if(score==0):
         res = 'the patient will not have Stroke'
      else:
         res = 'the patient will have Stroke'

      result = 'Given the above values, it is predicted that {}'.format(res)

   return render_template('intro.html', result=result)

if __name__ == '__main__':
   app.run()