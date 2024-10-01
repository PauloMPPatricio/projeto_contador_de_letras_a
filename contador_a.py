""" Projeto Para a seleção de estágio da Target Sistemas
    Nome: Paulo Mauricio Pereira Patricio
    Estudante: Análise e Desenvolvimento de Sistemas

   - Biblioteca unicodedata, permitirá normalizar a string e remover acentos.
   - Biblioteca string, permitirá identificar os caracteres de pontuação e removê-los antes
     da contagem."""
import unicodedata
import string


class VerificadorDeLetraA:
    def __init__(self, entrada):
        self.entrada = entrada

    def validar_entrada(self):
        """Verifica se a entrada não é vazia, contém letras e pode conter números e pontuações."""
        if not isinstance(self.entrada, str) or len(self.entrada.strip()) == 0:
            return False  # Verifica se a entrada é uma string e não está vazia

        # Verificar se a string contém pelo menos uma letra
        contem_letra = any(caractere.isalpha() for caractere in self.entrada)

        if not contem_letra:
            return False  # Se não tiver nenhuma letra, a entrada é inválida

        return True

    @staticmethod
    def remover_acentos(texto):
        """Normaliza a string para remover acentos."""
        return ''.join(
            c for c in unicodedata.normalize('NFKD', texto)
            if unicodedata.category(c) != 'Mn'
        )

    @staticmethod
    def remover_pontuacao(texto):
        """Remove a pontuação da string."""
        return ''.join(c for c in texto if c not in string.punctuation)

    def contar_letras_a(self):
        """Conta quantas vezes a letra 'a' ou 'A' aparece na string, incluindo acentuadas."""
        if self.validar_entrada():
            # Normalizar a string para remover acentos
            entrada_normalizada = self.remover_acentos(self.entrada.lower())
            # Remover a pontuação antes de contar as letras
            entrada_sem_pontuacao = self.remover_pontuacao(entrada_normalizada)
            # Contar quantas vezes 'a' aparece na string sem pontuação e normalizada
            contagem = entrada_sem_pontuacao.count('a')
            return contagem
        else:
            raise ValueError("Entrada inválida! "
                             "A entrada não pode ser vazia ou conter apenas números. "
                             "Deve haver pelo menos uma letra, palavra, frase ou texto.")


# Função principal para execução do programa
def main():
    while True:
        entrada_usuario = input("Digite uma letra, palavra, frase ou texto: ")
        verificador = VerificadorDeLetraA(entrada_usuario)

        try:
            contagem = verificador.contar_letras_a()
            if contagem > 0:
                print(f"A letra 'a' aparece {contagem} vezes na letra, palavra, frase ou texto digitado.")
            else:
                print("A letra 'a' não foi encontrada na letra, palavra, frase ou texto digitado.")
            break  # Saímos do loop se tudo ocorrer bem
        except ValueError as e:
            print(e)
            print("Por favor, tente novamente.")


if __name__ == "__main__":
    main()
