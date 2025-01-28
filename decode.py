def load_hashes_from_file(filename="hashes.txt"):
    # Membaca semua hash dan teks dari file
    hashes = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 3):  # Membaca 3 baris per entri (teks, hash, dan baris kosong)
            text = lines[i].strip().replace("Teks: ", "")
            hash_value = lines[i+1].strip().replace("Hash: ", "")
            hashes.append((text, hash_value))
    return hashes

def find_text_from_hash(hash_value, hashes):
    # Mencari teks yang sesuai dengan hash
    for text, hash in hashes:
        if hash == hash_value:
            return text
    return None

if __name__ == "__main__":
    # Memuat hash yang ada dalam file
    hashes = load_hashes_from_file()
    
    # Meminta input hash untuk memverifikasi
    hash_value = input("Masukkan SHA-256 hash untuk mencari teks asli: ").strip()

    # Mencari teks asli berdasarkan hash
    text = find_text_from_hash(hash_value, hashes)

    if text:
        print(f"Teks asli untuk hash tersebut adalah: {text}")
    else:
        print("Tidak ada teks asli yang ditemukan untuk hash ini.")
