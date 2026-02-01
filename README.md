# Cloud-Based API Automation Testing - Dropsuite Portfolio

## 📌 Project Overview

Proyek ini adalah kerangka kerja pengujian otomatisasi (Automation Testing Framework) yang dirancang untuk memvalidasi integritas data pada layanan backend. Fokus utama dari proyek ini adalah memastikan bahwa API dapat menangani operasi data (Backup/Restore simulation) dengan akurat, sesuai dengan standar **Software Quality methodologies**.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Testing Framework:** Pytest
- **Library:** Requests (API Testing)
- **CI/CD:** GitHub Actions (Automated workflow)
- **Environment:** Python venv (Virtual Environment)

## 📋 Key Features & Test Scenarios

Proyek ini mencakup pengujian fungsionalitas Backend yang krusial:

1. **Positive Test:** Memvalidasi pembuatan record baru (POST) dengan status code 201.
2. **Data Integrity Check:** Memastikan payload yang dikirim sama persis dengan data yang tersimpan/dikembalikan oleh API.
3. **Negative Test:** Menangani error handling (404 Not Found) untuk ID yang tidak valid.
4. **Schema Validation:** Memastikan struktur JSON respons konsisten.

## 🚀 Getting Started

### 1. Prerequisites

Pastikan Anda memiliki Python terinstal. Sangat disarankan untuk menjalankan proyek ini dalam **Virtual Environment** untuk menjaga isolasi dependensi.

### 2. Installation

Kloning repositori ini dan masuk ke direktori proyek:

```bash
git clone [https://github.com/robby-fa/api_test.git](https://github.com/robby-fa/api_test.git)
cd repository-anda

```

### 3. Buat dan aktifkan virtual environment

# Windows

```bash
python -m venv venv
venv\Scripts\activate
```

# Mac/Linux

```bash
python -m venv venv
source venv/bin/activate
```

# Install dependensi

```bash
pip install -r requirements.txt
```
