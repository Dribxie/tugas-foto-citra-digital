import cv2
import numpy as np

# ===== METODE 1 : Color Balance (menghilangkan warna sepia/jadul) =====
img = cv2.imread("img-2.jpeg")# baca gambar dari direktori
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      # konversi BGR → RGB

# normalisasi warna biar tiap channel R,G,B lebih seimbang
balanced = cv2.normalize(img_rgb, None, 0, 255, cv2.NORM_MINMAX)

# ===== METODE 2 : Modern Sharpening =====
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])                     # kernel tajam model modern

sharpened = cv2.filter2D(balanced, -1, kernel)      # apply kernel

# balik lagi ke BGR biar bisa disimpan oleh OpenCV
final_img = cv2.cvtColor(sharpened, cv2.COLOR_RGB2BGR)

# simpan hasil akhir
cv2.imwrite("/mnt/data/hasil_modern.jpg", final_img)
print("Berhasil disimpan sebagai hasil_modern.jpg")

cv2.imshow("Hasil", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
