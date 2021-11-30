from os import name
from model.model import Model
from view.view import View
from datetime import date

class Controller:
    """
    ***************************************************************
    * A controller for a store DB *
    ***************************************************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        self.main_menu()
    
    """
    ***************************************************************
    * General controllers *
    ***************************************************************
    """
    def main_menu(self):
        o = '0'
        while o != '5':
            self.view.main_menu()
            self.view.option('5')
            o = input()
            if o =='1':
                self.zips_menu()
            elif o == '2':
                self.products_menu()
            elif o == '3':
                self.clients_menu()
            elif o == '4':
                self.orders_menu()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v !=  '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals

    """
    ***************************************************************
    * Controllers for zips*
    ***************************************************************
    """

    def zips_menu(self):
        o = '0'
        while o != '7':
            self.view.zips_menu()
            self.view.option('7')
            o = input()
            if o =='1':
                self.create_zip()
            elif o == '2':
                self.read_a_zip()
            elif o == '3':
                self.read_all_zips()
            elif o == '4':
                self.read_zips_city()
            elif o == '5':
                self.update_zip()
            elif o == '6':
                self.delete_zip()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_zip(self):
        self.view.ask('Cidade: ')
        city = input()
        self.view.ask('Estado: ')
        state = input()
        return [city,state]
    
    def create_zip(self):
        self.view.ask('CP: ')
        i_zip = input()
        city, state = self.ask_zip()
        out = self.model.create_zip(i_zip, city, state)
        if out == True:
            self.view.ok(i_zip, 'adiciona')
        else:
            if out.errno == 1062:
                self.view.error('O CP ESTA REPETIDO')
            else:
                self.view.error('NAO SE PODE ADICIONAR O CP. VERIFICA.')
        return

    def read_a_zip(self):
        self.view.ask('CP: ')
        i_zip = input()
        zip = self.model.read_a_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_zip_header(' Dados do CP '+i_zip+' ')
            self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if zip == None:
                self.view.error(' O CP NAO EXISTE')
            else:
                self.view.error('PROBLEMA COM O CP. VERIFICA')
        return
    
    def read_all_zips(self):
        zips = self.model.read_all_zips()
        if type(zips) == list:
            self.view.show_zip_header(' Todos os CPs ')
            for zip in zips:
                self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            self.view.error('PROBLEA COM O CP. VERIFICA')
        return

    def read_zips_city(self):
        self.view.ask('Cidade: ')
        city = input()
        zips = self.model.read_zips_city(city)
        if type(zips) == list:
            self.view.show_zip_header(' CPs para a cidade de '+city+' ')
            for zip in zips:
                self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            self.view.error('PROBLEMA COM OS CPs. VERIFICA.')
        return
    
    def update_zip(self):
        self.view.ask('CP a modificar: ')
        i_zip = input()
        zip = self.model.read_a_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_zip_header(' Dados do CP '+i_zip+' ')
            self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if zip == None:
                self.view.error('O CP NAO EXISTE')
            else:
                self.view.error('PROBLEMA COM O CP. VERIFICA.')
            return
        self.view.msg('introduz os valores a modificar (vazio para deixar igual): ')
        whole_vals = self.ask_zip()
        fields, vals = self.update_lists(['z_city','z_state'], whole_vals)
        vals.append(i_zip)
        vals = tuple(vals)
        out = self.model.update_zip(fields, vals)
        if out == True:
            self.view.ok(i_zip, 'atualizado')
        else:
            self.view.error('NAO SE PODE ATUALIZAR O CP. VERIFICA.')
        return
    
    def delete_zip(self):
        self.view.ask('CP apagar: ')
        i_zip = input()
        count = self.model.delete_zip(i_zip)
        if count != 0:
            self.view.ok(i_zip, 'apago')
        else:
            if count == 0:
                self.view.error(' O CP NAO EXISTE')
            else:
                self.view.error('PROBLEMA AO APAGAR O CP. VERIFICA. ')
            return
    """
    ***************************************************************
    * Controllers for products*
    ***************************************************************
    """

    def products_menu(self):
        o = '0'
        while o != '8':
            self.view.products_menu()
            self.view.option('8')
            o = input()
            if o =='1':
                self.create_product()
            elif o == '2':
                self.read_a_product()
            elif o == '3':
                self.read_all_products()
            elif o == '4':
                self.read_products_brand()
            elif o == '5':
                self.read_products_price_range()
            elif o == '6':
                self.update_product()
            elif o == '7':
                self.delete_product()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_product(self):
        self.view.ask('Nome: ')
        name = input()
        self.view.ask('Marca: ')
        brand = input()
        self.view.ask('Descricao: ')
        descrip = input()
        self.view.ask('Preco: ')
        price = input()
        return [name,brand,descrip,price]
    
    def create_product(self):
        name, brand, descrip, price = self.ask_product()
        out = self.model.create_product(name, brand, descrip, price)
        if out == True:
            self.view.ok(name+' '+brand, 'adicionar')
        else:
            self.view.error('NAO SE PODE ADICIONAR O PRODUTO. VERIFICA.')
        return
    
    def read_a_product(self):
        self.view.ask('ID produto: ')
        id_product = input()
        product = self.model.read_a_product(id_product)
        if type(product) == tuple:
            self.view.show_product_header(' Dados do produto '+id_product+' ')
            self.view.show_a_product(product)
            self.view.show_product_midder()
            self.view.show_product_footer()
        else:
            if product == None:
                self.view.error('O PRODUTO NAO EXISTE')
            else:
                self.view.error('PROBLEMA NA VERIFICACAO DO PRODUTO. VERIFICA.')
            return
        
    def read_all_products(self):
        products = self.model.read_all_products()
        if type(products) == list:
            self.view.show_product_header(' Todos os produtos ')
            for product in products:
                self.view.show_a_product(product)
                self.view.show_product_midder()
            self.view.show_zip_footer()
        else:
            self.view.error('PROBLEMA AO VERIFICAR OS PRODUTOS. VERIFICA. ')
        return
    
    def read_products_brand(self):
        self.view.ask('Marca: ')
        brand = input()
        products = self.model.read_products_brand(brand)
        if type(products) == list:
            self.view.show_product_header(' Dados do produto '+brand+' ')
            for product in products:
                self.view.show_a_product(product)
                self.view.show_product_midder()
            self.view.show_product_footer()
        else:
            self.view.error('PROBLEMA NA VERIFICACAO DO PRODUTO. VERIFICA.')
        return
    
    def read_products_price_range(self):
        self.view.ask('preco inferior: ')
        price_ini = input()
        self.view.ask('preco suprior: ')
        price_end = input()
        products = self.model.read_products_price_range(float(price_ini), float(price_end))
        if type(products) == list:
            self.view.show_product_header(' Produtos entre '+price_ini+' y '+price_end+' ')
            for product in products:
                self.view.show_a_product(product)
                self.view.show_product_midder()
            self.view.show_product_footer()
        else:
            self.view.error('PROBLEMA AO VERIFICAR OS PRODUTOS. VERIFICA.')
        return
    
    def update_product(self):
        self.view.ask('ID de produto a modificar: ')
        id_product = input()
        product = self.model.read_a_product(id_product)
        if type(product) == tuple:
            self.view.show_product_header(' Dados do produto '+id_product+' ')
            self.view.show_a_product(product)
            self.view.show_product_midder()
            self.view.show_product_footer()
        else:
            if product == None:
                self.view.error('O PRODUTO NAO EXISTE')
            else:
                self.view.error('PROBLEMA AO VERIFICAR O PRODUTO. VERIFICA.')
            return
        self.view.msg('Introduz os valores a modificar (vazio para deixar igual):')
        whole_vals = self.ask_product()
        fields, vals = self.update_lists(['p_name','p_brand','p_descrip','p_price'], whole_vals)
        vals.append(id_product)
        vals = tuple(vals)
        out = self.model.update_product(fields, vals)
        if out == True:
            self.view.ok(id_product, 'atualizado')
        else:
            self.view.error('NAO SE PODE ATUALIZAR O PRODUTO. VERIFICA.')
        return
    
    def delete_product(self):
        self.view.ask('Id de produto a apagar: ')
        id_product = input()
        count = self.model.delelete_product(id_product)
        if count != 0:
            self.view.ok(id_product, 'apagado')
        else:
            self.view.error('PROBLEMA AO APAGAR O PRODUTO. VERIFICA.')
        return
    
    """
    ***************************************************************
    * Controllers for products*
    ***************************************************************
    """
    def clients_menu(self):
        o = '0'
        while o != '7':
            self.view.clients_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_client()
            elif o == '2':
                self.read_a_client()
            elif o == '3':
                self.read_all_clients()
            elif o == '4':
                self.read_clients_zip()
            elif o == '5':
                self.update_client()
            elif o == '6':
                self.delete_client()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_client(self):
        self.view.ask('Nome: ')
        name = input()
        self.view.ask('Apelido paterno: ')
        sname1 = input()
        self.view.ask('Apelido materno: ')
        sname2 = input()
        self.view.ask('Rua :')
        street = input()
        self.view.ask('no exterior: ')
        noext = input()
        self.view.ask('No interior: ')
        noint = input()
        self.view.ask('Colonia:' )
        col = input()
        self.view.ask('CP: ')
        zip = input()
        self.view.ask('Email: ')
        email = input()
        self.view.ask('Telefone: ')
        phone = input()
        return[name,sname1,sname2,street,noext,noint,col,zip,email,phone]
    
    def create_client(self):
        name, sname1, sname2, street, noext, noint, col, zip, email , phone = self.ask_client()
        out = self.model.create_client(name, sname1, sname2, street, noext, noint, col, zip, email , phone)
        if out == True:
            self.view.ok(name+' '+sname1+' '+sname2, 'adicionado')
        else:
            self.view.error('NAO SE PODE ADICIONAR AO CLIENTE. VERIFICA.')
        return
    
    def read_a_client(self):
        self.view.ask('ID cliente: ')
        id_client = input()
        client = self.model.read_a_client(id_client)
        if type(client) == True:
            self.view.show_client_header(' Dados do cliente '+id_client+' ')
            self.view.show_a_clients(client)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if client == None:
                self.view.error('O CLIENTE NAO EXISTE')
            else:
                self.view.error('PROBLEMA AO VERIFICAR O CLIENTE. VERIFICA.')
            return
    
    def read_all_clients(self):
        clients = self.model.read_all_clients()
        if type(clients) == list:
            self.view.show_client_header(' Todos os clientes ')
            for client in clients:
                self.view.show_a_client(client)
                self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            self.view.error('PROBLEMA AO VERIFICAR OS CLIENTES. VEERIFICA.')
        return
    
    def read_clients_zip(self):
        self.view.ask('CP: ')
        zip = input()
        clients = self.model.read_clients_zip(zip)
        if type(clients) == list:
            self.view.show_client_header(' Clients no CP '+zip+' ')
            for client in clients:
                self.view.show_a_client(client)
                self.view.show_client_midder()
            self.view.show_order_details_footer()
        else:
            self.view.error('PROBLEMA AO VERIFICAR OS CLIENTES. VERIFICA. ')
        return
    
    def update_client(self):
        self.view.ask('ID de cliente a modificar: ')
        id_client = input()
        client = self.model.read_a_client(id_client)
        if type(client) == tuple:
            self.view.show_client_header(' Dados do cliente '+id_client+' ')
            self.view.show_a_client(client)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if client == None:
                self.view.error('O CLIENTE NAO EXISTE')
            else:
                self.view.error('PROBLEMA AO VERIFICAR O CLIENTE. VERIFICA. ')
            return
        self.view.msg('Introduz os valores a modificar (vazio para deixar igual):')
        whole_vals = self.ask_client()
        fields, vals = self.update_lists(['c_fname','c_sname1','c_sname2','c_street','c_noext','c_noint','c_col','c_zip','c_email','c_phone',], whole_vals)
        vals.append(id_client)
        vals = tuple(vals)
        out = self.model.update_client(fields, vals)
        if out == True:
            self.view.ok(id_client, 'atualizo')
        else:
            self.view.error('NAO SE PODE ATUALIZAR O CLIENTE. VERIFICA.')
        return
    
    def delelete_client(self):
        self.view.ask('ID de cliente a apagar: ')
        id_client = input()
        count = self.model.delete_client(id_client)
        if count != 0:
            self.view.ok(id_client, 'apago')
        else:
            if count == 0:
                self.view.error('O CLIENTE NAO EXISTE')
            else:
                self.view.error('PROBLEMA AO APAGAR O CLIENTE. VERIFICA.')
        return
    
    """
    ***************************************************************
    * Controllers for orders*
    ***************************************************************
    """
    def orders_menu(self):
        o = '0'
        while o != '11':
            self.view.orders_menu()
            self.view.option('11')
            o = input()
            o = input()
            if o == '1':
                self.create_order()
            elif o == '2':
                self.read_a_order()
            elif o == '3':
                self.read_all_orders()
            elif o == '4':
                self.read_orders_date()
            elif o == '5':
                self.read_orders_client()
            elif o == '6':
                self.update_orders()
            elif o == '7':
                self.add_order_details()
            elif o == '8':
                self.update_order_details()
            elif o == '9':
                self.delete_order_details()
            elif o == '10':
                self.delete_order()
            elif o == '11':
                return
            else:
                self.view.not_valid_option()
        return
    
    def create_order(self):
        self.view.ask('ID cliente: ')
        id_client = input()
        o_status = 'processing'
        today = date.today()
        o_date = today.strftime('%y-%m-%d')
        o_total = 0.0
        id_order = self.model.create_order(id_client, o_status, o_date, o_total)
        if type(id_order) == int:
            id_product = ' '
            while id_product != ' ':
                self.view.msg('---- Adiciona os produtos a entrega (deixa em vazio o id do produto para sair) ---')
                id_product, od_total = self.create_order_details(id_order)
                o_total += od_total
            self.model.update_order(('o_total = %s',),(o_total, id_order))
        else:
            self.view.error('NAO SE PODE CRIAR A ENTREGA. VERIFICA.')
        return

    def read_a_order(self):
        self.view.ask('ID entrega: ')
        id_order = input()
        order = self.model.read_a_order(id_order)
        if type(order) == tuple:
            order_details = self.model.read_a_order_details(id_order)
            if type(order) == tuple:
                order_details = self.model.read_order_details(id_order)
                if type(order_details) != list and order_details != None:
                    self.view.error('PROBLEMA AO VERIFICAR A ENTREGA. VERIFICA. ')
                else:
                    self.view.show_order_details_header(' Dados da entrega '+id_order+' ')
                    self.view.show_order(order)
                    self.view.show_order_details_header()
                    for order_detail in order_details:
                        self.view.show_a_order_details(order_detail)
                    self.view.show_order_details_footer()
                    self.view.show_order_total(order)
                    self.view.show_order_footer()
                    return order
            else:
                if order == None:
                    self.view.error('A ENTREGA NAO EXISTE')
                else:
                    self.view.error('PROBLEMA AO VERIFICAR A ENTREGA. VERIFICA.')
    
    def read_all_orders(self):
        orders = self.model.read_all_orders()
        if type(orders) == list:
            self.view.show_order_header(' Todas as entregas ')
            for order in orders:
                id_order = order[0]
                order_details = self.model.read_a_order_details(id_order)
                if type(order_details) != list and order_details != None:
                    self.view.error('PROBLEMA AO VERIFICAR A ENTREGA '+id_order+'. VERIFICA.')
                else:
                    self.view.show_order(order)
                    self.view.show_order_details_header()
                    for order_detail in order_details:
                        self.view.show_a_order_details(order_detail)
                    self.view.show_order_details_footer()
                    self.view.show_order_total(order)
                    self.view.show_order_midder()
            self.view.show_order_footer()
        else:
            self.view.error('PROBLEMA AO VERIFICAR AS ENTREGAS. VERIFICA.')
        return
    
    def read_orders_date(self):
        self.view.ask('Ficha: ')
        date = input()
        orders = self.model.read_orders_date(date)
        if type(orders) == list:
            self.view.show_order_header(' Entregas para a ficha '+date+' ')
            for order in orders:
                id_order = order[0]
                order_details = self.model.read_a_order_details(id_order)
                if type(order_details) != list and order_details != None:
                    self.view.error('PROBLEMA AO VERIFICAR A ENTREGA '+id_order+'. VERIFICA.')
                else:
                    self.view.show_order(order)
                    self.view.show_order_details_header()
                    for order_detail in order_details:
                        self.view.show_a_order_details(order_detail)
                    self.view.show_order_details_footer()
                    self.view.show_order_total(order)
                    self.view.show_order_midder()
            self.view.show_order_footer()
        else:
            self.view.error('PROBLEMA AO VERIFICAR AS ENTREGAS. VERIFICA.')
        return
    
    def read_orders_client(self):
        self.view.ask('ID cliente: ')
        id_client = input()
        orders = self.model.read_orders_client(id_client)
        if type(orders) == list:
            self.view.show_order_header(' Entrega para o cliente '+id_client+' ')
            for order in orders:
                id_order = order[0]
                order_details = self.model.read_order_details(id_order)
                if type(order_details) != list and order_details != None:
                    self.view.error('PROBLEMA AO VERIFICAR A ENTREGA '+id_order+'. VERIFICA. ')
                else:
                    self.view.show_order(order)
                    self.view.show_order_details_header()
                    for order_detail in order_details:
                        self.view.show_a_order_details(order_detail)
                    self.view.show_order_details_footer()
                    self.view.show_order_total(order)
                    self.view.show_order_midder()
            self.view.show_order_footer()
        else:
            self.view.error('PROBLEMA AO VERIFICAR AS ENTREGAS. VERIFICA.')
        return
    
    def update_order(self):
        self.view.ask('ID da entrega a modificar: ')
        id_order = input()
        order = self.model.read_a_order(id_order)
        if type(order) == type:
            self.view.show_order_header(' Dados da entrega '+id_order+' ')
            self.view.show_order(order)
            self.view.show_order_total(order)
            self.view.show_order_footer()
        else:
            if order == None:
                self.view.error('A ENTREGA NAO EXISTE')
            else:
                self.view.error('PROBLEMA AO VERIFICAR A ENTREGA. VERIFICA. ')
            return
        self.view.msg('Introduz os valores a modificar (vazio para deixar igual) :')
        self.view.ask('ID Cliente: ')
        id_client = input()
        self.view.ask('Estado (processing, acepted, sent, received): ')
        o_status = input()
        self.view.ask('Estado (Ficha (yyyy/mm/dd): ')
        o_date = input()
        whole_vals  = [id_client, o_status, o_date]
        fields, vals = self.update_lists(['id_client','o_status','o_date'], whole_vals)
        vals.append(id_order)
        vals = tuple(vals)
        out = self.model.update_order(fields, vals)
        if out == True:
            self.view.ok(id_order, 'atualizado')
        else:
            self.view.error('NAO SE PODE ATUALIZAR A ENTREGA. VERIFICA.')
        return
    
    def delete_order(self):
        self.view.ask('Id da entrega a apagar: ')
        id_order = input()
        count = self.model.delelete_order(id_order)
        if count != 0:
            self.view.ok(id_order, 'apagado')
        else:
            if count == 0:
                self.view.error('A ENTREGA NAO EXISTE')
            else:
                self.view.error('PROBLEMA AO APAGAR A ENTREGA. VERIFICA.')
        return
    

    """
    ***************************************************************
    * Controllers for orders details*
    ***************************************************************
    """
    def create_order_details(self, id_order):
        od_total = 0.0
        self.view.ask('ID produto: ')
        id_product = input()
        if id_product != '':
            product = self.model.read_a_product(id_product)
            if type(product) == tuple:
                self.view.show_product_header(' Dados do produto '+id_product+' ')
                self.view.show_a_product(product)
                self.view.show_product_footer()
                self.view.ask('Quantidade: ')
                od_amount = int(input())
                od_total = od_amount*product[4]
                out = self.model.create_order_detail(id_order, id_product, od_amount, od_total)
                if out == True:
                    self.view.ok(product[1]+' '+product[2], 'detalhe da entrega')
                else:
                    if out.errno == 1062:
                        self.view.error('O PRODUTO JA ESTA NA ENTREGA')
                    else:
                        self.view.error('nao se pode juntar ao produto. verifica. ')
                    od_total == 0.0
            else:
                if product == None:
                    self.view.error('O PRODUTO NAO EXISTE')
                else:
                    self.view.error('PROBLEMA AO VERIFICAR O PRODUTO. VERIFICA.')
            return id_product, od_total
    
    def add_order_details(self):
        order = self.read_a_order()
        if type(order) == tuple:
            id_order = order[0]
            o_total = order[4]
            id_product =' '
            while id_product != '':
                self.view.msg('---- Adiciona produtos ao pedido (deixa em vazio id do produto para sair) ---')
                id_product, od_total = self.create_order_details(id_order)
                o_total += od_total
            self.model.update_order(('o_total = %s'),(o_total, id_order))
        return
    
    def update_order_details(self):
        order = self.read_a_order()
        if type(order) == tuple:
            id_order = order[0]
            o_total = order[4]
            id_product = ' '
            while id_product != '':
                self.view.msg('---- Modifica produtos do pedido (deixa em vazio o id do produto para sair9 ----')
                self.view.ask('ID produto: ')
                id_product = input()
                if id_product != '':
                    order_detail = self.model.read_a_order_detail(id_order, id_product)
                    if type(order_detail) == tuple:
                        od_total_old = order_detail[5]
                        o_total -= od_total_old
                        product = self.model.read_a_product(id_product)
                        price = product[4]
                        self.view.ask('Quantidade: ')
                        od_amount = int(input())
                        od_total = price*od_amount
                        o_total += od_total
                        fields, whole_vals = self.update_lists(['od_amount','od_total'],[od_amount,od_total])
                        whole_vals.append(id_order)
                        whole_vals.append(id_product)
                        self.model.update_order_details(fields, whole_vals)
                        self.view.ok(id_product, 'atualizacao do pedido ')
                    else:
                        if order_detail == None:
                            self.view.error('O PRODUTO NAO EXISTE NO PEDIDO')
                        else:
                            self.view.error('PROBLEMA AO ATUALIZAR O PRODUTO. VERIFICA.')
                self.model.update_order(('o_total = %s',),(o_total, id_order))
            return
    
    def delete_order_details(self):
        order = self.read_a_order()
        if type(order) == tuple:
            id_order = order[0]
            o_total = order[4]
            id_product = ' '
            while id_product != '':
                self.view.msg('---- Apaga produtos do pedido (deixa em vazio o id do produto para sair)---')
                self.view.ask('ID produto: ')
                id_product = input()
                if id_product != '':
                    order_detail = self.model.read_a_order_detail(id_order, id_product)
                    count = self.model.delete_order_detail(id_order, id_product)
                    if type(order_detail) == tuple and count != 0:
                        od_total = order_detail[5]
                        o_total -= od_total
                        self.view.error('O PRODUTO NAO EXISTE NA COMPRA')
                    else:
                        if order_detail == None:
                            self.view.ok(id_product, 'eliminação da compra')
                        else:
                            self.view.error('PROBLEMA AO ELIMINAR O PRODUTO. VERIFICA.')
            self.model.update_order(('o_total = %s',),(o_total, id_order))
        return
    


