from PIL import Image
import numpy as np
from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import base64
import io

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = "./static"
Bootstrap(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def image_upload():
    # coef_dict = request.form.to_dict()
    # filter_matrix = []
    # for key in coef_dict:
    #     filter_matrix.append(coef_dict[key])
    # filter_matrix = np.array(filter_matrix, dtype=np.int8)
    # filter_matrix = filter_matrix.reshape((5, 5))
    # img = request.files.get('image')
    # data = io.BytesIO()
    # img.save(data)
    # encoded_img_data = base64.b64encode(data.getvalue())
    # up_img = Image.open(img)
    # up_img = up_img.resize((1200, 1200), Image.ANTIALIAS)
    # red, green, blue = up_img.split()
    # grn_arr = np.array(green)
    # red_arr = np.array(red)
    # blue_arr = np.array(blue)
    #
    # blur_g = np.array(
    #     [[min(max(np.sum(filter_matrix * grn_arr[5 * i:5 * i + 5, 5 * j:5 * j + 5]), 0), 255) for j in range(240)]
    #      for i in range(240)], dtype=np.int8)
    # out_green = Image.fromarray(blur_g, 'L')
    #
    # blur_r = np.array(
    #     [[min(max(np.sum(filter_matrix * red_arr[5 * i:5 * i + 5, 5 * j:5 * j + 5]), 0), 255) for j in range(240)]
    #      for i in range(240)], dtype=np.int8)
    # out_red = Image.fromarray(blur_r, 'L')
    #
    # blur_b = np.array(
    #     [[min(max(np.sum(filter_matrix * blue_arr[5 * i:5 * i + 5, 5 * j:5 * j + 5]), 0), 255) for j in range(240)]
    #      for i in range(240)], dtype=np.int8)
    # out_blue = Image.fromarray(blur_b, 'L')
    #
    # output = np.dstack((out_red, out_green, out_blue))
    #
    # out_img = Image.fromarray(output, 'RGB')
    # f_data = io.BytesIO()
    # out_img.save(f_data, 'JPEG')
    # encoded_f_img_data = base64.b64encode(f_data.getvalue())
    # return render_template('index.html', img_data=encoded_img_data.decode('utf-8'),
    #                        filter_img_data=encoded_f_img_data.decode('utf-8'))
    print(request)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
