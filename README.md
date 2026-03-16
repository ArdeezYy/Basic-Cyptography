# Basic-Cryptography (Layered OTP & Rail Fence) 🔐

This repository contains a **Product Cipher** implementation that combines **Substitution** and **Transposisiton** methods. This project was developed as part of the **System Security (Kamsis)** course at Telkom University.

## 🚀 Key Features
- **Multi-Step Encryption:** A hybrid system utilizing both One-Time Pad (OTP) and Rail Fence Cipher.
- **Secure Key Generation:** Leverages the Python `secrets` module (CSPRNG) to ensure high-entropy, cryptographically secure keys.
- **Algorithmic Visualization:** Features a built-in demo mode to visualize the zig-zag character repositioning.
- **Mathematical Precision:** Guaranteed 100% data recovery (lossless) through a precise decryption pipeline.

## 🛠️ Theoretical Foundation
The program implements the two core principles of secure communication defined by Claude Shannon:

1. **Confusion:** Achieved via the **OTP** layer, which obscures the relationship between the plaintext and the ciphertext by altering character identities.
2. **Diffusion:** Achieved via the **Rail Fence** layer, which spreads the influence of individual plaintext characters across the entire ciphertext by shuffling their positions.

### Mathematical Model
The OTP layer operates using modular arithmetic (Modulo 26):

**Encryption:**
$$C_i = (P_i + K_i) \pmod{26}$$

**Decryption:**
$$P_i = (C_i - K_i) \pmod{26}$$

*(Where $P$ = Plaintext, $K$ = Key, and $C$ = Ciphertext)*

## 📂 Project Structure
```text
.
├── src/
│   └── basickripografi2.py  # Main source code
│   └── flowchart.png        # System architecture diagram
