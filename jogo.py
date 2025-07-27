import random

# Lista de palavras para o jogo
palavras = ['Linux', 'Linus Torvalds', 'Ubuntu', 'Debian', 'Fedora', 'Red Hat', 'Arch Linux', 'Kali Linux', 'SUSE', 'Gentoo', 'Manjaro', 'Raspberry Pi', 'Terminal', 'Kernel', 'Shell', 'Bash', 'Zsh', 'Git']

palavra = random.choice(palavras)
palavra_oculta = palavra.lower()  # versão em minúsculas para comparar
letras_descobertas = []

# Revela os espaços já no início
for c in palavra:
    if c == ' ':
        letras_descobertas.append(' ')
    else:
        letras_descobertas.append('_')

tentativas = 6
letras_erradas = []

print("🐧 Bem-vindo ao Jogo da Forca (Linux Edition)!")
print("Adivinhe a palavra ou frase:")

while tentativas > 0 and '_' in letras_descobertas:
    print("\nPalavra: " + ' '.join(letras_descobertas))
    print(f"Erros: {', '.join(letras_erradas)}")
    print(f"Tentativas restantes: {tentativas}")
    
    letra = input("Digite uma letra: ").lower()

    if not letra.isalpha() or len(letra) != 1:
        print("Digite apenas uma letra válida.")
        continue

    if letra in letras_erradas or letra in letras_descobertas:
        print("Você já tentou essa letra.")
        continue

    if letra in palavra_oculta:
        for i, l in enumerate(palavra_oculta):
            if l == letra:
                letras_descobertas[i] = palavra[i]  # preserva maiúsculas
        print("✔ Boa! Letra correta.")
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        print("❌ Letra errada!")

# Resultado final
if '_' not in letras_descobertas:
    print("\n🎉 Parabéns! Você adivinhou: " + palavra)
else:
    print("\n💀 Você perdeu! A palavra era: " + palavra)
