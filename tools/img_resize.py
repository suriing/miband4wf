from PIL import Image

def resizepng(source, result, res_width, res_hight):
    image = Image.open(source)
    # resize 할 이미지 사이즈 
    resize_image = image.resize((res_width, res_hight))
    # 저장할 파일 Type : JPEG, PNG 등 
    # 저장할 때 Quality 수준 : 보통 95 사용 
    resize_image.save(result, "PNG", quality=95 )

def main():
    start_no = 91
    end_no = 116
    wi = 18
    he = 18
    for i in range(start_no, end_no+1):
        if i > 999:
            resizepng(str(i) + ".png", "re-" + str(i) + ".png", wi, he)
        elif i > 99:
            resizepng("0" + str(i) + ".png", "re-0" + str(i) + ".png", wi, he)
        elif i > 9:
            resizepng("00" + str(i) + ".png", "re-00" + str(i) + ".png", wi, he)
        else:
            resizepng("000" + str(i) + ".png", "re-000" + str(i) + ".png", wi, he)