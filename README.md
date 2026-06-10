# Task Tracker CLI

Project URL:
https://roadmap.sh/projects/task-tracker

## Deskripsi

Task Tracker CLI adalah aplikasi berbasis Command Line Interface (CLI) yang dibuat menggunakan Python untuk membantu pengguna mengelola daftar tugas sehari-hari.

Aplikasi ini memungkinkan pengguna untuk menambah, memperbarui, menghapus, dan memantau status tugas langsung dari terminal. Seluruh data tugas disimpan secara lokal dalam file JSON sehingga tidak memerlukan database tambahan.

---

## Fitur

* Menambahkan tugas baru
* Memperbarui tugas yang sudah ada
* Menghapus tugas
* Menandai tugas sebagai **sedang dikerjakan (in-progress)**
* Menandai tugas sebagai **selesai (done)**
* Menampilkan seluruh tugas
* Memfilter tugas berdasarkan status
* Menyimpan data ke file JSON

---

## Struktur Proyek

```text
Task Tracker/
│
├── task-cli.py
├── tasks.json
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Persyaratan

* Python 3.10 atau lebih baru

Proyek ini tidak memerlukan library eksternal.

---

## Instalasi

Clone repository:


git clone https://github.com/Husemn/task-tracker.git
cd task-tracker


---

## Cara Menjalankan

### Menambahkan tugas

```bash
python task-cli.py add "Belajar Python"
```

Contoh output:

```text
Tugas berhasil ditambahkan (ID: 1)
```

---

### Memperbarui tugas

```bash
python task-cli.py update 1 "Belajar Python Lanjutan"
```

---

### Menghapus tugas

```bash
python task-cli.py delete 1
```

---

### Menandai tugas sedang dikerjakan

```bash
python task-cli.py mark-in-progress 1
```

---

### Menandai tugas selesai

```bash
python task-cli.py mark-done 1
```

---

### Menampilkan semua tugas

```bash
python task-cli.py list
```

---

### Menampilkan tugas yang selesai

```bash
python task-cli.py list done
```

---

### Menampilkan tugas yang sedang dikerjakan

```bash
python task-cli.py list in-progress
```

---

### Menampilkan tugas yang belum dikerjakan

```bash
python task-cli.py list todo
```

---

## Penyimpanan Data

Semua data tugas disimpan dalam file:

```text
tasks.json
```

Setiap tugas memiliki informasi:

* ID
* Deskripsi tugas
* Status
* Waktu pembuatan
* Waktu terakhir diperbarui

---

## Contoh Data Tugas

```json
{
  "id": 1,
  "description": "Belajar Python",
  "status": "todo",
  "createdAt": "2025-01-01T10:00:00",
  "updatedAt": "2025-01-01T10:00:00"
}
```

---

## Tujuan Proyek

Proyek ini dibuat sebagai bagian dari roadmap pembelajaran backend untuk melatih:

* Manipulasi file JSON
* Pemrograman Python
* Pengelolaan data menggunakan CLI
* Praktik pengembangan perangkat lunak sederhana

---

