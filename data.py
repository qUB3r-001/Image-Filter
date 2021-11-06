DICT = [
    {
        "name": "Red Channel",
        "img": "static/images/red.png",
        "matrix": r'$$\begin{bmatrix}0 & 0 & 0 \\ 0 & 1 & 0\\0 & 0 & 0\end{bmatrix}_{Red}$$'
                  r'$$\begin{bmatrix}0 & 0 & 0 \\ 0 & 0 & 0\\0 & 0 & 0\end{bmatrix}_{Green}'
                  r'\begin{bmatrix}0 & 0 & 0 \\ 0 & 0 & 0\\0 & 0 & 0\end{bmatrix}_{Blue}$$',
        "info": "Red Channel is one of the 3 channels of a RGB image. These images are exclusively made up of "
                "shades of Red. The Red regions in the original image would be brighter in Red channel as compared "
                "to the other 2 channels.",
    },
    {
        "name": "Green Channel",
        "img": "static/images/green.png",
        "matrix": r'$$\begin{bmatrix}0 & 0 & 0 \\ 0 & 0 & 0\\0 & 0 & 0\end{bmatrix}_{Red}$$'
                  r'$$\begin{bmatrix}0 & 0 & 0 \\ 0 & 1 & 0\\0 & 0 & 0\end{bmatrix}_{Green}'
                  r'\begin{bmatrix}0 & 0 & 0 \\ 0 & 0 & 0\\0 & 0 & 0\end{bmatrix}_{Blue}$$',
        "info": "Green Channel is one of the 3 channels of a RGB image. These images are exclusively made up of "
                "shades of Green. The Green regions in the original image would be brighter in Green channel as"
                "compared to the other 2 channels.",
    },
    {
        "name": "Blue Channel",
        "img": "static/images/blue.png",
        "matrix": r'$$\begin{bmatrix}0 & 0 & 0 \\ 0 & 0 & 0\\0 & 0 & 0\end{bmatrix}_{Red}$$'
                  r'$$\begin{bmatrix}0 & 0 & 0 \\ 0 & 0 & 0\\0 & 0 & 0\end{bmatrix}_{Green}'
                  r'\begin{bmatrix}0 & 0 & 0 \\ 0 & 1 & 0\\0 & 0 & 0\end{bmatrix}_{Blue}$$',
        "info": "Blue Channel is one of the 3 channels of a RGB image. These images are exclusively made up of "
                "shades of Blue. The Blue regions in the original image would be brighter in Blue channel as compared "
                "to the other 2 channels.",
    },
    {
        "name": "Emboss",
        "img": "static/images/emboss.png",
        "matrix": r'$$ \begin{bmatrix}-2 & 0 & -1 & 0 & 0\\ 0 & -2 & -1 & 0 & 0\\-1 & -1 & 1 & 1 & 1\\0 & 0 & 1 '
                  r'& 2 & 0\\0 & 0 & 1 & 0 & 2\\\end{bmatrix}$$',
        "info": "A box blur (also known as a box linear filter) is a filter in which each pixel in the resulting "
                "image has a value equal to the average value of its neighboring pixels in the input image.",
    },
    {
        "name": "Edge Highlighter",
        "img": "static/images/edge-highlighter.png",
        "matrix": r'$$ \begin{bmatrix}'
                  r' 0 & 0 & 1 & 0 & 0\\'
                  r' 0 & 1 & 2 & 1 & 0\\'
                  r'1 & 2 & -15 & 2 & 1\\'
                  r'0 & 1 & 2 & 1 & 0\\'
                  r'0 & 0 & 1 & 0 & 0\\'
                  r'\end{bmatrix}$$',
        "info": "A box blur (also known as a box linear filter) is a filter in which each pixel in the resulting "
                "image has a value equal to the average value of its neighboring pixels in the input image.",
    },
    {
        "name": "Edge Detector",
        "img": "static/images/Lapacian-Filter-(edge-detection).png",
        "matrix": r'$$ \begin{bmatrix} '
                  r'-1 & -1 & -1 & -1 & -1\\'
                  r' -1 & -1 & -1 & -1 & -1\\'
                  r'-1 & -1 & 24 & -1 & -1\\'
                  r'-1 & -1 & -1 & -1 & -1\\'
                  r'-1 & -1 & -1 & -1 & -1\\'
                  r'\end{bmatrix}$$',
        "info": "A box blur (also known as a box linear filter) is a filter in which each pixel in the resulting "
                "image has a value equal to the average value of its neighboring pixels in the input image.",
    },
    {
        "name": "Horizontal Sobel",
        "img": "static/images/Hsobel.png",
        "matrix": r'$$ \begin{bmatrix}2 & 2 & 4 & 2 & 2\\ 1 & 1 & 2 & 1 & 1\\0 & 0 & 0 & 0 & 0\\-1 & -1 & -2'
                  r'& -1 & -1\\-2 & -2 & -4 & -2 & -2\\\end{bmatrix}$$',
        "info": "A box blur (also known as a box linear filter) is a filter in which each pixel in the resulting "
                "image has a value equal to the average value of its neighboring pixels in the input image.",
    },
    {
        "name": "Vertical Sobel",
        "img": "static/images/Vsobel.png",
        "matrix": r'$$ \begin{bmatrix}2 & 1 & 0 & -1 & -2\\ 2 & 1 & 0 & -1 & -2\\4 & 2 & 0 & -2 & -4\\'
                  r'2 & 1 & 0 & -1 & -2\\2 & 1 & 0 & -1 & -2\\\end{bmatrix}$$',
        "info": "A box blur (also known as a box linear filter) is a filter in which each pixel in the resulting "
                "image has a value equal to the average value of its neighboring pixels in the input image.",
    },
    {
        "name": "Box Blur",
        "img": "static/images/blur.png",
        "matrix": r'$$ 1/273*\begin{bmatrix}1 & 4 & 7 & 4 & 1\\ 4 & 16 & 26 & 16 & 4\\7 & 26 & 41 & 26 & 7\\4 & 16 & '
                  r'26 & 16 & 4\\1 & 4 & 7 & 4 & 1\\\end{bmatrix}$$',
        "info": "A box blur (also known as a box linear filter) is a filter in which each pixel in the resulting "
                "image has a value equal to the average value of its neighboring pixels in the input image.",
    },
    {
        "name": "Gaussian Blur",
        "img": "static/images/gaussian.png",
        "matrix": r'$$ 1/273*\begin{bmatrix}1 & 4 & 7 & 4 & 1\\ 4 & 16 & 26 & 16 & 4\\7 & 26 & 41 & 26 & 7\\4 & 16 & '
                  r'26 & 16 & 4\\1 & 4 & 7 & 4 & 1\\\end{bmatrix}$$',
        "info": "A box blur (also known as a box linear filter) is a filter in which each pixel in the resulting "
                "image has a value equal to the average value of its neighboring pixels in the input image.",
    },
    {
        "name": "Vertical Motion Blur",
        "img": "static/images/Vmotion.png",
        "matrix": r'$$ 1/35*'
                  r'\begin{bmatrix}'
                  r'0 & \cdots & 1 & \cdots & 0'
                  r'\\ 0 & \cdots & 1 & \cdots & 0\\'
                  r' \vdots & \vdots & \vdots & \vdots & \vdots\\'
                  r'0 & \cdots & 1 & \cdots & 0\\'
                  r'0 & \cdots & 1 & \cdots & 0\\'
                  r'\end{'
                  r'bmatrix}$$',
        "info": "A box blur (also known as a box linear filter) is a filter in which each pixel in the resulting "
                "image has a value equal to the average value of its neighboring pixels in the input image.",
    },
    {
        "name": "Horizontal Motion Blur",
        "img": "static/images/Hmotion.png",
        "matrix": r'$$ 1/35*'
                  r'\begin{bmatrix}0 & 0 & \cdots & 0 & 0\\'
                  r' \vdots & \vdots & \cdots & \vdots & \vdots\\ '
                  r'1 & 1 & \cdots & 1 & 1\\'
                  r'\vdots & \vdots & \cdots & \vdots & \vdots\\'
                  r'0 & 0 & \cdots & 0 & 0\\'
                  r'\end{'
                  r'bmatrix}$$',
        "info": "A box blur (also known as a box linear filter) is a filter in which each pixel in the resulting "
                "image has a value equal to the average value of its neighboring pixels in the input image.",
    },
]
