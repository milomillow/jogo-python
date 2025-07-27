import random

palavras = [
    'Information Society', 'InSoc', 'Kurt Harland', 'Paul Robb', 'Amanda Kramer', 'James Cassidy',
    'Peace and Love', 'Synthpop', 'Repetition', 'Running', 'Walking Away', 'Pure Energy', 'Peace and Love'
]

palavra = random.choice(palavras)
palavra_oculta = palavra.lower()

letras_descobertas = []
for c in palavra:
    if c == ' ':
        letras_descobertas.append(' ')
    else:
        letras_descobertas.append('_')

tentativas = 6
letras_erradas = []

print("🖥️ SYSTEM BOOTING...")
print("🎶 WELCOME TO INFORMATION SOCIETY EDITION 🎵")
print("Try to guess the word or phrase!")

while tentativas > 0 and '_' in letras_descobertas:
    print("\nPalavra: " + ' '.join(letras_descobertas))
    print(f"Erros: {', '.join(letras_erradas)}")
    print(f"Tentativas restantes: {tentativas}")
    
    letra = input("Digite uma letra: ").lower()

    if not letra.isalpha() or len(letra) != 1:
        print("Digite apenas uma letra válida.")
        continue

    if letra in letras_descobertas or letra in letras_erradas:
        print("Você já tentou essa letra.")
        continue

    if letra in palavra_oculta:
        for i, l in enumerate(palavra_oculta):
            if l == letra:
                letras_descobertas[i] = palavra[i]  # preserva maiúsculas e espaços
        print("✔ Boa! Letra correta.")
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        print("❌ Letra errada!")

if '_' not in letras_descobertas:
    print("\n🎉 Parabéns! Você adivinhou a palavra:", palavra)
else:
    print("\n💀 Você perdeu! A palavra era:", palavra)
