import google.generativeai as genai
from config import Config

# Konfigurasi API Google Generative AI
genai.configure(api_key=Config.GEMINI_API_KEY)

def create_chat_session():
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction="Nilai jawaban siswa berikut ini dengan skala 5-10, di mana 5 adalah  sangat buruk dan 10 adalah sangat baik. Perhatikan apakah jawaban siswa sesuai dengan jawaban yang benar pada json yang di berikan",
    )
    
    return model.start_chat(
        history=[
            {
            "role": "user",
            "parts": [
                "{\"soal\":{\"id\":\"soal_001\",\"pertanyaan\":\"Berapakah hasil dari 2 + 2?\",\"jawaban_benar\":4},\"siswa\":[{\"id\":\"siswa_001\",\"jawaban\":\"4\"},{\"id\":\"siswa_002\",\"jawaban\":\"3\"}]}",
            ],
            },
            {
            "role": "model",
            "parts": [
                "```json\n{\"soal\": {\"id\": \"soal_001\", \"pertanyaan\": \"Berapakah hasil dari 2 + 2?\"}, \"penilaian\": [{\"id\": \"siswa_001\", \"nilai\": 10}, {\"id\": \"siswa_002\", \"nilai\": 5}]}\n\n```",
            ],
            },
            {
            "role": "user",
            "parts": [
                "{\"soal\":[{\"id\":\"soal_001\",\"pertanyaan\":\"Jelaskan mengapa langit berwarna biru pada siang hari?\",\"jawaban_benar\":\"Terjadi hamburan Rayleigh pada sinar matahari oleh partikel-partikel di atmosfer, terutama pada cahaya dengan panjang gelombang pendek seperti warna biru.\",\"siswa\":[{\"id\":\"siswa_01\",\"jawaban\":\"Karena langit memantulkan warna laut\"},{\"id\":\"siswa_02\",\"jawaban\":\"Karena adanya lapisan ozon\"},{\"id\":\"siswa_03\",\"jawaban\":\"Terjadi pembiasan cahaya matahari oleh atmosfer\"}]},{\"id\":\"soal_002\",\"pertanyaan\":\"Apa yang akan terjadi pada periode ayunan sederhana jika panjang tali pendulum diperpendek?\",\"jawaban_benar\":\"Periode ayunan akan menjadi lebih pendek.\",\"siswa\":[{\"id\":\"siswa_01\",\"jawaban\":\"Periode ayunan akan menjadi lebih panjang\"},{\"id\":\"siswa_02\",\"jawaban\":\"Periode ayunan tidak akan berubah\"},{\"id\":\"siswa_03\",\"jawaban\":\"Periode ayunan akan menjadi lebih pendek\"}]}]}",
            ],
            },
            {
            "role": "model",
            "parts": [
                "```json\n{\"soal\":[{\"id\":\"soal_001\",\"pertanyaan\":\"Jelaskan mengapa langit berwarna biru pada siang hari?\",\"jawaban_benar\":\"Terjadi hamburan Rayleigh pada sinar matahari oleh partikel-partikel di atmosfer, terutama pada cahaya dengan panjang gelombang pendek seperti warna biru.\",\"penilaian\":[{\"id\":\"siswa_01\",\"nilai\":5},{\"id\":\"siswa_02\",\"nilai\":5},{\"id\":\"siswa_03\",\"nilai\":7}]},{\"id\":\"soal_002\",\"pertanyaan\":\"Apa yang akan terjadi pada periode ayunan sederhana jika panjang tali pendulum diperpendek?\",\"jawaban_benar\":\"Periode ayunan akan menjadi lebih pendek.\",\"penilaian\":[{\"id\":\"siswa_01\",\"nilai\":5},{\"id\":\"siswa_02\",\"nilai\":5},{\"id\":\"siswa_03\",\"nilai\":10}]}]}\n\n```",
            ],
            },
            {
            "role": "user",
            "parts": [
                "soal 1 : kenapa manusia hidup",
            ],
            },
            {
            "role": "model",
            "parts": [
                "```json\n{\"error\":\"request tidak berbentuk json\"}\n```",
            ],
            },
            {
            "role": "user",
            "parts": [
                "apakah nana jawaban nya benar",
            ],
            },
            {
            "role": "model",
            "parts": [
                "```json\n{\"error\":\"request tidak berbentuk json\"}\n```",
            ],
            },
        ]
    )
