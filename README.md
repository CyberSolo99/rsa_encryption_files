# RSA Encryption/Decryption Program

## Описание

Эта программа реализует базовое RSA шифрование и расшифровку файлов. Пользователь может выбрать длину ключа с помощью аргументов командной строки. Программа шифрует файл `images.jpeg` и сохраняет результат в виде зашифрованного файла `images(1).jpeg`. Расшифрованный файл сохраняется как `images(2).jpeg`.

## Особенности

- Генерация простых чисел с использованием теста Миллера-Рабина.
- Проверка на атаку Винера для дополнительной безопасности.
- Шифрование и расшифровка файлов с использованием RSA алгоритма.
- Возможность выбора длины ключа через аргументы командной строки.
- Использование библиотеки `gmpy2` для работы с большими числами.

## Установка

1. Убедитесь, что у вас установлен Python 3.
2. Установите необходимые библиотеки с помощью pip:

   ```sh
   pip install gmpy2
   ```

## Использование

### Запуск программы

Для запуска программы используйте Makefile. Вы можете указать длину ключа с помощью аргумента `KEYLENGTH`.

```sh
make run KEYLENGTH=128
```

### Пример использования

- Генерация и шифрование файла с длиной ключа 128 бит:

   ```sh
   make run KEYLENGTH=128
   ```

### Дополнительные команды

- Удаление всех временных файлов:

   ```sh
   make clean
   ```

- Вычисление MD5 хэшей для всех JPEG файлов:

   ```sh
   make checksum
   ```

## Пример вывода

Пример вывода программы при запуске команды `make run KEYLENGTH=2048`:

```
rm -f *.enc *.dec "images(1).jpeg" "images(2).jpeg"
python3 rsa.py -k 2048
p = [generated prime p]
q = [generated prime q]
n = [calculated n]
phi(n) = [calculated phi]
e = 65537
d = [calculated d]
gcd(e,phi(n)) = 1
Public key: (65537, [calculated n])
Private key: ([calculated d], [calculated n])
Файл images.jpeg зашифрован и сохранен как images(1).jpeg
Зашифрованный файл images(1).jpeg расшифрован и сохранен как images(2).jpeg
md5sum *.jpeg
[MD5 hashes of the files]
```

## Структура файлов

- `rsa.py`: Основной скрипт программы.
- `Makefile`: Скрипт для автоматизации запуска и очистки временных файлов.
- `README.md`: Документация программы.

## Лицензия

Эта программа распространяется под [MIT License](https://opensource.org/licenses/MIT).