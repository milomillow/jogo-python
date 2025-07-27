import random

palavras = [
    'Centro', 'Lumiar', 'Mury', 'Olaria', 'Riograndina', 'São Geraldo',
    'Conselheiro Paulino', 'Cordoeira', 'Parque São Clemente',
    'Córrego Dantas', 'São Pedro da Serra', 'Duas Pedras',
    'Vale do Paraíso', 'Jardim Califórnia', 'Catarcione'
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

print("🏘️ Bem-vindo ao Jogo da Forca - Nova Friburgo Edition!")
print("Adivinhe o nome do bairro:")

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
                letras_descobertas[i] = palavra[i]  # mantém maiúsculas e espaços
        print("✔ Boa! Letra correta.")
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        print("❌ Letra errada!")

if '_' not in letras_descobertas:
    print(f"\n🎉 Parabéns! Você adivinhou o bairro: {palavra}")
else:
    print(f"\n💀 Você perdeu! O bairro era: {palavra}")
