
from flask import Flask, render_template, request
import random
import string
import random

app = Flask(__name__)


def generate_password(length=12,uppercase=True,digits=True,special_chars=True):
    characters = list("abcdefghijklmnopqrstuvwxyz")
    if uppercase==True:
        characters += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if digits==True:
        characters += list("0123456789")
    if special_chars==True:
        characters += ("!^&*()-$%_@#=+[]}|{;:,.<>?")
    password = ''.join(random.choice(characters) for _ in range(length))

    return password
@app.route('/', methods=['GET', 'POST'])
def home():
    password = ''
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        uppercase = 'uppercase' in request.form
        digits = 'digits' in request.form
        special_chars = 'special_chars' in request.form
        password = generate_password(length, uppercase, digits, special_chars)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)