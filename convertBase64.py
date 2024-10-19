
# git 커밋 테스트 4차

import base64
from PIL import Image
from io import BytesIO
from urlBase import url as urlbase

# 문자열값 import
base64_string = urlbase

# 형태값 제거
replace_url_base = base64_string.replace("data:jpg;base64,","")

# Base64 문자열 디코딩하기
image_data = base64.b64decode(replace_url_base)

# 디코딩된 이미지 읽어오기
image = Image.open(BytesIO(image_data))

# 이미지 보여주기
image.show() 

