

from flask import Flask, render_template, request, send_file
import qrcode
from PIL import Image

app = Flask(__name__,template_folder='template',static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr_code', methods=['POST'])
def generate_qr_code():
    name = request.form['name']
    phone = request.form['phone']

    data = f"Name: {name}\nPhone: {phone}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_path = "static/qrcode.png"
    img.save(img_path)

    return send_file(img_path, as_attachment=True)

# if __name__ == "__main__":
#     app.run(debug=True)
