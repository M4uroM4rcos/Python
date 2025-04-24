#importação de biblioteca
from deep_translator import GoogleTranslator

try:
    # declaração de variaveis
    tradutor = GoogleTranslator(source='auto', target='pt')
    while True:
        # declaração de variaveis
        texto_original = input('Digite o texto a ser traduzido e, qualquer idioma: ')
        texto_traduzido = tradutor.translate(texto_original)

        # exibe o yesto traduzido
        print(f'Texto traduzido: "{texto_traduzido}"\n')

        # informa se deseja atraduir outro texto ou encerrar
        encerrar = input('Deseja traduzir outro texto? (s/n)')
        match encerrar:
            case "s":
                continue
            case "n":
                break
            case _:
                print('Opção invaloda.')

except Exception as e:
    print(f'Não doi possivel traduzir. {e}.')