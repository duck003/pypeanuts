from pycat.core import Window
from pycat.base import NumpyImage as Image

w = Window()
image01 = Image.get_array_from_file("4_0.jpg")
image02 = Image.get_array_from_file("10_0.jpg")
image03 = Image.get_array_from_file("11_0.jpg")
image04 = Image.get_array_from_file("16_0.jpg")
image06 = Image.get_array_from_file("22_0.jpg")

rows1, cols1, channels1 = image01.shape
rows2, cols2, channels2 = image02.shape
rows3, cols3, channels3 = image03.shape
rows4, cols4, channels4 = image04.shape
rows6, cols6, channels6 = image06.shape

isprite1 = w.create_sprite()
isprite1.scale = 1.6
isprite1.texture = Image.get_texture_from_array(image01)
isprite1.position = (430, 460)

isprite2 = w.create_sprite()
isprite2.scale = 1.6
isprite2.texture = Image.get_texture_from_array(image02)
isprite2.position = (860, 460)

isprite3 = w.create_sprite()
isprite3.scale = 1.6
isprite3.texture = Image.get_texture_from_array(image03)
isprite3.position = (360, 290)

isprite4 = w.create_sprite()
isprite4.scale = 1.6
isprite4.texture = Image.get_texture_from_array(image04)
isprite4.position = (900, 290)

isprite6 = w.create_sprite()
isprite6.scale = 1.6
isprite6.texture = Image.get_texture_from_array(image06)
isprite6.position = (650, 100)

left_eye_image = image01[50:68, 16:40, :]
left_eye = w.create_sprite()
left_eye.position = (600, 500)
left_eye.texture = Image.get_texture_from_array(left_eye_image)
left_eye.scale = 3

right_eye_image = image02[50:68, 50:74, :]
right_eye = w.create_sprite()
right_eye.position = (700, 500)
right_eye.texture = Image.get_texture_from_array(right_eye_image)
right_eye.scale = 3

nose_image = image03[26:54, 26:46, :]
nose = w.create_sprite()
nose.position = (625, 400)
nose.texture = Image.get_texture_from_array(nose_image)
nose.scale = 2

rnose_image = image04[26:54, 46:66, :]
rnose = w.create_sprite()
rnose.position = (662, 400)
rnose.texture = Image.get_texture_from_array(rnose_image)
rnose.scale = 2

mouth_image = image06[16:30, 25:72, :]
mouth = w.create_sprite()
mouth.position = (650, 300)
mouth.texture = Image.get_texture_from_array(mouth_image)
mouth.scale = 2


right_eye = w.create_sprite()
nose = w.create_sprite()
mouth = w.create_sprite()

w.run()