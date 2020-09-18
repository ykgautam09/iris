from flask import Flask,request ,render_template
from model import predict_species

app=Flask(__name__,template_folder='templates')

@app.route('/')
def homepage():
    return render_template('index.html',flower='')

@app.route('/',methods=['POST'])
def predict():
    l=[]
    l.append(request.form.get('sepel_l'))
    l.append(request.form.get('sepel_w'))
    l.append(request.form.get('petal_l'))
    l.append(request.form.get('petal_w'))
    flower=predict_species(l)
    return render_template('index.html',flower=flower)

if __name__=='__main__':
    app.run(port=5000,debug=True)