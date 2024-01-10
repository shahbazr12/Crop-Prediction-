from flask import Flask,render_template,jsonify,request
import pickle
import json
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/prediction',methods=['GET','post'])
def prediction():
    if request.method=="POST":
        nitro = request.form.get("nitrogen")
        phos = request.form.get("phosphorous")
        kp = request.form.get("potassium")
        temp = request.form.get("temperature")
        hum = request.form.get("humidity")
        ph =request.form.get("ph")
        rain = request.form.get("rainfall")

        print(nitro,phos,kp,temp,hum,ph,rain)
        with open("model.pkl","rb") as model_file:
            mlmodel=pickle.load(model_file)

        res = mlmodel.predict([[float(nitro),float(phos),float(kp),float(temp),float(hum),float(ph),float(rain)]])
        return render_template("result.html",res=res[0])
    
    


    else:
        return  render_template("prediction.html")


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5050)


