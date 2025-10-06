# Keylogger Simulado (educacional)

**Objetivo:** Demonstrar captura de teclas em ambiente controlado e formas de envio automático (simulado).

**Modo seguro incluído:** `simulate_keylogger.py` pede que você digite no terminal; tudo que você digitar será salvo em `logs/keys.txt`.
- Isso evita usar listeners em nível de sistema e mantém o exemplo simples e portátil.

**Instruções rápidas (modo simulado):**
1. `python simulate_keylogger.py`
2. Digite algumas linhas e use `CTRL+D` (Linux/macOS) ou `CTRL+Z` + Enter (Windows) para terminar.
3. Verifique `keylogger/logs/keys.txt`.

**Código comentado:** Há trechos comentados que mostram como usar `pynput` para captura em tempo real e `smtplib` para envio por email.
Esses trechos estão comentados por segurança e exigem configuração adicional (e consentimento explícito) para uso real.
