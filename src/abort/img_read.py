from PIL import Image
def img2rgb(path:str = 'capoo.png'):
    # 打开图像
    image = img2pix(path)

    # 将图像转换为RGB模式
    image = image.convert('RGB')

    # 获取图像的像素数据
    pixel_data = list(image.getdata())
    return pixel_data
def img2size(path:str = 'capoo.png'):
    # 打开图像
    image = img2pix(path)

    # 获取图像的长度和宽度
    width, height = image.size

    # 打印图像的长度和宽度
    return width,height

def img2xyc(path: str = 'capoo.png'):
    width, height = img2size(path)
    pixel_data = img2rgb(path)

    result = []
    for y in range(height):
        for x in range(width):
            pixel_index = y * width + x
            color = pixel_data[pixel_index]
            x_coord = x - width // 2
            y_coord = height // 2 - y
            result.append(((x_coord, y_coord), color))

    return result
def img2pix(path: str = 'capoo.png'):
    # 打开原始图像
    image = Image.open(path)

    resized_image = image.resize((120, 120),Image.NEAREST)

    return resized_image