from PIL import Image
import numpy as np
from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import base64
import io

FILTER = np.array([[-1, 0, 1], [0, 0, 0], [1, 0, -1]], dtype=np.int8)

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = "./static"
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/image-upload', methods=['GET', 'POST'])
def image_upload():
    if request.method == "POST":
        if request.files:
            img = request.files.get('image')
            print("img recieved")
            data = io.BytesIO()
            img.save(data)
            encoded_img_data = base64.b64encode(data.getvalue())
            up_img = Image.open(img)
            red, green, blue = up_img.split()
            grn_arr = np.array(green)
            red_arr = np.array(red)
            blue_arr = np.array(blue)

            blur_g = np.array(
                [[min(max(np.sum(FILTER * grn_arr[3 * i:3 * i + 3, 3 * j:3 * j + 3]), 0), 255) for j in range(400)]
                 for i in range(400)], dtype=np.int8)
            out_green = Image.fromarray(blur_g, 'L')

            blur_r = np.array(
                [[min(max(np.sum(FILTER * red_arr[3 * i:3 * i + 3, 3 * j:3 * j + 3]), 0), 255) for j in range(400)]
                 for i in range(400)], dtype=np.int8)
            out_red = Image.fromarray(blur_r, 'L')

            blur_b = np.array(
                [[min(max(np.sum(FILTER * blue_arr[3 * i:3 * i + 3, 3 * j:3 * j + 3]), 0), 255) for j in range(400)]
                 for i in range(400)], dtype=np.int8)
            out_blue = Image.fromarray(blur_b, 'L')

            output = np.dstack((out_red, out_green, out_blue))

            out_img = Image.fromarray(output, 'RGB')
            f_data = io.BytesIO()
            out_img.save(f_data, 'JPEG')
            encoded_f_img_data = base64.b64encode(f_data.getvalue())
            return render_template('index.html', img_data=encoded_img_data.decode('utf-8'),
                                   filter_img_data=encoded_f_img_data.decode('utf-8'))
    return render_template('image-upload.html')


# FILTER = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]], dtype=np.int8)
# # FILTER = np.ones((3, 3), dtype=np.int8)
# print(FILTER)
# img = Image.open("etower.jpg")
# img.load()
# img.show()
# array = np.array(img)
#
# # R = np.array([[[0*val[2], 0*val[2], val[2]] for val in row] for row in array], dtype=np.uint8)red
#
#
# red, green, blue = img.split()
# grn_arr = np.array(green)
# red_arr = np.array(red)
# blue_arr = np.array(blue)
#
# blur_g = np.array(
#     [[min(max(np.sum(FILTER * grn_arr[3 * i:3 * i + 3, 3 * j:3 * j + 3]), 0), 255) for j in range(400)]
#      for i in range(400)], dtype=np.int8)
# out_green = Image.fromarray(blur_g, 'L')
#
# blur_r = np.array(
#     [[min(max(np.sum(FILTER * red_arr[3 * i:3 * i + 3, 3 * j:3 * j + 3]), 0), 255) for j in range(400)]
#      for i in range(400)], dtype=np.int8)
# out_red = Image.fromarray(blur_r, 'L')
#
# blur_b = np.array(
#     [[min(max(np.sum(FILTER * blue_arr[3 * i:3 * i + 3, 3 * j:3 * j + 3]), 0), 255) for j in range(400)]
#      for i in range(400)], dtype=np.int8)
# out_blue = Image.fromarray(blur_b, 'L')
#
#
# output = np.dstack((out_red, out_green, out_blue))
#
# out_img = Image.fromarray(output, 'RGB')
# out_img.load()
# out_img.show()


if __name__ == '__main__':
    app.run(debug=True)
