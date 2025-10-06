# decrypt.py - Reverte a cifragem XOR aplicada por encrypt.py
import os
from pathlib import Path

def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def process_files(folder: Path, key: bytes):
    for p in folder.glob('*.enc'):
        with open(p, 'rb') as f:
            data = f.read()
        out = xor_bytes(data, key)
        # cria arquivo sem sufixo .enc
        out_path = p.with_name(p.name.replace('.enc',''))
        with open(out_path, 'wb') as f:
            f.write(out)
        print(f"[+] Decrypted {p} -> {out_path}")

def main():
    folder = Path(__file__).parent / 'test_files'
    if not folder.exists():
        print('Pasta test_files não encontrada.')
        return
    pwd = input('Senha para descriptografar (mesma senha usada na cifragem): ').strip().encode('utf-8')
    if not pwd:
        print('Senha vazia. Abortando.')
        return
    process_files(folder, pwd)
    print('\nConcluído. Verifique os arquivos gerados.')

if __name__ == '__main__':
    main()
