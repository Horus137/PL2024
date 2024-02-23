# TPC3: Somador on/off

## Autor: João Vale, a93219

Primeiramente, é definida a função somador(texto), onde são inicializadas as variáveis soma e estado a "on" . Depois disto, temos expressão regular para encontrar sequências de dígitos, os caracteres "Off", "On" e "=" que vai ser utilizada para iterar o texto pretendido para ir calculando a soma dos digitos encontrados. Para tal acontecer, primeiro é verificado que não é encontrada a sequencia "off". Caso contrário, o estado muda de on para off e vice-versa quando encontra a sequencia "on". Seguidamente é verificado se o estado está on para ver se os digitos encontrados naquele momento são ou não adicionados à soma. Finalmente quando se encontrar "=" é imprimida a soma atual para o stdout.