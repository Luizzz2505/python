def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes_in_range(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

if __name__ == "__main__":
    start_range = int(input("Digite o início do intervalo: "))
    end_range = int(input("Digite o fim do intervalo: "))

    if start_range < 2:
        start_range = 2

    prime_list = generate_primes_in_range(start_range, end_range)

    if prime_list:
        print("Números primos no intervalo:", prime_list)
    else:
        print("Nenhum número primo encontrado no intervalo.")
