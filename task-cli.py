"""
Task Tracker CLI
Penggunaan:
  python task-cli.py add "Deskripsi task"
  python task-cli.py list
  python task-cli.py list todo
  python task-cli.py list in-progress
  python task-cli.py list done
  python task-cli.py update <id> "Deskripsi baru"
  python task-cli.py delete <id>
  python task-cli.py mark-in-progress <id>
  python task-cli.py mark-done <id>
"""

import sys
import json
import os
from datetime import datetime

# ── Konstanta ──────────────────────────────────────────────────────────────────
FILE = "tasks.json"
STATUS_VALID = ("todo", "in-progress", "done")


# ── Utilitas File JSON ─────────────────────────────────────────────────────────

def baca_tasks() -> list:
    """Baca semua task dari file JSON. Kembalikan list kosong jika belum ada."""
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        isi = f.read().strip()
    return json.loads(isi) if isi else []


def simpan_tasks(tasks: list) -> None:
    """Tulis semua task ke file JSON."""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def sekarang() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ── Operasi Task ───────────────────────────────────────────────────────────────

def tambah_task(deskripsi: str) -> None:
    """Tambahkan task baru dengan status default 'todo'."""
    tasks = baca_tasks()
    id_baru = max((t["id"] for t in tasks), default=0) + 1
    waktu = sekarang()
    tasks.append({
        "id": id_baru,
        "description": deskripsi,
        "status": "todo",
        "createdAt": waktu,
        "updatedAt": waktu,
    })
    simpan_tasks(tasks)
    print(f"Task added successfully (ID: {id_baru})")


def list_tasks(filter_status: str | None = None) -> None:
    """Tampilkan semua task, atau filter berdasarkan status."""
    tasks = baca_tasks()

    if filter_status:
        if filter_status not in STATUS_VALID:
            print(f"Error: status tidak valid. Pilih: {', '.join(STATUS_VALID)}")
            return
        tasks = [t for t in tasks if t["status"] == filter_status]

    if not tasks:
        print("Tidak ada task." if not filter_status else f"Tidak ada task dengan status '{filter_status}'.")
        return

    # Kelompokkan per status agar lebih rapi
    label = {"todo": "📋 TODO", "in-progress": "🔄 IN-PROGRESS", "done": "✅ DONE"}
    urutan = ["todo", "in-progress", "done"]
    grouped = {s: [t for t in tasks if t["status"] == s] for s in urutan}

    for status in urutan:
        grup = grouped[status]
        if not grup:
            continue
        print(f"\n{label[status]}")
        print("─" * 50)
        for t in grup:
            print(f"  [{t['id']:>3}] {t['description']}")
            print(f"        Dibuat : {t['createdAt']}")
            print(f"        Diupdate: {t['updatedAt']}")


def update_task(id_task: int, deskripsi_baru: str) -> None:
    """Perbarui deskripsi task berdasarkan ID."""
    tasks = baca_tasks()
    for task in tasks:
        if task["id"] == id_task:
            task["description"] = deskripsi_baru
            task["updatedAt"] = sekarang()
            simpan_tasks(tasks)
            print(f"Task {id_task} berhasil diupdate.")
            return
    print(f"Error: Task ID {id_task} tidak ditemukan.")


def hapus_task(id_task: int) -> None:
    """Hapus task berdasarkan ID."""
    tasks = baca_tasks()
    tasks_baru = [t for t in tasks if t["id"] != id_task]
    if len(tasks_baru) == len(tasks):
        print(f"Error: Task ID {id_task} tidak ditemukan.")
        return
    simpan_tasks(tasks_baru)
    print(f"Task {id_task} berhasil dihapus.")


def ubah_status(id_task: int, status_baru: str) -> None:
    """Ubah status task menjadi 'in-progress' atau 'done'."""
    tasks = baca_tasks()
    for task in tasks:
        if task["id"] == id_task:
            task["status"] = status_baru
            task["updatedAt"] = sekarang()
            simpan_tasks(tasks)
            print(f"Task {id_task} ditandai sebagai '{status_baru}'.")
            return
    print(f"Error: Task ID {id_task} tidak ditemukan.")


# ── Bantuan ────────────────────────────────────────────────────────────────────

def tampilkan_bantuan() -> None:
    print("""
Task Tracker CLI — Daftar Perintah
───────────────────────────────────────────────────────
  add <deskripsi>              Tambah task baru
  list                         Tampilkan semua task
  list todo                    Tampilkan task belum dikerjakan
  list in-progress             Tampilkan task sedang dikerjakan
  list done                    Tampilkan task selesai
  update <id> <deskripsi>      Perbarui deskripsi task
  delete <id>                  Hapus task
  mark-in-progress <id>        Tandai task sebagai in-progress
  mark-done <id>               Tandai task sebagai selesai
  help                         Tampilkan bantuan ini
""")


# ── Main / Dispatcher ──────────────────────────────────────────────────────────

def main() -> None:
    if len(sys.argv) < 2:
        tampilkan_bantuan()
        sys.exit(0)

    perintah = sys.argv[1]

    try:
        if perintah == "add":
            if len(sys.argv) < 3:
                print("Penggunaan: task-cli.py add <deskripsi>")
            else:
                tambah_task(sys.argv[2])

        elif perintah == "list":
            filter_status = sys.argv[2] if len(sys.argv) >= 3 else None
            list_tasks(filter_status)

        elif perintah == "update":
            if len(sys.argv) < 4:
                print("Penggunaan: task-cli.py update <id> <deskripsi baru>")
            else:
                update_task(int(sys.argv[2]), sys.argv[3])

        elif perintah == "delete":
            if len(sys.argv) < 3:
                print("Penggunaan: task-cli.py delete <id>")
            else:
                hapus_task(int(sys.argv[2]))

        elif perintah == "mark-in-progress":
            if len(sys.argv) < 3:
                print("Penggunaan: task-cli.py mark-in-progress <id>")
            else:
                ubah_status(int(sys.argv[2]), "in-progress")

        elif perintah == "mark-done":
            if len(sys.argv) < 3:
                print("Penggunaan: task-cli.py mark-done <id>")
            else:
                ubah_status(int(sys.argv[2]), "done")

        elif perintah in ("help", "--help", "-h"):
            tampilkan_bantuan()

        else:
            print(f"Error: Perintah '{perintah}' tidak dikenal.")
            print("Ketik 'python task-cli.py help' untuk daftar perintah.")

    except ValueError:
        print("Error: ID harus berupa angka bulat. Contoh: task-cli.py delete 3")
    except json.JSONDecodeError:
        print(f"Error: File '{FILE}' rusak atau bukan JSON yang valid.")
    except PermissionError:
        print(f"Error: Tidak punya izin untuk membaca/menulis '{FILE}'.")


if __name__ == "__main__":
    main()