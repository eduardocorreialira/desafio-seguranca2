# Ransomware Simulado (educacional)

**Objetivo:** Demonstrar, em ambiente controlado, como um processo de criptografia de arquivos poderia funcionar e como reverter a operação.

**Como funciona neste repositório (seguro):**
- O script `encrypt.py` aplica uma cifragem XOR simples (educacional) em todos os arquivos `.txt` dentro de `test_files/`.
- O script `decrypt.py` reverte a operação usando a mesma senha/ chave.
- **NÃO** altera ou toca em arquivos fora de `test_files/`.

**Instruções:**
1. Coloque arquivos `.txt` de teste em `ransomware/test_files/`.
2. Execute `python encrypt.py` e informe uma senha (pode ser qualquer texto).
3. Para reverter, execute `python decrypt.py` e informe a mesma senha.

*Observação de segurança:* Este método XOR é propositalmente simples e **não** é recomendado para uso real. Serve apenas para fins educacionais e demonstração.
