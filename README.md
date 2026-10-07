# 2026 Data Mining TI-3A

Repositori proyek praktikum & riset Data Mining (TI-3A).

## 📁 Struktur Direktori
- `Youtube_Data_Collection_API/`: Modul ekstraksi dataset YouTube Data API v3 dan Return YouTube Dislike (RYD) API.
- `SKILL.md`: Pedoman pemeliharaan context AI Agent (`danish-ai-agent-context`).
- `DANISH_AI_AGENT.md`: Context file ringkas sumber informasi untuk AI assistant.

## 🚀 Memulai Cepat
Silakan menuju ke direktori [Youtube_Data_Collection_API](file:///home/imnotdanish05/data1/project/kuliah/2026_Data-Mining_TI-3A/Youtube_Data_Collection_API/) untuk panduan instalasi, konfigurasi API Key, dan menjalankan pengumpulan data:

```bash
cd Youtube_Data_Collection_API
pip install -r requirements.txt
cp .env.example .env
# Masukkan API Key Anda di .env
python main.py --input-csv input_videos_template.csv
```

