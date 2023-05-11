import matplotlib.pyplot as plt
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np
import cv2

astronautImage = data.astronaut()
cameraImage = data.camera()
#Load gambar asli dari modul data skimage


astroCropped = astronautImage.copy()
astroCropped = astroCropped[0:256,64:320]

cameraCropped = cameraImage.copy()
cameraCropped = cameraCropped[64:256,128:320]
#Crop gambar dengan slicing dan ukurang yang diinginkan


fig, axes = plt.subplots(2,2, figsize = (12,12))
ax = axes.ravel()
ax[0].imshow(astronautImage)
ax[0].set_title("Citra Input 1")
ax[1].imshow(cameraImage, cmap='gray')
ax[1].set_title("Citra Input 2")
ax[2].imshow(astroCropped, cmap='gray')
ax[2].set_title("Citra Output 1")
ax[3].imshow(cameraCropped, cmap='gray')
ax[3].set_title("Citra Output 2")

plt.show()
#Menampilkan citra input dan output dengan subplot dari matplotlib


inv = invert(astroCropped)
print('Shape Input : ', astroCropped.shape)
print('Shape Output : ',inv.shape)
#Invert gambar dengan skimage.util.invert


fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(astroCropped)
ax[0].set_title("Citra Input")

ax[1].hist(astroCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')

ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')

plt.show()
#Menampilkan citra input, histogram input, citra output, dan histogram output dengan subplot dari matplotlib


copyCamera = cameraCropped.copy().astype(float)

m1,n1 = copyCamera.shape
output1 = np.empty([m1, n1])

for baris in range(0, m1):
    for kolom in range(0, n1):
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyCamera[baris, kolom] + 100
#Menambahkan nilai 100 pada setiap pixel gambar dengan operasi penjumlahan pada numpy array


fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(cameraCropped, cmap='gray')
ax[0].set_title("Citra Input")

ax[1].hist(astroCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(output1, cmap='gray')
ax[2].set_title('Citra Output (Brightnes)')

ax[3].hist(output1.ravel(), bins=256)
ax[3].set_title('Histogram Input')

plt.show()
#Menampilkan citra input, histogram input, citra output, dan histogram output dengan subplot dari matplotlib

img = cv2.imread(r"C:\Users\Wahyu\Downloads\Compressed\Prak 34\Praktikum 3 dan 4\image\orange.jpg")

img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype
#Membuat variabel


img_brightness = np.zeros(img.shape, dtype=np.uint8)
# Membuat matriks kosong yang sama ukurannya dengan gambar asli

def brighter(nilai):
# Membuat fungsi untuk membuat gambar menjadi lebih terang
# dengan nilai input "nilai"
    for y in range(0,img_height):
        for x in range(0, img_width):
            # Looping setiap pixel dalam gambar berdasarkan koordinat x dan y
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red)+int(green)+int(blue)/3)
             # Menghitung rata-rata dari tiga nilai RGB
            gray += nilai
            # Menambahkan nilai yang diberikan ke nilai rata-rata
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            # Memastikan nilai gray tidak lebih dari 255 atau kurang dari 0
            img_brightness[y][x] = (gray, gray, gray)
            #Mengisi pixsel y,x dengan variable gray yang sudah di atur

            
img_rgbbright = np.zeros(img.shape, dtype=np.uint8)
# Membuat matriks kosong yang sama ukurannya dengan gambar asli
def rgbbrighter(nilai):
    # Membuat fungsi untuk membuat gambar menjadi lebih terang
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Looping setiap pixel dalam gambar berdasarkan koordinat x dan y
            red = img[y][x][0]
            red+= nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            # Membuat nilai red tidak lebih dari 255 atau kurang dari 0
            green = img[y][x][1]
            green+= nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            # Membuat nilai green tidak lebih dari 255 atau kurang dari 0
            blue = img[y][x][2]
            blue+= nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            # Membuat nilai red tidak lebih dari 255 atau kurang dari 0
            img_rgbbright[y][x] = (red, green, blue)
            #Mengisi pixsel y,x dengan variable red green blue yang sudah di atur

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()
brighter(-100)
rgbbrighter(-100)
ax[0].imshow(img_brightness)
ax[0].set_title("Brightness -100")
ax[1].imshow(img_rgbbright)
ax[1].set_title("RGB Brightness -100")
brighter(100)
rgbbrighter(100)
ax[2].imshow(img_brightness)
ax[2].set_title("Brightness 100")
ax[3].imshow(img_rgbbright)
ax[3].set_title("RGB Brightness 100")
plt.show()
#Menampilkan gambar dalam bentuk plot 2x2

img_contrass = np.zeros(img.shape, dtype=np.uint8)
def contrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red)+int(green)+int(blue)/3)
            gray += nilai
            if gray > 255:
                gray = 255
            #membuat nilai gray tidak lebih dari 255
            img_contrass[y][x] = (gray, gray, gray)
#membuat variabel img_contrass
img_rgbcontrass = np.zeros(img.shape, dtype=np.uint8)
def rgbcontrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            #membuat nilai red tidak lebih dari 255
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            #membuat nilai green tidak lebih dari 255
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            #membuat nilai blue tidak lebih dari 255
            gray = int((red + green + blue) / 3)
            img_rgbcontrass[y][x] = (red, green, blue)
#Membuat variabel img_rgbcontrass
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

contrass(-100)
rgbcontrass(-100)
ax[0].imshow(img_contrass)
ax[0].set_title("Contrass -100")
ax[1].imshow(img_rgbcontrass)
ax[1].set_title("RGB Contrass -100")
contrass(100)
rgbcontrass(100)
ax[2].imshow(img_contrass)
ax[2].set_title("Contrass 100")
ax[3].imshow(img_rgbcontrass)
ax[3].set_title("RGB Contrass 100")
plt.show()
#menampilkan dengan plot 2x2


img_autocontrass = np.zeros(img.shape, dtype=np.uint8)
def autocontrass():
    xmax = 300
    xmin = 0
    d = 0
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray
    d = xmin-xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(float(255/d) * (gray-xmax))
            img_autocontrass[y][x] = (gray, gray, gray)
#membuat variabel img_autocontrass

fig, axes = plt.subplots(1, 2, figsize=(12, 12))
ax = axes.ravel()
autocontrass()
ax[0].imshow(img)
ax[0].set_title("Default")
ax[1].imshow(img_autocontrass)
ax[1].set_title("Contrass Autolevel")
plt.show()
#menampilkan gambar