import re

def somador(texto):
    estado = "On"
    soma = 0

    # Define a expressão regular para encontrar sequências de dígitos e os caracteres "Off", "On" e "="
    regex_digitos = re.compile(r'\d+|off|on|=', re.IGNORECASE)

    # Itera sobre todas as correspondências da expressão regular no texto
    for match in regex_digitos.finditer(texto):
        # Se encontrar "Off", muda o estado para "Off"
        if match.group().lower() == "off":
            estado = "Off"
        # Se encontrar "On", muda o estado para "On"
        elif match.group().lower() == "on":
            estado = "On"
        # Se o estado for "On", soma os dígitos encontrados
        elif estado == "On" and match.group() != "=":
            soma += int(match.group())
        # Se encontrar "=", imprime o resultado da soma
        elif match.group() == "=":
            print("Resultado da soma:", soma)
    
    return soma

texto = "A soma = numeros 31 com 43 é =. Contudo, agora estando oFf = não apanha estes numeros 13 e 91. Por isso a soma continua =. Mas como esta oN agora já vai capturar o numero 7 e 8, adicionando-os à nova soma ="
resultado = somador(texto)