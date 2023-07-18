from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    message = request.form.get('message')
    if message:
        qr = qrcode.make(message)
        qr.save('static/qrcode.png')
        return render_template('result.html')
    else:
        return render_template('index.html', error="Please enter a message.")

if __name__ == '__main__':
    app.run(debug=True)
