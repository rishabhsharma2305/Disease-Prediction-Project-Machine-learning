from flask import Flask, request, render_template
import ML_Model as ml
app= Flask(__name__)

def res(a=0):
    return a

@app.route("/", methods=['GET','POST'])
def home():
    return render_template("updated.html")

@app.route("/result", methods=['GET','POST'])
def result():
    if request.method=='POST':
        person_age= int(request.form.get("age") )
        person_cp= int(request.form.get("cp"))
        person_heart_rate= int(request.form.get("heart_rate"))
        person_exang= int(request.form.get("exang"))
        person_depp= float(request.form.get("depp"))
        person_slope= int(request.form.get("slope"))
        person_vessels= int(request.form.get("vessels"))
        ans= ml.calcutale_result(person_age, person_cp, person_heart_rate, person_exang, person_depp, person_slope, person_vessels)
        if ans==0:
            return render_template("updated.html", val= "You are safe")
    return render_template("updated.html", val= "You are at risk")
if __name__=='__main__':
    app.run(debug=True)