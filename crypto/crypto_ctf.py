# crypto_ctf.py

import codecs

def main():
    encoded = "QNYVFRP{frperg_pvcure}" 

    print("📜 Intercepted ROT13 Message:")
    print(f"Flag looks like: {encoded}")
    print("\nDecode it to get the real flag!")

    while True:
        user_input = input("\nEnter decoded flag: ").strip()

        # Decode stored value at runtime instead of revealing it in file
        real_flag = codecs.decode(encoded, "rot_13")

        if user_input == real_flag:
            print("✅ Correct! You captured the flag.")
            break
        else:
            print("❌ Incorrect. Hint: It's ROT13 — try harder!")

if __name__ == "__main__":
    main()