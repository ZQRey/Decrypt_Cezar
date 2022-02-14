# М БЭНИФ№ SЦWKRQ
print('Программа разшифровки шифра Цезаря. Create 3QRey')

# Ключи шифра должны совпадать с зашифроваными
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ!"№;%:?*()_+Ё123456789.,'

print('Введите сообщение для разшифровки.')
message = input('> ')

for key in range(len(SYMBOLS)):
    translated = ''

    # Разшифровываем каждый символ в сообщении:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol) # Получаем числовое значение
            num = num - key # Расшифровываем значение

            # выполняем переход по кругу если число меньше 0
            if num < 0:
                num = num + len(SYMBOLS)

            # Добавляем разшифрованный символ в translate
            translated = translated + SYMBOLS[num]
        else:
            translated = translated + symbol
    print(f'Key #{key}: {translated}')
