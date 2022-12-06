import sys
import os
from PIL import Image

def compressor(directory):
	for file in os.listdir(directory):
		nameFile, extension = os.path.splitext(directory + file)

		if extension in ['.jpg', '.png', '.jpeg']:
			aux = Image.open(directory + file)
			aux.save(directory + '__compressed__' + file, optimize=True, quality=60)

if __name__ == '__main__':
	compressor(sys.argv[1])
