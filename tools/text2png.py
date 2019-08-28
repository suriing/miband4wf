# coding=utf8

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

NanumBarunGothic = "C:/Windows/Fonts/NanumBarunGothic.ttf"
NotoSansKR = "C:/Windows/Fonts/NotoSansKR-Regular.otf"
D2Coding = "C:/Windows/Fonts/D2Coding-Ver1.3.2-20180524-ligature.ttc"

def text2png(text, fullpath, color = "#ffffff", bgcolor = "#000", fontfullpath = None, fontsize = 10, leftpadding = 1, rightpadding = 1, height = 20, width = 90):
	REPLACEMENT_CHARACTER = u'\uFFFD'
	NEWLINE_REPLACEMENT_STRING = ' ' + REPLACEMENT_CHARACTER + ' '

	font = ImageFont.load_default() if fontfullpath == None else ImageFont.truetype(fontfullpath, fontsize)
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
	#img_height = line_height * (len(lines) + 1)
	img_height = height

	img = Image.new("RGBA", (width, height), bgcolor)
	draw = ImageDraw.Draw(img)

	y = 0
	for line in lines:
		#draw.text( (leftpadding, y), line, color, font=font)
		draw.text( ((90-line_width)/2,(20-line_height)/2), line, color, font=font)
		y += line_height

	# add linkback at the bottom
	# draw.text( (width - linkbackx, height - linkback_height), linkback, color, font=fontlinkback)

	img.save(fullpath)

#show time
# 나눔바른고딕
# text2png(u"월 月 MON", '나눔바른고딕-20.png', fontfullpath = NanumBarunGothic, fontsize = 20) # eq v1
# text2png(u"월 月 MON", '1나눔바른고딕-66.png', fontfullpath = NanumBarunGothic, fontsize = 17)

# NotoSansKR
# text2png(u"월 月 MON", '2NotoSansKR-17.png', fontfullpath = NotoSansKR, fontsize = 17) # pref

# D2Coding (FOR V1.1,V2)
def weekdaymaker(context_list, co, bgco, font_path, font_size, start_i, end_i, lp, rp, he, wi):
	start_rem = start_i % 7
	for i in range(start_i, end_i+1):
		if (i - start_rem) % 7 == 0:
			text2png(context_list[0], '00' + str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi)
		elif (i - start_rem) % 7 == 1:
			text2png(context_list[1], '00' + str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi)
		elif (i - start_rem) % 7 == 2:
			text2png(context_list[2], '00' + str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi)
		elif (i - start_rem) % 7 == 3:
			text2png(context_list[3], '00' + str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi)
		elif (i - start_rem) % 7 == 4:
			text2png(context_list[4], '00' + str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi)
		elif (i - start_rem) % 7 == 5:
			text2png(context_list[5], '00' + str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi)
		elif (i - start_rem) % 7 == 6:
			text2png(context_list[6], '00' + str(i) + '.png', color = co, bgcolor = bgco, fontfullpath = font_path, fontsize = font_size, leftpadding = lp, rightpadding = rp, height = he, width = wi)
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
#  weekdaymaker(context_list = ERLE_V1_1, co = "#52e8e7", bgco = "#000", font_path = D2Coding, font_size = 16, start_i = 66, end_i = 86, lp = 3, rp = 3, he = 20, wi = 90)

# ERLE V2
weekdaymaker(context_list = ERLE_V1_1, co = "#52e8e7", bgco = "#000", font_path = D2Coding, font_size = 16, start_i = 53, end_i = 73, lp = 1, rp = 1, he = 20, wi = 85)