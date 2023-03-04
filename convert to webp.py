from PIL import Image
import os
import PIL
import shutil
import easygui
from random import randint
root_dir = easygui.diropenbox(title="select the root folder with your images")
os.chdir(root_dir)
junk = 'junk'
try:
	os.mkdir(junk)
except:
	junk += str(randint(1,1000000))
	try:
		os.mkdir(junk)
	except:
		junk += str(randint(0,9))
		os.mkdir(junk)
for root, dirs, files in os.walk("."):
	for file in files:
		if file.endswith((".png", ".jpg", "jpeg", ".jfif", ".pjpeg", ".pjp", ".bmp", ".tif", ".tiff")):
			if not junk in root:
				try:
					image = Image.open(os.path.join(root, file))
					pos = file.rfind('.')
					new_file = file[:pos] + ".webp"
					image.save(os.path.join(root,new_file), format="webp")
					if not os.path.exists(os.path.join(junk, root[2:])):
						os.makedirs(os.path.join(junk, root[2:]))
					shutil.move(os.path.join(root,file), os.path.join(os.path.join(junk, root[2:]), file))
				except Exception as e:
					print(e)
