# simulate_keylogger.py - modo seguro: grava texto digitado pelo usuário no terminal
from pathlib import Path

def main():
    logs_dir = Path(__file__).parent / 'logs'
    logs_dir.mkdir(exist_ok=True)
    out_file = logs_dir / 'keys.txt'
    print('Modo simulado: digite (vários parágrafos ok). Para finalizar, pressione Ctrl+D (Linux/mac) ou Ctrl+Z then Enter (Windows).\n')
    try:
        data = []
        while True:
            line = input()
            data.append(line)
    except EOFError:
        pass
    with open(out_file, 'a', encoding='utf-8') as f:
        f.write('\n'.join(data) + '\n')
    print(f'Conteúdo salvo em {out_file}')

if __name__ == '__main__':
    main()
