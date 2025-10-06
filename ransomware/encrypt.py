# encrypt.py - Ransomware simulado (XOR) - EDUCATIVO E SEGURO
import os
from pathlib import Path

def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def process_files(folder: Path, key: bytes, mode='encrypt'):
    for p in folder.glob('*.txt'):
        if p.name.endswith('.enc.txt') and mode=='encrypt':
            # já está encriptado (precaução)
            continue
        with open(p, 'rb') as f:
            data = f.read()
        out = xor_bytes(data, key)
        if mode == 'encrypt':
            out_path = p.with_name(p.name + '.enc')
        else:
            # decrypt: if file endswith .enc remove suffix
            out_path = p.with_name(p.name.replace('.enc',''))
        with open(out_path, 'wb') as f:
            f.write(out)
        # for safety, do not delete original; just keep both files
        print(f"[+] Processed {p} -> {out_path}")

def main():
    folder = Path(__file__).parent / 'test_files'
    if not folder.exists():
        print('Pasta test_files não encontrada. Crie e coloque arquivos .txt para testar.')
        return
    pwd = input('Senha para cifrar (usa como chave XOR): ').strip().encode('utf-8')
    if not pwd:
        print('Senha vazia. Abortando.')
        return
    process_files(folder, pwd, mode='encrypt')
    print('\nConcluído. Lembre-se: este é um script educacional. Não use em sistemas de produção.')


if __name__ == '__main__':
    main()
