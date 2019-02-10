from flask import Flask, render_template, redirect, request, session

app = Flask('__name__')
app.secret_key = "development_key"

@app.route("/", methods=['POST', 'GET'])
def index():
    if 'goldNum' not in session:
        session['goldNum'] = 0
    if 'formType' not in session:
        session['formType'] = ''
    if 'activities' not in session:
        session['activities'] = []    
    
    return render_template("index.html", activities=session['activities'])

@app.route("/process_money", methods=['POST'])
def process_money():
    
    if request.form['building'] == 'farm':
        session['activities'].append('Earned 15 golds from the farm! (date)')
        session['goldNum'] = int(session['goldNum']) + 15

    if request.form['building'] == 'cave':
        session['activities'].append('Earned 7 golds from the cave! (date)')
        session['goldNum'] = int(session['goldNum']) + 7

    if request.form['building'] == 'house':
        session['activities'].append('Earned 5 golds from the house! (date)')
        session['goldNum'] = int(session['goldNum']) + 5

    if request.form['building'] == 'casino':
        session['activities'].append('Enter a casino and lost 50 golds ... Ouch... (date)')
        session['goldNum'] = int(session['goldNum']) - 50

    return redirect("/")

@app.route("/clear_session")
def clear_session():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)