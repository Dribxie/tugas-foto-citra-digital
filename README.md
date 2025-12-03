# tugas-foto-citra-digital

Image Modernization (Color Balance + Sharpening)

Proyek ini melakukan modernisasi foto jadul dengan dua langkah utama: Color Balance untuk memperbaiki warna pudar/sepia dan Modern Sharpening untuk menambah ketajaman detail. Program dibuat menggunakan Python, OpenCV, dan NumPy.

Fitur:

- Menghilangkan warna sepia & meningkatkan keseimbangan warna (normalisasi RGB).
- Menajamkan foto dengan kernel sharpening 3×3.
- Konversi otomatis BGR ↔ RGB sesuai kebutuhan OpenCV.
- Menyimpan hasil ke file dan menampilkan pratinjau.

Alur Proses:

1. Baca gambar (BGR).
2. Konversi ke RGB.
3. Normalisasi warna (min–max).
4. Terapkan kernel sharpening.
5. Kembalikan ke BGR & simpan.
6. Tampilkan hasil.
