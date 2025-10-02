from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/main', methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        print("Dostaliśmy POST!")
        print(request.form)
        return redirect('/main') 
    return render_template('main.html')

@app.route('/kontakt', methods = ['GET', 'POST'])
def kontakt():
    if request.method == 'POST':
        print('dostalismy post!!!!!')
        print(request.form)
        return redirect('/main')
    if request.method == 'GET':
        return render_template('podstrona.html')
