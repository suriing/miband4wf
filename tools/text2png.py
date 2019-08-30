# coding=utf8

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

NanumBarunGothic = "C:/Windows/Fonts/NanumBarunGothic.ttf"
NotoSansKR = "C:/Windows/Fonts/NotoSansKR-Regular.otf"
NotoSansKR_Bold = "C:/Windows/Fonts/NotoSansKR-Bold.otf"
D2Coding = "C:/Windows/Fonts/D2Coding-Ver1.3.2-20180524-ligature.ttc"

def text2png(text, fullpath, color = "#ffffff", bgcolor = "#000", fontfullpath = None, fontsize = 10, leftpadding = 1, rightpadding = 1, height = 20, width = 90, multiline = False, y_offset = 0, font_type = 0):
	REPLACEMENT_CHARACTER = u'\uFFFD'
	NEWLINE_REPLACEMENT_STRING = ' ' + REPLACEMENT_CHARACTER + ' '

	font = ImageFont.load_default() if fontfullpath == None else ImageFont.truetype(fontfullpath, fontsize, index = font_type)
	text = text.replace('\n', NEWLINE_REPLACEMENT_STRING)

	lines = []
	line = u""

	for word in text.split():
		#print(word)
		if word == REPLACEMENT_CHARACTER: #give a blank line
			lines.append( line[1:] ) #slice the white space in the begining of the line
			line = u""
			lines.append( u"" ) #the blank line
		elif font.getsize( line + ' ' + word )[0] <= (width - rightpadding - leftpadding):
			line += ' ' + word
		else: #start a new line
			lines.append( line[1:] ) #slice the white space in the begining of the line
			line = u""

			#TODO: handle too long words at this point
			line += ' ' + word #for now, assume no word alone can exceed the line width

	if len(line) != 0:
		lines.append( line[1:] ) #add the last line

	line_width = font.getsize(text)[0]
	line_height = font.getsize(text)[1]
	
	if multiline:
		img_height = line_height * len(lines)
	else:
		img_height = height

	img = Image.new("RGBA", (width, img_height), bgcolor)
	draw = ImageDraw.Draw(img)

	y = 0
	for line in lines:
		if multiline:
			draw.text( (leftpadding, y + y_offset), line, color, font=font)
		else:
			draw.text( ((width-line_width)/2, (height-line_height)/2 + y_offset), line, color, font=font)
		y += line_height

	img.save(fullpath)

#show time
# 나눔바른고딕
# text2png(u"월 月 MON", '나눔바른고딕-20.png', fontfullpath = NanumBarunGothic, fontsize = 20) # eq v1
# text2png(u"월 月 MON", '1나눔바른고딕-66.png', fontfullpath = NanumBarunGothic, fontsize = 17)

# NotoSansKR
# text2png(u"월 月 MON", '2NotoSansKR-17.png', fontfullpath = NotoSansKR, fontsize = 17) # pref

# D2Coding (FOR V1.1,V2)
def weekdaymaker(context_list, co, bgco, font_path, font_size, start_i, end_i, lp, rp, he, wi, ml, ft = 0):
	start_rem = start_i % 7
	for i in range(start_i, end_i+1):
		if (i - start_rem) % 7 == 0:
			text2png(context_list[0], '00' + str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi, multiline = ml, font_type = ft)
		elif (i - start_rem) % 7 == 1:
			text2png(context_list[1], '00' + str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi, multiline = ml, font_type = ft)
		elif (i - start_rem) % 7 == 2:
			text2png(context_list[2], '00' + str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi, multiline = ml, font_type = ft)
		elif (i - start_rem) % 7 == 3:
			text2png(context_list[3], '00' + str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi, multiline = ml, font_type = ft)
		elif (i - start_rem) % 7 == 4:
			text2png(context_list[4], '00' + str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi, multiline = ml, font_type = ft)
		elif (i - start_rem) % 7 == 5:
			text2png(context_list[5], '00' + str(i) + '.png', color = "#ff7f27", bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi, multiline = ml, font_type = ft)
		elif (i - start_rem) % 7 == 6:
			text2png(context_list[6], '00' + str(i) + '.png', color = "#ed1c24", bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi, multiline = ml, font_type = ft)
		else:
			print("????")

ERLE_V1_1 = [
	"월 月 MON",
	"화 火 TUE",
	"수 水 WED",
	"목 木 THU",
	"금 金 FRI",
	"토 土 SAT",
	"일 日 SUN"
	]

# ERLE V1.1
#  weekdaymaker(context_list = ERLE_V1_1, co = "#52e8e7", bgco = "#000", font_path = D2Coding, font_size = 16, start_i = 66, end_i = 86, lp = 3, rp = 3, he = 20, wi = 90, ml = False)

# ERLE V2
# weekdaymaker(context_list = ERLE_V1_1, co = "#52e8e7", bgco = "#000", font_path = D2Coding, font_size = 16, start_i = 53, end_i = 73, lp = 1, rp = 1, he = 20, wi = 85, ml = False)

ERLE_V3KC = [
	"월 月",
	"화 火",
	"수 水",
	"목 木",
	"금 金",
	"토 土",
	"일 日"
	]

ERLE_V3KE = [
	"월 MON",
	"화 TUE",
	"수 WED",
	"목 THU",
	"금 FRI",
	"토 SAT",
	"일 SUN"
	]

# ERLE V3
weekdaymaker(context_list = ERLE_V3KC, co = "#52e8e7", bgco = "#000", font_path = D2Coding, font_size = 15, start_i = 53, end_i = 73, lp = 1, rp = 1, he = 20, wi = 58, ml = False, ft = 1)#50

def digitmaker(co, bgco, font_path, font_size, offset = 0):
	font = ImageFont.load_default() if font_path == None else ImageFont.truetype(font_path, font_size)
	tmp = "8"
	wi = font.getsize(tmp)[0]
	he = font.getsize(tmp)[1]
	for i in range(10):
		text2png(str(i), str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, height = he, width = wi, y_offset = offset)
		
		# make dashed digit
		im = Image.open(str(i) + '.png')
		d = ImageDraw.Draw(im)
		div = 6
		gap = int(round(wi/div,0))
		for j in range(div):
			p1 = (0+j*gap, 0)
			p2 = (wi+j*gap, he)
			p3 = (0-j*gap, 0)
			p4 = (wi-j*gap, he)
			d.line([p1, p2], fill=bgco, width=int(round(font_size/30,0)))
			d.line([p3, p4], fill=bgco, width=int(round(font_size/30,0)))
		im.save(str(i) + '-d.png')

# digitmaker(co = "#52e8e7", bgco = "#000", font_path = D2Coding, font_size = 100, offset = -4)

def findfontsize(font_path = D2Coding, font_size = 100):
	font = ImageFont.load_default() if font_path == None else ImageFont.truetype(font_path, font_size)
	tmp = "8"
	wi = font.getsize(tmp)[0]
	he = font.getsize(tmp)[1]
	print("font_size : " + str(font_size) + " \twidth : " + str(wi) + " \theight : " + str(he))

#for i in range(50,80+1):
#	findfontsize(font_size = i)