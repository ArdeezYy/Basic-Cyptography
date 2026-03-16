# Ardika Putra Hadian - 101032300240


import secrets
import string

def generate_otp_key(length):
    return ''.join(secrets.choice(string.ascii_uppercase) for _ in range(length))

def encrypt_otp(plaintext, key):
    res = ""
    for p, k in zip(plaintext, key):
        res += chr((ord(p) - 65 + ord(k) - 65) % 26 + 65)
    return res

def decrypt_otp(ciphertext, key):
    res = ""
    for c, k in zip(ciphertext, key):
        res += chr((ord(c) - 65 - (ord(k) - 65)) % 26 + 65)
    return res

def rail_fence_process(text, key, mode='encrypt'):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    if mode == 'encrypt':
        down, row, col = False, 0, 0
        for char in text:
            if row == 0 or row == key - 1: down = not down
            rail[row][col] = char
            col += 1
            row = row + 1 if down else row - 1
        return "".join([rail[i][j] for i in range(key) for j in range(len(text)) if rail[i][j] != '\n'])
    else:
        
        down, row, col = None, 0, 0
        for i in range(len(text)):
            if row == 0: down = True
            if row == key - 1: down = False
            rail[row][col] = '*'
            col += 1
            row = row + 1 if down else row - 1
        idx = 0
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] == '*' and idx < len(text):
                    rail[i][j] = text[idx]; idx += 1
        res, row, col = [], 0, 0
        for i in range(len(text)):
            if row == 0: down = True
            if row == key - 1: down = False
            res.append(rail[row][col])
            col += 1
            row = row + 1 if down else row - 1
        return "".join(res)

# main
print("=== TUGAS 1: KRIPTOGRAFI MULTI-STEP (TK-47-01) ===")
p_original = input("Masukkan Plaintext: ").upper().replace(" ", "")

# 1. otp dulu
k_otp = generate_otp_key(len(p_original))
c_otp = encrypt_otp(p_original, k_otp)
print(f"\n[STEP 1: OTP ENCRYPTION] ")
print(f"Input: {p_original} | Key: {k_otp}")
print(f"Output (C1): {c_otp}")

# 2. lalu rail fence (demo)
k_rail = 3
print(f"\n[STEP 2: RAIL FENCE DEMO ON C1]")
# Mencoba dekripsi pada data yang belum di-enkripsi rail fence
demo_dec = rail_fence_process(c_otp, k_rail, mode='decrypt')
print(f"C1 di-Decrypt Rail Fence: {demo_dec} (Reposisi Terbalik)")

# enkripsi rail fence
final_cipher = rail_fence_process(c_otp, k_rail, mode='encrypt')
print(f"C1 di-Encrypt Rail Fence (Final): {final_cipher}")

# 3. deskripsi akhir
print(f"\n[STEP 3: FULL DECRYPTION PROOF] ")
rev_rail = rail_fence_process(final_cipher, k_rail, mode='decrypt')
rev_final = decrypt_otp(rev_rail, k_otp)
print(f"Final -> Rail Decrypt: {rev_rail}")
print(f"Result -> OTP Decrypt: {rev_final}")