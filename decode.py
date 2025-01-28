def load_hashes_from_file(filename="hashes.txt"):
    # Membaca semua hash dari file
    with open(filename, "r") as f:
        hashes = f.readlines()
    return [hash.strip() for hash in hashes]

def check_hash_against_text(text, hashes):
    # Mengecek apakah hash dari teks cocok dengan salah satu hash di file
    from hashlib import sha256
    text_hash = sha256(text.encode()).hexdigest()
    return text_hash in hashes

if __name__ == "__main__":
    # Memuat hash yang ada dalam file
    hashes = load_hashes_from_file()
    
    # Meminta input teks untuk memverifikasi hash
    text = input("Masukkan teks untuk memverifikasi SHA-256: ")
    
    if check_hash_against_text(text, hashes):
        print("Teks cocok dengan salah satu hash di file.")
    else:
        print("Teks tidak cocok dengan hash di file.")
