def palindromo(frase):
    tr = str.maketrans("��������������.,;!��?", "aeiouunAEIOUUN       ")
    frase = frase.translate(tr)
    frase = "".join(frase.split())
    frase =frase.lower()
    if frase == frase[::-1]:
      return True
    else:
      return False
