from captcha.image import ImageCaptcha

from PIL import Image
import random

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


def random_captcha_text(char_set=number + alphabet + ALPHABET, captcha_size=4):
	captcha_text = []
	for i in range(captcha_size):
		c = random.choice(char_set)
		captcha_text.append(c)
	return captcha_text


def gen_captcha_text_and_image():
	"""
	获取验证码
	:return:
	"""
	image = ImageCaptcha()
	captcha_text = random_captcha_text()
	captcha_text = ''.join(captcha_text)
	
	captcha = image.generate(captcha_text)
	
	image.write('hoho', 'jpjp' + '.jpg')
	
	captcha_image = Image.open(captcha)
	
	return captcha_text, captcha


# if __name__ == '__main__':
# 	# 测试
# 	text, image = gen_captcha_text_and_image()
# 	f = plt.figure()
# 	ax = f.add_subplot(111)
# 	ax.text(0.1, 0.9, text, ha='center', va='center', transform=ax.transAxes)
# 	plt.imshow(image)
# 	plt.show()
