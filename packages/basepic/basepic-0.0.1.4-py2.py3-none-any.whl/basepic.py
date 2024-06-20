import base64
from PIL import Image
from io import BytesIO

# base64转图片
def down_base64(path:str,base64_str:str) -> None:
    if base64_str.startswith('data:image/'):
        base64_str = base64_str.split(',')[1]
    img_data = base64.b64decode(base64_str)    # 解码时只要内容部分
    image = Image.open(BytesIO(img_data))
    image.save(path)

# 图片转base64
def get_base64(path:str, fmt:str='png') -> str:
    with open(path, 'rb') as f:
        image_data = f.read()
    image_io = BytesIO(image_data)
    base64_str = base64.b64encode(image_io.getvalue()).decode('utf-8')
    return base64_str

# 写入txt文本
def write_txt(path:str,content:str) -> None:
    with open(path,'w') as f:
        f.write(str(content))

# 读取txt文本
def read_txt(path:str) -> str:
    with open(path,'r') as f:
        return str(f.read())