import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("📭 Tidak ada tugas.")
        return
    print("\n📋 Daftar Tugas:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task['done'] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("📝 Judul tugas: ")
    tasks.append({"title": title, "done": False})
    print("✅ Tugas ditambahkan!")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Nomor tugas yang selesai: ")) - 1
        tasks[idx]["done"] = True
        print("✔️ Ditandai selesai!")
    except (ValueError, IndexError):
        print("❌ Nomor tidak valid.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Nomor tugas yang dihapus: ")) - 1
        deleted = tasks.pop(idx)
        print(f"🗑️ Tugas '{deleted['title']}' dihapus!")
    except (ValueError, IndexError):
        print("❌ Nomor tidak valid.")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== Aplikasi To-Do List ===")
        print("1. Lihat Tugas")
        print("2. Tambah Tugas")
        print("3. Tandai Selesai")
        print("4. Hapus Tugas")
        print("5. Keluar")
        choice = input("Pilih menu (1-5): ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("👋 Sampai jumpa!")
            break
        else:
            print("❗ Pilihan tidak valid.")

if __name__ == "__main__":
    main()
