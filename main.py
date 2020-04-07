from flask import Flask, render_template, request
app = Flask(__name__)
import pickle



file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        myDict = request.form
        # print(myDict)
        # print(myDict[])
        # print("hi")
        fever = int(myDict["fever"])
        age = int(myDict["age"])
        bodyPain = int(myDict["bodyPain"])
        runnyNose = int(myDict["runnyNose"])
        diffBreath = int(myDict["diffBreath"])
        # code for prediction
        inputFeatures = [fever,bodyPain,age,runnyNose,diffBreath]
        infProb = clf.predict_proba([inputFeatures])[0][1]
        infProb = round(infProb * 100)
        # return 'Hello,word!!!' + str(infProb)
        return render_template('show.html', inf=infProb)
    return render_template('index.html')

@app.route('/aboutus')
def aboutUs():
    return render_template('aboutus.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug = True)