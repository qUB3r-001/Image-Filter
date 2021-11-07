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
        "info": "Image embossing is a technique in which each pixel of an image is replaced either by a highlight or "
                "a shadow, depending on light/dark boundaries on the original image. Low contrast areas are replaced "
                "by a gray background.",
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
        "info": "Laplacian Operator is a Second order derivative operator which is used to find edges in an image. "
                "The Laplacian is often applied to an image that has first been smoothed with something approximating "
                "a Gaussian smoothing filter in order to reduce its sensitivity to noise.",
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
        "info": "This kernel similar to Laplacian operator, it Highlights edges around the image. The edges around the "
                "region where there is a rapid change in intensity is highlighted while preserving the original image "
                "too thus creating a outlining effect.",
    },
    {
        "name": "Horizontal Sobel",
        "img": "static/images/Hsobel.png",
        "matrix": r'$$ \begin{bmatrix}2 & 2 & 4 & 2 & 2\\ 1 & 1 & 2 & 1 & 1\\0 & 0 & 0 & 0 & 0\\-1 & -1 & -2'
                  r'& -1 & -1\\-2 & -2 & -4 & -2 & -2\\\end{bmatrix}$$',
        "info": "It is a derivative mask used for Edge detection.This give more weight age to the pixel values around "
                "the edge region. This increase the edge intensity and it become enhanced comparatively to the "
                "original image.Horizontal Sobel operator highlights the horizontal edges.",
    },
    {
        "name": "Vertical Sobel",
        "img": "static/images/Vsobel.png",
        "matrix": r'$$ \begin{bmatrix}2 & 1 & 0 & -1 & -2\\ 2 & 1 & 0 & -1 & -2\\4 & 2 & 0 & -2 & -4\\'
                  r'2 & 1 & 0 & -1 & -2\\2 & 1 & 0 & -1 & -2\\\end{bmatrix}$$',
        "info": "It is a derivative mask used for Edge detection.This give more weight age to the pixel values around "
                "the edge region. This increase the edge intensity and it become enhanced comparatively to the "
                "original image.Horizontal Sobel operator highlights the vertical edges.",
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
        "info": " In a Gaussian blur, the pixels nearest the center of the kernel are given more weight than those "
                "far away from the center. Larger kernels have more values factored into the average, "
                "and this implies that a larger kernel will blur the image more than a smaller kernel.",
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
        "info": "Applying motion blur to an image boils down to convolving a filter across the image.The greater the "
                "size of the filter, the greater will be the motion blur effect. Further, the direction of 1’s across "
                "the filter grid is the direction of the desired motion.",
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
        "info": "Applying motion blur to an image boils down to convolving a filter across the image.The greater the "
                "size of the filter, the greater will be the motion blur effect. Further, the direction of 1’s across "
                "the filter grid is the direction of the desired motion.",
    },
]
