import pandas as pd
import re
from unidecode import unidecode


class Contasbancarias:

    def __init__(self):
        pass

    def criar_contas(self):
        df_contas = pd.read_csv('banco_de_dados/contas.csv', sep=';', encoding='latin1')
        print(df_contas)
        nome = input('Nome da conta: ')
        instituicao = input('Nome do Banco: ')
        saldo = float(input('Saldo atual da conta: '))
        try:
            i = df_contas.index[-1] + 1
            id_conta = df_contas.iloc[-1, 0] + 1
        except IndexError:
            i = 0
            id_conta = 1001
        df_contas.loc[i] = [id_conta, nome, instituicao, saldo]
        print(df_contas)
        df_contas.to_csv('banco_de_dados/contas.csv', index=False, sep=';', encoding='latin1')

    def criar_cartao_credito(self):
        df_cartoes = pd.read_csv('banco_de_dados/cartao_credito.csv', sep=';', encoding='latin1')
        print(df_cartoes)
        nome = input('Nome do Cartão: ')
        bandeira = input('Bandeira do Cartão: ')
        instituicao = input('Instituição Financeira: ')
        dia_fechamento_fat = int(input('Dia do Fechamento da Fatura: '))
        dia_vencimento_fat = int(input('Dia do Vencimento da Fatura: '))
        saldo = float(input('Saldo atual da fatura: '))
        try:
            i = df_cartoes.index[-1] + 1
            id_cartao = df_cartoes.iloc[-1, 0] + 1
        except IndexError:
            i = 0
            id_cartao = 2001
        df_cartoes.loc[i] = [id_cartao, nome, bandeira, instituicao, dia_fechamento_fat, dia_vencimento_fat, saldo]
        print(df_cartoes)
        df_cartoes.to_csv('banco_de_dados/cartao_credito.csv', index=False, sep=';', encoding='latin1')

    def _tratamento_strigs(self, string, *karg):
        '''
        Função troca ou retira caracteres especiais e formatata um texto segundo alguns parametros.

        Caso não defina nenhum parametro karg a função apenas retirará ou trocará os caracteres especiais e deixará as letras minusculas.

        Caso defina algum parametro karg a função manterá apenas os parametros definidos.

        :param string: Texto a ser formatado
        :param karg: 'm' manter minusculas, 'M' manter maiusculas, 'N' Manter números, 'E' Manter espaços
        :return: Texto formatado
        '''

        if 'M' not in karg:
            string = string.lower()
        string = unidecode(string)
        m = ''
        M = ''
        N = ''
        E = ''
        if karg:
            for k in karg:
                if k == 'm':
                    m = 'a-z'
                if k == 'M':
                    M = 'A-Z'
                if k == 'N':
                    N = '0-9'
                if k == 'E':
                    E = ' '
            parametros = m + M + N + E
            nova_string = re.sub(fr"[^{parametros}]", "", string)
        else:
            nova_string = string
        return nova_string

    def fazer_lancamentos(self):
        # df_lancamentos = pd.read_csv('banco_de_dados/lancamentos.csv', sep=';', encoding='latin1')
        # # print(df_lancamentos.info())
        # try:
        #     i = df_lancamentos.index[-1] + 1
        #     id_cartao = df_lancamentos.iloc[-1, 0] + 1
        # except IndexError:
        #     i = 0
        #     id_cartao = 100001
        # tipo_rec_desp = input('É receita ou despesa? ')
        # tipo_rec_desp = self._tratamento_strigs(tipo_rec_desp)
        # while True:
        #     if tipo_rec_desp in ('receita', 'despesa'):
        #         break
        #     else:
        #         tipo_rec_desp = input('ERRO na digitação - Digite receita ou despesa: ')
        #         tipo_rec_desp = self._tratamento_strigs(tipo_rec_desp)
        #
        # print(tipo_rec_desp)
        list_descricao = ['Alimentação', 'Transporte']
        descricao = input(f'''Digite a Descrição do Lançamento
{list_descricao}:
''')
        descricao = self._tratamento_strigs(descricao)
        print(descricao)
        # categoria = input('Digite uma categoria para o lançamento: ')
        # print(categoria)
        # metodo = input('É crédito ou Débito? ')
        # print(metodo)
        # local_lancamento = input('Qual cartão ou conta vai lançar? ')
        # print(local_lancamento)
        # id_conta_cartao = ''
        # print(id_conta_cartao)
        # valor = input('Digite o valor: ')
        # print(valor)
        # data = input('Digite a data do lançamento: DD/MM/AAAA: ')
        # while True:
        #     if len(data) != 10:
        #         data = input('Formato invalido: Digite a data novamente: DD/MM/AAAA: ')
        #     else:
        #         break
        # dia = data[:2]
        # mes = data[3:5]
        # ano = data[6:]

    def ler_contas(self):
        df_contas_atuais = pd.read_csv('banco_de_dados/contas.csv', sep=';', encoding='latin1')
        print(df_contas_atuais)

    def ler_cartao_credito(self):
        df_cartoes = pd.read_csv('banco_de_dados/cartao_credito.csv', sep=';', encoding='latin1')
        print(df_cartoes.info())
        # df_cartoes.loc[0, 'id'] = 2002
        # print(df_cartoes.loc[lambda df: df_cartoes['id'] == 2002])

    def ler_lancamentos(self):
        df_lancamentos = pd.read_csv('banco_de_dados/lancamentos.csv', sep=';', encoding='latin1')
        print(df_lancamentos.info())