from PIL import Image
from io import BytesIO
from urlBase import url as urlbase

# url 값 읽어오기
urlText = urlbase

# 형태값 슬라이싱
rmText = urlText.replace("data:jpg;base64,","")

# 이미지 읽어오기
result = open(rmText(BytesIO))

# 이미지 열기
result.show()