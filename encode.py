import hashlib

def generate_sha256(text):
    # Menghitung hash SHA-256 dari teks
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    return sha256_hash

def save_hash_to_file(text, hash_value, filename="hashes.txt"):
    # Menyimpan hash dan teks ke dalam file dengan keterangan
    with open(filename, "a") as f:
        f.write(f"Teks: {text}\nHash: {hash_value}\n\n")

if __name__ == "__main__":
    text = input("Masukkan teks untuk menghasilkan SHA-256: ")
    hash_value = generate_sha256(text)
    print(f"SHA-256 Hash: {hash_value}")
    save_hash_to_file(text, hash_value)
    print(f"Hash disimpan di file 'hashes.txt'.")
