
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    def print_fail():
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        # не получилось собрать все условия проверки адресов одной строкой, поэтому разбил на 3 части
    if '@' not in  sender or'@' not in recipient:
        print_fail()
        return
    if not (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')):
        print_fail()
        return
    if not (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')):
        print_fail()
        return
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
