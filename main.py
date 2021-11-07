import base64
import io
import time
import cv2
from random import randint

import numpy as np
from PIL import Image
from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap

from data import DICT

# DEMO_RESULT_ARRAY = [77, 40, 58, 66, 50, 82, 69, 87, 49, 78, 56, 47, 61, 60, 55, 83, 62, 53, 49, 64, 41, 42, 68,
# 57, 58]
DEMO_RESULT_ARRAY = [randint(40, 90) for i in range(25)]
DEMO_IMG_ARRAY = [80-2*i for i in range(25)]
DEMO_IMG_ARRAY = np.reshape(DEMO_IMG_ARRAY, (5, 5))
DEMO_IMG_ARRAY = np.pad(DEMO_IMG_ARRAY, ((1, 1), (1, 1)), 'constant', constant_values=255)
DEMO_IMG_ARRAY = DEMO_IMG_ARRAY.flatten()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = "./static"
app.config['MAX_CONTENT_LENGTH'] = 2 * 1000 * 1000
Bootstrap(app)


def convolve(image, filter_matrix, final_image):
    h = final_image.shape[0]
    w = final_image.shape[1]
    flat_filter = filter_matrix.flatten()
    for i in range(h):
        for j in range(w):
            flat_img = image[i:i + 3, j:j + 3].flatten('F')
            calc_value = np.sum(np.matmul(flat_filter, flat_img))
            final_image[i, j] = min(max(round(calc_value), 0), 255)
    return final_image


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    # corr_demo_img = []
    # for i in range(5):
    #     for j in range(5):
    #         temp = demo_img_to_js[i:i+3, j:j+3].flatten()
    #         corr_demo_img.append(temp)
    return render_template('index.html',
                           demo_result_array=DEMO_RESULT_ARRAY,
                           demo_img_array=DEMO_IMG_ARRAY, data=DICT)


@app.route('/filtered', methods=['POST'])
def image_upload():
    coef_dict = request.form.to_dict()
    filter_matrix = []
    for key in coef_dict:
        filter_matrix.append(coef_dict[key])
    img = request.files.get('image')
    # print(img)
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

        if up_img.mode == 'RGB':
            red_arr = np.array(up_img)[:, :, 0]
            grn_arr = np.array(up_img)[:, :, 1]
            blue_arr = np.array(up_img)[:, :, 2]
        else:
            red_arr = np.array(up_img)[:, :]
            grn_arr = np.array(up_img)[:, :]
            blue_arr = np.array(up_img)[:, :]

        if coef_dict.get('channel-mode-check') != 'on':
            factor = int(filter_matrix[-1])
            filter_matrix = filter_matrix[:-1]
            filter_matrix = np.array(filter_matrix, dtype=np.float32)
            filter_matrix = filter_matrix.reshape((5, 5))
            filter_matrix = filter_matrix / factor
            # print(filter_matrix)
            blur_g = cv2.filter2D(src=grn_arr, kernel=filter_matrix, ddepth=-1)
            out_green = Image.fromarray(blur_g, 'L')

            blur_r = cv2.filter2D(src=red_arr, kernel=filter_matrix, ddepth=-1)
            out_red = Image.fromarray(blur_r, 'L')

            blur_b = cv2.filter2D(src=blue_arr, kernel=filter_matrix, ddepth=-1)
            out_blue = Image.fromarray(blur_b, 'L')
        else:
            filter_matrix_r = filter_matrix[1:10]
            filter_matrix_r = np.array(filter_matrix_r, dtype=np.float32)
            filter_matrix_r = filter_matrix_r.reshape((3, 3))
            factor_r = int(filter_matrix[10])
            filter_matrix_r = filter_matrix_r / factor_r

            filter_matrix_g = filter_matrix[11:20]
            filter_matrix_g = np.array(filter_matrix_g, dtype=np.float32)
            filter_matrix_g = filter_matrix_g.reshape((3, 3))
            factor_g = int(filter_matrix[20])
            filter_matrix_g = filter_matrix_g / factor_g

            filter_matrix_b = filter_matrix[21:-1]
            filter_matrix_b = np.array(filter_matrix_b, dtype=np.float32)
            filter_matrix_b = filter_matrix_b.reshape((3, 3))
            factor_b = int(filter_matrix[-1])
            filter_matrix_b = filter_matrix_b / factor_b

            blur_g = cv2.filter2D(src=grn_arr, kernel=filter_matrix_g, ddepth=-1)
            out_green = Image.fromarray(blur_g, 'L')

            blur_r = cv2.filter2D(src=red_arr, kernel=filter_matrix_r, ddepth=-1)
            out_red = Image.fromarray(blur_r, 'L')

            blur_b = cv2.filter2D(src=blue_arr, kernel=filter_matrix_b, ddepth=-1)
            out_blue = Image.fromarray(blur_b, 'L')

        output = np.dstack((out_red, out_green, out_blue))
        out_img = Image.fromarray(output, 'RGB')
        f_data = io.BytesIO()
        out_img.save(f_data, 'JPEG')
        encoded_f_img_data = base64.b64encode(f_data.getvalue())
        time.sleep(2)
        return render_template('index.html', img_data=encoded_img_data.decode('utf-8'),
                               filter_img_data=encoded_f_img_data.decode('utf-8'),
                               demo_result_array=DEMO_RESULT_ARRAY,
                               demo_img_array=DEMO_IMG_ARRAY, data=DICT)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
