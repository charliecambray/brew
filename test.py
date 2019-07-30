from flask import Flask, render_template, request, redirect, url_for,flash
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
import time

app = Flask(__name__)


app.config['SECRET_KEY'] = 'fe85445f0c9ebbaaf12628c81e79c4bc'

nameList =['']
timeStampList=['']
drink = ''  
numberx=-1

class name(Form):
    username = StringField('username', validators=[DataRequired()])
    

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',nameList=nameList,timeStampList=timeStampList,numberx=numberx)


@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html',name=name)

@app.route('/thirsty', methods=['GET','POST'])
def register():
    form = name()
    if request.method == 'POST':
            if request.form["coffeetea"] == "WANT'S A COFFEE":
                nameList.insert(0,((str(form.data.get('username'))) + " wants a coffee").lower())
                timeStampList.insert(0,(str(time.strftime("%H:%M"))))
                drink = 'coffee'
                flash('coffee requested!')
                return redirect(url_for('requested'))
                
                           
            if request.form["coffeetea"] == "WANT'S A TEA":
                nameList.insert(0,((str(form.data.get('username'))) + " wants a tea").lower())
                timeStampList.insert(0,(str(time.strftime("%H:%M"))))
                drink = 'tea'
                flash('tea requested!') 
                return redirect(url_for('requested'))

            if request.form["coffeetea"] == "HOME":
                return redirect(url_for('home'))
            
    return render_template('register.html', title='thirsty', form=form)

@app.route('/success', methods=['GET','POST'])
def requested(drink='cuppa'):
    if request.method == 'POST':
        if request.form["returnHome"] == "HOME":
            return redirect(url_for('home'))
    else:        
        return render_template('requested.html',drink=drink)
    
@app.route('/clearcuppas', methods=['GET','POST'])
def clearcuppas():
    if request.method == 'POST':
        if request.form["clearList"] == "CLEAR CUPPAS":
            flash('cuppas cleared!')
            nameList.clear()
            return redirect(url_for('clearcuppas'))
        if request.form["clearList"] == "HOME":
            return redirect(url_for('home'))
    else:     
        return render_template('clear.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 8000)
