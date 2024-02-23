 # TPC2: Conversor de MD para HTML

## Autor: João Vale, a93219

Inicialmente são definidas várias funções que são responsáveis por realizar as respetivas conversões de Markdown para HTML. A cada função corresponde a um tipo específico de elemento Markdown: 
1. Cabeçalhos
2. Negritos
3. Itálicos
4. Citações
5. Listas ordenadas
6. Listas não ordenadas
7. Links
8. Imagens

Posto isto, temos a função principal chamada markdown_to_html(file_path). Esta função recebe o caminho de um arquivo Markdown como entrada e lê o conteúdo do arquivo Markdown especificado pelo caminho fornecido aplicando todas as substituições necessárias para converter a marcação Markdown em HTML, utilizando as funções de conversão definidas anteriormente e expressões regulares para capturar os padrões que irão ser convertidos.