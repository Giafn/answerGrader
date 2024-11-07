Berikut adalah panduan instalasi, konfigurasi, serta dokumentasi API dengan penjelasan mengenai pengaturan dan penyesuaian (tuning) yang dapat dilakukan.

---

# Dokumentasi Instalasi API Grader

API ini dibangun dengan Python dan Flask, yang bertugas menilai jawaban siswa berdasarkan pertanyaan dan kunci jawaban yang benar. Selain itu, API ini menggunakan Google Generative AI untuk menghasilkan respons otomatis, yang dikonfigurasi dengan beberapa parameter yang bisa dituning.

## Persyaratan

1. **Python** 3.8 atau lebih baru.
2. **Pip** untuk mengelola paket Python.
3. **Google Generative AI SDK** untuk Python.
4. **API Key** dari Google Generative AI yang disimpan dalam file `.env` untuk keperluan autentikasi.

## Instalasi

1. **Kloning repositori atau salin kode API ke dalam direktori Anda:**

   ```bash
   git clone https://github.com/Giafn/answerGrader.git
   cd answerGrader
   ```

2. **Buat virtual environment (opsional, tapi disarankan):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # untuk macOS atau Linux
   .\venv\Scripts\activate    # untuk Windows
   ```

3. **Instal dependensi:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Buat file `.env` untuk menyimpan kunci API dan konfigurasi lainnya.** File `.env` ini sebaiknya berisi:

   ```
   GEMINI_API_KEY=Your_Google_Generative_API_Key
   API_SECRET_KEY=Your_Secret_API_Key_For_Authorization
   ```

   - **GEMINI_API_KEY**: Kunci API untuk mengakses Google Generative AI.
   - **API_SECRET_KEY**: Kunci rahasia yang harus dikirimkan pada header `Authorization` untuk akses ke endpoint API.

5. **Jalankan aplikasi Flask:**

   ```bash
   flask run
   ```

   Jika Anda melihat pesan `Running on http://127.0.0.1:5000`, berarti API sudah berjalan dengan benar dan dapat diakses pada URL tersebut.

---

## Konfigurasi dan Tuning API

### Konfigurasi Tuning di `config.py`

File `config.py` berisi beberapa parameter yang bisa diatur untuk memodifikasi respons dari model Generative AI. Berikut adalah parameter tuning yang dapat dikonfigurasi:

- **temperature**: Nilai dari `temperature` (0 - 1) mengatur kreativitas atau kebebasan model dalam memberikan jawaban. Semakin rendah nilainya, semakin konservatif dan konsisten jawabannya.
- **top_p**: Nilai `top_p` menentukan rentang distribusi kumulatif dari kemungkinan output. Nilai mendekati 1 berarti lebih banyak kemungkinan yang dipertimbangkan.
- **top_k**: Nilai `top_k` menentukan jumlah pilihan kata teratas yang diambil pada setiap langkah. Semakin tinggi `top_k`, semakin besar variasi output model.
- **max_output_tokens**: Jumlah maksimum token (kata atau bagian dari kata) yang bisa dihasilkan dalam satu respons.

Contoh pengaturan ini di `config.py`:

```python
generation_config = {
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40,
    "max_output_tokens": 8192,
}
```

### Pengaturan Fine-Tuning di `services/generative_ai.py`

File ini memungkinkan Anda untuk melakukan fine-tuning atas prompt dan konteks model. Beberapa konfigurasi tambahan:

- **system_instruction**: Menyediakan instruksi umum pada model untuk konteks tertentu, misalnya menilai jawaban siswa dengan skala tertentu.
- **history**: Riwayat percakapan yang memungkinkan Anda memelihara konteks antara sesi. Ini dapat ditambahkan jika API perlu menyimpan riwayat percakapan dalam jangka waktu tertentu.

Contoh konfigurasi di `services/generative_ai.py`:

```python
system_instruction = "Nilai jawaban siswa berikut ini dengan skala 5-10, di mana 5 adalah sangat buruk dan 10 adalah sangat baik. Perhatikan apakah jawaban siswa sesuai dengan jawaban yang benar pada json yang di berikan."
history = [
    # Tambahkan elemen riwayat di sini jika dibutuhkan
]
```

---

## Contoh Penggunaan API dengan JavaScript

Berikut adalah contoh JavaScript untuk melakukan permintaan ke API:

```javascript
const data = JSON.stringify({
  "data": {
    "soal": [
      {
        "id": "soal_001",
        "pertanyaan": "Jelaskan mengapa langit berwarna biru pada siang hari?",
        "jawaban_benar": "Terjadi hamburan Rayleigh pada sinar matahari oleh partikel-partikel di atmosfer, terutama pada cahaya dengan panjang gelombang pendek seperti warna biru.",
        "siswa": [
          {
            "id": "siswa_01",
            "jawaban": "Karena langit memantulkan warna laut"
          },
          {
            "id": "siswa_02",
            "jawaban": "Karena adanya lapisan ozon"
          },
          {
            "id": "siswa_03",
            "jawaban": "Terjadi pembiasan cahaya matahari oleh atmosfer"
          }
        ]
      }
    ]
  }
});

const xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === this.DONE) {
    console.log(this.responseText);
  }
});

xhr.open("POST", "http://127.0.0.1:5000/grader");
xhr.setRequestHeader("Content-Type", "application/json");
xhr.setRequestHeader("Authorization", "API_SECRET_KEY");

xhr.send(data);
```

---

## Kesalahan yang Mungkin Terjadi

- **401 Unauthorized**: Header `Authorization` tidak ada atau tidak sesuai.
- **400 Bad Request**: Data permintaan tidak valid atau tidak lengkap.
- **500 Internal Server Error**: Masalah pada server, termasuk ketika respons AI tidak dalam format JSON yang valid.

---

Dengan mengikuti panduan ini, Anda dapat mengonfigurasi, menjalankan, dan melakukan tuning pada API sesuai kebutuhan.