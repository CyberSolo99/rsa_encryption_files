import random
import argparse
import gmpy2


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(n, k=128):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def generate_prime_candidate(length):
    p = 0
    while not is_prime(p):
        p = random.getrandbits(length)
    return p


def multiplicative_inverse(e, phi):
    d_old, r_old = 0, phi
    d, r = 1, e

    while r != 0:
        q = r_old // r
        d_old, d = d, d_old - q * d
        r_old, r = r, r_old - q * r

    if d_old < 0:
        d_old += phi

    return d_old


def encrypt_file(filename, public_key):
    with open(filename, "rb") as file:
        plaintext = file.read()

    key, n = public_key
    cipher = [pow(byte, key, n) for byte in plaintext]

    with open("images(1).jpeg", "w") as file:
        file.write(" ".join(map(str, cipher)))


def decrypt_file(filename, private_key):
    with open(filename, "r") as file:
        ciphertext = list(map(int, file.read().split()))

    key, n = private_key
    plain = bytearray([pow(byte, key, n) for byte in ciphertext])

    with open("images(2).jpeg", "wb") as file:
        file.write(plain)


def main():
    parser = argparse.ArgumentParser(description="RSA Encryption/Decryption Program")
    parser.add_argument(
        "-k",
        "--keylength",
        type=int,
        required=True,
        help="Length of the RSA key in bits",
    )
    args = parser.parse_args()

    # Генерация простых чисел длиной keylength/2 бит
    p = generate_prime_candidate(args.keylength // 2)
    q = generate_prime_candidate(args.keylength // 2)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Поиск e, такого что gcd(e, phi) = 1
    e = 65537  # Используем стандартное значение для e
    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e += 1

    d = multiplicative_inverse(e, phi)

    # Проверка условия d > 1/3 * n^(1/4) для защиты от атаки Винера
    n_root_4 = gmpy2.iroot(n, 4)[0]  # Вычисление четвертого корня из n как целое число
    while d <= (1 / 3) * n_root_4:
        e += 1
        if gcd(e, phi) == 1:
            d = multiplicative_inverse(e, phi)

    print("p =", p)
    print("q =", q)
    print("n =", n)
    print("phi(n) =", phi)
    print("e =", e)
    print("d =", d)
    print("gcd(e,phi(n)) =", gcd(e, phi))
    print(f"Public key: {e, n}")
    print(f"Private key: {d, n}")

    # Шифрование файла
    encrypt_file("images.jpeg", (e, n))
    print("Файл images.jpeg зашифрован и сохранен как images(1).jpeg")

    # Расшифровка файла
    decrypt_file("images(1).jpeg", (d, n))
    print("Зашифрованный файл images(1).jpeg расшифрован и сохранен как images(2).jpeg")


if __name__ == "__main__":
    main()
