from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from Ham.Sat.Flask import app


class ReusableForm(Form):
    name = StringField('Name:', validators=[validators.required()])


print("adding /frm")
@app.route("/frm", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    if request.method == 'POST':
        name = request.form['name']

        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')

    return render_template('hello.html', form=form)
