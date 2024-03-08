# TPC4: Analisador Léxico

## Autor: João Vale, a93219

No início do código, são definidos os tokens que posteriormente vão ser reconhecidos pelo analisador léxico, e para cada token, são definidas as expressões regulares que o descrevem. Depois são definidas as funções que serão usadas pelo analisador léxico para reconhecer os tokens na entrada. Essas recebem a entrada e tentam fazer uma correspondência com a expressão regular associada ao token. Se houver uma correspondência, é criado um token e retornado. Caso contrário, é gerado um erro devido ao caractere não ser reconhecido.