import argparse

LETTERS = "abcdefghijklmnopqrstuvwxyz"


def decrypt_message(msg: str, key: int):
    """
    Decrypts a string based on the Caesar Cipher Algorithm

    Parameters:
    msg (str): Message to be decrypted
    key (int): Encryption key

    Returns:
    str: Containing decrypted message
    """

    # enter the key value to decrypt
    decrypted_message = ""

    for ch in msg:

        if ch.lower() in LETTERS:
            position = LETTERS.find(ch.lower())
            new_pos = (position - key) % 26
            new_char = LETTERS[new_pos] if ch.islower() else LETTERS[new_pos].upper()
            decrypted_message += new_char
        else:
            decrypted_message += ch
    return decrypted_message


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='El reto más difícil: verano 2024. Semana 1, CRIPTOGRAFÍA. Consigne '
                                                 'un mensaje de entrada y el programa le mostrará por pantalla el '
                                                 'mensaje descrifrado. ',
                                     epilog='luismesalas@gmail.com')
    parser.add_argument("--mensaje", "-m", type=str, required=True, help="Mensaje a descifrar")
    parser.add_argument("--clave", "-c", type=int, required=True, help="Clave de cifrado (desplazamiento)")

    args = parser.parse_args()
    print(f"El mensaje oculto es: '{decrypt_message(args.mensaje, args.clave)}'")
