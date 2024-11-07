Berikut adalah dokumentasi API dengan Markdown dalam bahasa Indonesia.

---

# Dokumentasi API Grader

API ini menilai jawaban siswa berdasarkan pertanyaan dan jawaban yang benar. API ini memerlukan autentikasi melalui header `Authorization`.

## URL Dasar

```
http://127.0.0.1:5000
```

## Autentikasi

Setiap permintaan harus menyertakan header `Authorization` dengan nilai `API_SECRET_KEY` yang disimpan di `.env`. Jika header ini tidak ada atau tidak cocok, permintaan akan ditolak dengan respons **401 Unauthorized**.

## Endpoint

### `POST /grader`

Endpoint ini menerima data soal dan jawaban siswa dalam format JSON, lalu mengembalikan penilaian berdasarkan kesesuaian jawaban siswa terhadap jawaban yang benar.

#### Header

| Key             | Value           |
|-----------------|-----------------|
| Authorization   | API_SECRET_KEY  |
| Content-Type    | application/json|

#### Permintaan

- **Metode**: `POST`
- **URL**: `/grader`

#### Body Permintaan

Body permintaan harus berbentuk JSON dengan struktur berikut:

```json
{
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
          // ...siswa lainnya
        ]
      },
      {
        "id": "soal_002",
        "pertanyaan": "Apa yang akan terjadi pada periode ayunan sederhana jika panjang tali pendulum diperpendek?",
        "jawaban_benar": "Periode ayunan akan menjadi lebih pendek.",
        "siswa": [
          {
            "id": "siswa_01",
            "jawaban": "Periode ayunan akan menjadi lebih panjang"
          },
          {
            "id": "siswa_02",
            "jawaban": "Periode ayunan tidak akan berubah"
          },
          {
            "id": "siswa_03",
            "jawaban": "Periode ayunan akan menjadi lebih pendek"
          }
          // ...siswa lainnya
        ]
      }
    ]
  }
}
```

#### Respons

Respons akan berisi hasil penilaian dalam format JSON sebagai berikut:

```json
{
  "response": {
    "soal": [
      {
        "id": "soal_001",
        "pertanyaan": "Jelaskan mengapa langit berwarna biru pada siang hari?",
        "penilaian": [
          {
            "id": "siswa_01",
            "nilai": 5
          },
          {
            "id": "siswa_02",
            "nilai": 5
          },
          {
            "id": "siswa_03",
            "nilai": 7
          }
        ]
      },
      {
        "id": "soal_002",
        "pertanyaan": "Apa yang akan terjadi pada periode ayunan sederhana jika panjang tali pendulum diperpendek?",
        "penilaian": [
          {
            "id": "siswa_01",
            "nilai": 5
          },
          {
            "id": "siswa_02",
            "nilai": 5
          },
          {
            "id": "siswa_03",
            "nilai": 10
          }
        ]
      }
    ]
  }
}
```

#### Kesalahan yang Mungkin Terjadi

1. **401 Unauthorized**: Header `Authorization` tidak ada atau tidak sesuai.
2. **400 Bad Request**: Data permintaan tidak valid atau tidak lengkap.
3. **500 Internal Server Error**: Masalah pada server, termasuk ketika respons AI tidak dalam format JSON yang valid.

## Contoh Penggunaan dengan JavaScript

Berikut adalah contoh penggunaan API dengan JavaScript:

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
          // ...siswa lainnya
        ]
      }
      // ...soal lainnya
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

Dengan dokumentasi ini, Anda dapat memahami cara menggunakan API untuk memberikan penilaian pada jawaban siswa berdasarkan kunci jawaban yang telah disediakan. Pastikan `API_SECRET_KEY` di `.env` sesuai dengan header `Authorization` dalam setiap permintaan.