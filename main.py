from PIL import Image
import numpy as np
from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import base64
import io

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = "./static"
app.config['MAX_CONTENT_LENGTH'] = 2*1000*1000
Bootstrap(app)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html', extn_error=False)


@app.route('/filtered', methods=['POST'])
def image_upload():
    coef_dict = request.form.to_dict()
    filter_matrix = []
    for key in coef_dict:
        filter_matrix.append(coef_dict[key])
    img = request.files.get('image')
    if img and allowed_file(img.filename):
        data = io.BytesIO()
        img.save(data)
        encoded_img_data = base64.b64encode(data.getvalue())
        up_img = Image.open(img)
        width = up_img.size[0]
        height = up_img.size[1]
        resized_width = width - width % 15
        resized_height = height - height % 15
        up_img = up_img.resize((resized_width, resized_height), Image.ANTIALIAS)
        red, green, blue = up_img.split()
        grn_arr = np.array(green)
        red_arr = np.array(red)
        blue_arr = np.array(blue)
        if coef_dict['inlineRadioOptions'] == 'single':
            filter_matrix = filter_matrix[1:]
            filter_matrix = np.array(filter_matrix, dtype=np.int8)
            filter_matrix = filter_matrix.reshape((5, 5))
            new_width_range = int(resized_width / 5)
            new_height_range = int(resized_height / 5)
            blur_g = np.array(
                [[min(max(np.sum(filter_matrix * grn_arr[5 * i:5 * i + 5, 5 * j:5 * j + 5]), 0), 255) for j in range(new_width_range)]
                 for i in range(new_height_range)], dtype=np.int8)
            out_green = Image.fromarray(blur_g, 'L')

            blur_r = np.array(
                [[min(max(np.sum(filter_matrix * red_arr[5 * i:5 * i + 5, 5 * j:5 * j + 5]), 0), 255) for j in range(new_width_range)]
                 for i in range(new_height_range)], dtype=np.int8)
            out_red = Image.fromarray(blur_r, 'L')

            blur_b = np.array(
                [[min(max(np.sum(filter_matrix * blue_arr[5 * i:5 * i + 5, 5 * j:5 * j + 5]), 0), 255) for j in range(new_width_range)]
                 for i in range(new_height_range)], dtype=np.int8)
            out_blue = Image.fromarray(blur_b, 'L')
        else:
            filter_matrix_r = []
            filter_matrix_g = []
            filter_matrix_b = []
            filter_matrix_r = filter_matrix[1:10]
            filter_matrix_r = np.array(filter_matrix_r, dtype=np.int8)
            filter_matrix_r = filter_matrix_r.reshape((3, 3))
            filter_matrix_g = filter_matrix[10:19]
            filter_matrix_g = np.array(filter_matrix_g, dtype=np.int8)
            filter_matrix_g = filter_matrix_g.reshape((3, 3))
            filter_matrix_b = filter_matrix[19:]
            filter_matrix_b = np.array(filter_matrix_b, dtype=np.int8)
            filter_matrix_b = filter_matrix_b.reshape((3, 3))

            new_width_range = int(resized_width / 3)
            new_height_range = int(resized_height / 3)

            blur_g = np.array(
                [[min(max(np.sum(filter_matrix_g * grn_arr[3 * i:3 * i + 3, 3 * j:3 * j + 3])/9, 0), 255) for j in range(new_width_range)]
                 for i in range(new_height_range)], dtype=np.int8)
            out_green = Image.fromarray(blur_g, 'L')

            blur_r = np.array(
                [[min(max(np.sum(filter_matrix_r * red_arr[3 * i:3 * i + 3, 3 * j:3 * j + 3])/9, 0), 255) for j in range(new_width_range)]
                 for i in range(new_height_range)], dtype=np.int8)
            out_red = Image.fromarray(blur_r, 'L')

            blur_b = np.array(
                [[min(max(np.sum(filter_matrix_b * blue_arr[3 * i:3 * i + 3, 3 * j:3 * j + 3])/9, 0), 255) for j in range(new_width_range)]
                 for i in range(new_height_range)], dtype=np.int8)
            out_blue = Image.fromarray(blur_b, 'L')
        output = np.dstack((out_red, out_green, out_blue))

        out_img = Image.fromarray(output, 'RGB')
        f_data = io.BytesIO()
        out_img.save(f_data, 'JPEG')
        encoded_f_img_data = base64.b64encode(f_data.getvalue())
        return render_template('index.html', img_data=encoded_img_data.decode('utf-8'),
                               filter_img_data=encoded_f_img_data.decode('utf-8'))
    else:
        return render_template('index.html', extn_error=True)


if __name__ == '__main__':
    app.run(debug=True)
