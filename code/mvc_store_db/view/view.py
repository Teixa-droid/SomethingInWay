from _typeshed import Self


class View:
    """
    ***************************************************************
    * A view for a store DB*
    ***************************************************************
    """
    def start(self):
        print('==========================================')
        print(' Bem vindo!')
        print('==========================================')
    
    def start(self):
        print('==========================================')
        print(' Ate a proxima!')
        print('==========================================')
    
    def main_menu(self):
        print('==========================================')
        print('-- Menu Principal --')
        print('==========================================')
        print('1. CPs')
        print('2. Produtos')
        print('3. Clientes')
        print('4. Entregas')
        print('5. Sair')
        print('==========================================')
    
    def option(self, last):
        print('Seleciona uma opção (1-'+last+'): ', end='')

    def not_valid_option(self):
        print('Opção invalida!\n Tenta de novo')
    
    def ask(self, output):
        print(output, end= '')
    
    def msg(self, output):
        print(output)
    
    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+'+str(id)+' se '+op+' corretamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))
    
    """
    ***************************************************************
    * A view for a store DB*
    ***************************************************************
    """
    def zips_menu(self):
        print('==========================================')
        print('-- SubMenu CPs --')
        print('==========================================')
        print('1. Adicionar CPs')
        print('2. Mostrar CP')
        print('3. Mostrar todos os CPs')
        print('4. Mostrar CPs de uma cidade')
        print('5. Atualizar CP')
        print('6. Apagar CP')
        print('7. Voltar')
        print('==========================================')
    
    def show_a_zip(self, record):
        print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}')
    
    def show_zip_header(self, header):
        print(header.center(78,'*'))
        print('CP'.ljust(6)+'|'+'Cidade'.ljust(35)+'|'+'Estado'.ljust(35))
        print('-'*78)
    
    def show_zip_midder(self):
        print('-'*78)
    
    def show_zip_footer(self):
        print('*'*78)
    
    """
    ***************************************************************
    * A view for products*
    ***************************************************************
    """
    def zips_menu(self):
        print('==========================================')
        print('-- SubMenu Produtos --')
        print('==========================================')
        print('1. Adicionar produto')
        print('2. Mostrar produto')
        print('3. Mostrar todos os produtos')
        print('4. Mostrar produtos de uma marca')
        print('5. Mostrar produtos entre preços')
        print('6. Atualizar produto')
        print('7. Apagar produto')
        print('8. Voltar')
        print('==========================================')

    def show_a_product(self, record):
        print('ID:', record[0])
        print('Nome:', record[1])
        print('Marca:', record[2])
        print('Descrição:', record[3])
        print('Preço:', record[4])
    
    def show_product_header(self, header):
        print(header.center(48,'*'))
        print('-'*48)
    
    def show_product_midder(self):
        print('-'*48)
    
    def show_product_footer(self):
        print('*'*48)
    
    """
    ***************************************************************
    * Views for clients*
    ***************************************************************
    """
    def zips_menu(self):
        print('==========================================')
        print('-- SubMenu Clientes --')
        print('==========================================')
        print('1. Adicionar cliente')
        print('2. Mostrar cliente')
        print('3. Mostrar todos os clientes')
        print('4. Mostrar cliente de um CP')
        print('5. Atualizar cliente')
        print('6. Apagar cliente')
        print('7. Voltar')
        print('==========================================')
    
    def show_a_clients(self, record):
        print('ID:', record[0])
        print('Nome:', record[1])
        print('Apelido paterno:', record[2])
        print('Apelido materno:', record[3])
        print('Rua:', record[4])
        print('No exterior:', record[5])
        print('No interior:', record[6])
        print('Colonia:', record[7])
        print('Cidade:', record[11])
        print('Estado:', record[12])
        print('CP:', record[8])
        print('Email:', record[9])
        print('Telefone:', record[10])
    
    def show_a_client_brief(self, record):
        print('ID:', record[0])
        print('Nome:', record[1]+' '+record[2]+' '+record[3])
        print('Direction:', record[4]+' '+record[5]+' '+record[6]+', '+record[7])
        print(record[11]+' '+record[12]+' '+record[8])
        print('Email:', record[9])
        print('Telefone:', record[10])
    
    def show_client_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)
    
    def show_client_midder(self):
        print('-'*53)
    
    def show_client_footer(self):
        print('*'*53)
    
    """
    ***************************************************************
    * Views for Orders*
    ***************************************************************
    """

    def orders_menu(self):
        print('==========================================')
        print('-- SubMenu entregas --')
        print('==========================================')
        print('1. Adicionar entrega')
        print('2. Mostrar entrega')
        print('3. Mostrar todos as entregas')
        print('4. Mostrar todos as entregas da ficha')
        print('5. Mostrar todos as entregas do cliente')
        print('6. Atualizar os dados da entrega')
        print('7. Adicionar produtos a uma entrega')
        print('8. Modificar produtos a uma entrega')
        print('9. Apagar produtos a uma entrega')
        print('10. Apagar entrega')
        print('11. Voltar')
        print('==========================================')
    
    def show_order(self, record):
        print('ID:', record[0])
        print('Estado da entrega:', record[2])
        print('Ficha:', record[3])
        print('Dados do cliente:'.center(81,'*'))
        self.show_a_client_brief(record[5:])
    
    def show_order_midder(self):
        print('/'*81)
    
    def show_order_total(self, record):
        print('Total da entrega: '+str(record[4]))
    
    def show_order_footer(self):
        print('+'*81)
    
    """
    ***************************************************************
    * Views for Order Details *
    ***************************************************************
    """
    def show_a_order_details(self, records):
        print(f'{records[0]:<5} | {records[1]:<20} | {records[2]:<20} | {records[3]:<11} | {records[3]:<9}| {records[3]:<11}')
    
    def show_order_details_header(self):
        print('-'*81)
        print('ID'.ljust(5)+'|'+'Produto'.ljust(20)+'|'+'Marca'.ljust(20)+'Preco'.ljust(11)+'|'+'Quantidade'.ljust(9)+'|'+'Total'.ljust(11))
        print('-'*81)
    
    def show_order_details_footer(self):
        print('-'*81)
    
