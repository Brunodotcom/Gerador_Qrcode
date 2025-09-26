import qrcode
from PIL import Image
from flask import Flask, render_template, request
import os


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        link = request.form.get('INPUT')
        if not link:
            return render_template('index.html', enviado=False, erro='Por favor, insira um link válido.')


        filename = f'qr_{abs(hash(link))}.png'
        path = os.path.join('static', filename)

        img = qrcode.make(link)
        img.save(path)

        return render_template('index.html', enviado=True, img=filename)
    return render_template('index.html', enviado=False)

if __name__ == '__main__':
    app.run()