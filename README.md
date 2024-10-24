# Contador de Letras 'A'

## Descrição
Este projeto foi desenvolvido como parte do processo de seleção de estágio da Target Sistemas. 
O objetivo do programa é contar quantas vezes a letra **'a'** (incluindo acentuadas) aparece em uma string fornecida pelo usuário. 
O programa remove acentos e pontuações antes de realizar a contagem.

## Funcionalidades
- Valida a entrada do usuário para garantir que não esteja vazia, que contenha apenas números e contenha pelo menos uma letra.
- Remove acentos e pontuações da string antes de realizar a contagem.
- Conta todas as ocorrências da letra **'a'** ou **'A'**, incluindo variações acentuadas (á, à, â, ã).

## Tecnologias Utilizadas
- **Python**
- Bibliotecas:
  - `unicodedata`: Para normalização e remoção de acentos.
  - `string`: Para remoção de pontuação.

## Como Executar o Projeto
1. Clone o repositório:
   ```bash
    git clone https://github.com/PauloMPPatricio/string-character-counter.git
   
3. Navegue até o diretório do projeto:
   ```bash
    cd string-character-counter
   
5. Execute o script contador_a.py:
   ```bash
    python contador_a.py

## Exemplo de Uso
   Quando o usuário fornecer a entrada, o programa contará quantas vezes a letra 'a' ou suas variantes acentuadas aparecem na string.

## Exemplo de execução
   Digite uma letra, palavra, frase ou texto: A árvore caiu na estrada.
  
   A letra 'a' aparece 4 vezes na letra, palavra, frase ou texto digitado.
      
## Contribuições
Contribuições são bem-vindas! Se você deseja melhorar este projeto, fique à vontade para abrir issues ou enviar pull requests.

## Licença
Este projeto está licenciado sob a MIT License.
