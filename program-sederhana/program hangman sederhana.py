import random
import os
os.system('cls')
# --- ASCII art untuk nyawa (0 = kalah) ---
STAGES = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """
]

# --- Kumpulan kata (ada yang punya spasi) ---
penyimpanan_kata = ['sialan', 'tampar', 'lampu kuning', 'lantas', 'malapetaka']
kata = random.choice(penyimpanan_kata).lower()

# Tampilkan spasi apa adanya, selain itu '_' sebagai sensor
tebak_kata = [' ' if c == ' ' else '_' for c in kata]

# Nyawa = jumlah tahap - 1 (karena indeks 0 adalah kondisi terburuk/kalah)
nyawa = len(STAGES) - 1

# Simpan huruf yang sudah ditebak agar tidak dihitung dua kali
sudah_tebak = set()

print("=== HANGMAN SEDERHANA ===")
while nyawa > 0:
    print(STAGES[nyawa])
    print("Kata: " + ''.join(tebak_kata))
    print(f"Huruf yang sudah ditebak: {', '.join(sorted(sudah_tebak))}" if sudah_tebak else "Belum ada tebakan.")
    print(f"Nyawa tersisa: {nyawa}")
    
    tebak = input("Tebak huruf: ").lower().strip()
    if len(tebak) != 1 or not tebak.isalpha():
        print("Masukkan 1 huruf alfabet saja.\n")
        continue

    if tebak in sudah_tebak:
        print("Huruf ini sudah ditebak sebelumnya.\n")
        continue

    sudah_tebak.add(tebak)

    if tebak in kata:
        # Ungkap semua posisi huruf yang cocok
        for i, ch in enumerate(kata):
            if ch == tebak:
                tebak_kata[i] = tebak
        print("Benar!\n")
    else:
        nyawa -= 1
        print("Salah!\n")

    # Cek kemenangan
    if '_' not in tebak_kata:
        print(STAGES[nyawa])
        print("Kata: " + ''.join(tebak_kata))
        print("\nSELAMAT!! Kamu berhasil menebak kata:", kata)
        break

# Jika nyawa habis dan masih ada '_' → kalah
if nyawa == 0 and '_' in tebak_kata:
    print(STAGES[nyawa])
    print("Sayang sekali, kamu kehabisan nyawa.")
    print("Kata yang benar adalah:", kata)
