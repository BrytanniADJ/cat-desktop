import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QErrorMessage
from PyQt5.QtCore import QTimer
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import threading
from PyQt5 import QtWidgets, QtCore 

from fpdf import FPDF
import os
from PyQt5 import QtWidgets

# from reportlab.pdfgen import canvas
# from pdfrw import PdfArray,pdfwriter,PageMerge

app = QtWidgets.QApplication([])

# Importar Banco de Dados
banco =  mysql.connector.connect(
    host='localhost',
    user='root',
    port='3308',
    password='Senac',
    database='CAT_TREINEE'
)
    
#entrar na tela de cadastro inicial
def chamar_cad_inicial():
    cad_inicial.show()
    login.close()

#cadastro inicial
def cad_func_inicial():
    # Capturar dados dos campos de entrada
    cod_funcionario = cad_inicial.campo_cod_funci.text()
    cod_empresa = cad_inicial.campo_cod_empre_2.text()
    nome_func = cad_inicial.campo_nome_func.text()
    nome_mae_func = cad_inicial.campo_nome_mae.text()
    data_nascimento_func = cad_inicial.campo_data_nascimento.text()
    identidade_func = cad_inicial.campo_identidade.text()
    cpf_func = cad_inicial.campo_cpf.text()
    ra_func = cad_inicial.campo_ra.text()
    estado_civil = cad_inicial.selec_estado_civil.currentText()
    sexo = cad_inicial.selec_sexo.currentText()
    cep_func = cad_inicial.campo_cep.text()[:10]  # Truncar para 10 caracteres
    bairro_func = cad_inicial.campo_bairro.text()
    municipio_func = cad_inicial.campo_municipio.text()
    estado_func = cad_inicial.selec_estado.currentText()
    endereco_func = cad_inicial.campo_endereco.text()
    telefone_func = cad_inicial.campo_telefone.text()
    email_func = cad_inicial.campo_email.text()
    area_func = cad_inicial.campo_area.text()
    grau_instrucao_func = cad_inicial.selec_grau.currentText()
    ctps_func = cad_inicial.campo_ctps.text()
    cbo_func = cad_inicial.campo_cbo.text()
    remuneracao_func = cad_inicial.campo_remuneracao.text()
    pis_pasep_nit_func = cad_inicial.campo_pis.text()
    aposentadoria_func = cad_inicial.select_apo.currentText()  # Truncar para 50 caracteres
    
    try:
        # Verifica se o formato está correto (ano/mês/dia)
        data_nascimento_validada = datetime.strptime(data_nascimento_func, '%Y/%m/%d')
    except ValueError:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! A data de nascimento deve estar preenchida ou no formato ano/mês/dia (AAAA/MM/DD).")
        erro.exec_()
        return

    cursor = banco.cursor()

    cadastro = """
    INSERT INTO funcionario (
        cod_funcionario, cod_empresa, nome_func, nome_mae_func, data_nascimento_func, sexo, estado_civil,
        remuneracao_func, ctps_func, identidade_func, pis_pasep_nit_func, cep_func, endereco_func, bairro_func,
        estado_func, municipio_func, telefone_func, area_func, cbo_func, aposentadoria_func, cpf_func, ra_func,
        grau_instrucao_func, email_func
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        cod_funcionario, cod_empresa, nome_func, nome_mae_func, data_nascimento_func, sexo, estado_civil,
        remuneracao_func, ctps_func, identidade_func, pis_pasep_nit_func, cep_func, endereco_func, bairro_func,
        estado_func, municipio_func, telefone_func, area_func, cbo_func, aposentadoria_func, cpf_func, ra_func,
        grau_instrucao_func, email_func
    )

    try:
        cursor.execute(cadastro, valores)
        banco.commit()
        cursor.close()

        # Limpar todos os campos após o cadastro bem-sucedido
        cad_inicial.campo_cod_funci.clear()
        cad_inicial.campo_cod_empre_2.clear()
        cad_inicial.campo_nome_func.clear()
        cad_inicial.campo_nome_mae.clear()
        cad_inicial.campo_data_nascimento.clear()
        cad_inicial.campo_remuneracao.clear()
        cad_inicial.campo_ctps.clear()
        cad_inicial.campo_identidade.clear()
        cad_inicial.campo_cpf.clear()
        cad_inicial.campo_ra.clear()
        cad_inicial.campo_cep.clear()
        cad_inicial.campo_bairro.clear()
        cad_inicial.campo_pis.clear()
        cad_inicial.campo_municipio.clear()
        cad_inicial.campo_endereco.clear()
        cad_inicial.campo_cbo.clear()
        cad_inicial.campo_area.clear()
        cad_inicial.campo_telefone.clear()
        cad_inicial.campo_email.clear()
        cad_inicial.select_apo.setCurrentIndex(0)
        cad_inicial.selec_grau.setCurrentIndex(0)
        cad_inicial.selec_sexo.setCurrentIndex(0)
        cad_inicial.selec_estado_civil.setCurrentIndex(0)
        cad_inicial.selec_estado.setCurrentIndex(0)

    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código não cadastrado ou campo nulo.")
        erro.exec_()


#sair tela de cadastro inicial
def sair_cad_inicial():
    login.show()
    cad_inicial.close()

#inicial
def chamar_inicial():
    usuario = login.usuario.text()
    senha = login.senha.text()

    cursor = banco.cursor()
    consultar = f"SELECT ra_func, cpf_func FROM funcionario WHERE ra_func = '{usuario}' AND cpf_func = '{senha}'"
    cursor.execute(consultar)

    if cursor.fetchone() is not None:
        inicial.show()
        login.close()
    else:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Usuário ou Senha Inválidos")
        erro.exec_()
    cursor.close()


#entrar e sair na tela de cadastro
def chamar_cadastros():
    cadastros.show()
    inicial.close()

def sair_cadastros():
    inicial.show()
    cadastros.close()

#Funcionario
#cadastrar funcionario
def func_cadastros():
    cod_funcionario = cadastros.campo_cod_funci.text()
    cod_empresa = cadastros.campo_cod_empre_2.text()
    nome_func = cadastros.campo_nome_func.text()
    nome_mae_func = cadastros.campo_nome_mae.text()
    data_nascimento_func = cadastros.campo_data_nascimento.text()
    identidade_func = cadastros.campo_identidade.text()
    cpf_func = cadastros.campo_cpf.text()
    ra_func = cadastros.campo_ra.text()
    estado_civil = cadastros.selec_estado_civil.currentText()
    sexo = cadastros.selec_sexo.currentText()
    cep_func = cadastros.campo_cep.text()[:10]# Truncar para 10 caracteres
    bairro_func = cadastros.campo_bairro.text()
    municipio_func = cadastros.campo_municipio.text()
    estado_func = cadastros.selec_estado.currentText()
    endereco_func = cadastros.campo_endereco.text()
    telefone_func = cadastros.campo_telefone.text()
    email_func = cadastros.campo_email.text()
    area_func = cadastros.campo_area.text()
    grau_instrucao_func = cadastros.selec_grau.currentText()
    ctps_func = cadastros.campo_ctps.text()
    cbo_func = cadastros.campo_cbo.text()
    remuneracao_func = cadastros.campo_remuneracao.text()
    pis_pasep_nit_func = cadastros.campo_pis.text()
    aposentadoria_func = cadastros.select_apo.currentText()

    # Validação de data
    try:
        # Verifica se o formato está correto (ano/mês/dia)
        data_nascimento_validada = datetime.strptime(data_nascimento_func, '%Y/%m/%d')
    except ValueError:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! A data de nascimento deve estar preenchida ou no formato ano/mês/dia (AAAA/MM/DD).")
        erro.exec_()
        return
   
    cursor = banco.cursor()

    cadastro = """
    INSERT INTO funcionario (
        cod_funcionario, cod_empresa, nome_func, nome_mae_func, data_nascimento_func, sexo, estado_civil,
        remuneracao_func, ctps_func, identidade_func, pis_pasep_nit_func, cep_func, endereco_func, bairro_func,
        estado_func, municipio_func, telefone_func, area_func, cbo_func, aposentadoria_func, cpf_func, ra_func,
        grau_instrucao_func, email_func
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        cod_funcionario, cod_empresa, nome_func, nome_mae_func, data_nascimento_func, sexo, estado_civil,
        remuneracao_func, ctps_func, identidade_func, pis_pasep_nit_func, cep_func, endereco_func, bairro_func,
        estado_func, municipio_func, telefone_func, area_func, cbo_func, aposentadoria_func, cpf_func, ra_func,
        grau_instrucao_func, email_func
    )

    try:
        cursor.execute(cadastro, valores)
        banco.commit()
        cursor.close()

        cadastros.campo_cod_funci.clear()
        cadastros.campo_cod_empre_2.clear()
        cadastros.campo_nome_func.clear()
        cadastros.campo_nome_mae.clear()
        cadastros.campo_data_nascimento.clear()
        cadastros.campo_remuneracao.clear()
        cadastros.campo_ctps.clear()
        cadastros.campo_identidade.clear()
        cadastros.campo_cpf.clear()
        cadastros.campo_ra.clear()
        cadastros.campo_cep.clear()
        cadastros.campo_bairro.clear()
        cadastros.campo_pis.clear()
        cadastros.campo_municipio.clear()
        cadastros.campo_endereco.clear()
        cadastros.campo_cbo.clear()
        cadastros.campo_area.clear()
        cadastros.campo_telefone.clear()
        cadastros.campo_email.clear()
        cadastros.select_apo.setCurrentIndex(0)
        cadastros.selec_grau.setCurrentIndex(0)
        cadastros.selec_sexo.setCurrentIndex(0)
        cadastros.selec_estado_civil.setCurrentIndex(0)
        cadastros.selec_estado.setCurrentIndex(0)

    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código RA ou CPF já cadastrado ou campo nulo.")
        erro.exec_()

#limpar dados da tela
def limpar_func():
    #limpar dados da tela
    
    cadastros.campo_cod_funci.setText('')
    cadastros.campo_cod_empre_2.setText('')
    cadastros.campo_nome_func.setText('')
    cadastros.campo_nome_mae.setText('')
    cadastros.campo_data_nascimento.setText('')
    cadastros.campo_remuneracao.setText('')
    cadastros.campo_ctps.setText('')
    cadastros.campo_identidade.setText('')
    cadastros.campo_cpf.setText('')
    cadastros.campo_ra.setText('')
    cadastros.campo_cep.setText('')
    cadastros.campo_bairro.setText('')
    cadastros.campo_pis.setText('')
    cadastros.campo_municipio.setText('')
    cadastros.campo_endereco.setText('')
    cadastros.campo_cbo.setText('')
    cadastros.campo_area.setText('')
    cadastros.campo_telefone.setText('')
    cadastros.campo_email.setText('')
    cadastros.select_apo.setCurrentIndex(0)
    cadastros.selec_grau.setCurrentIndex(0)
    cadastros.selec_sexo.setCurrentIndex(0)
    cadastros.selec_estado_civil.setCurrentIndex(0)
    cadastros.selec_estado.setCurrentIndex(0)       

#consultar funcionario
def culsutar_func():
    cod_funcionario = cadastros.campo_cod_funci.text()

    cursor = banco.cursor()
    consulta = f"SELECT * FROM funcionario WHERE cod_funcionario = '{cod_funcionario}'"
    cursor.execute(consulta)

    try:
        busca = cursor.fetchall()
        cursor.close()

        cadastros.campo_endereco.setText(str(busca[0][12]))  # endereco_func --
        cadastros.campo_nome_func.setText(str(busca[0][2]))  # nome_func --
        cadastros.campo_nome_mae.setText(str(busca[0][3]))  # nome_func --
        cadastros.campo_data_nascimento.setText(str(busca[0][4]))  # data_nascimento_func --
        cadastros.selec_sexo.setCurrentText(str(busca[0][5]))  # sexo --
        cadastros.selec_estado_civil.setCurrentText(str(busca[0][6]))  # estado_civil --
        cadastros.campo_remuneracao.setText(str(busca[0][7]))  # remuneracao_func --
        cadastros.campo_ctps.setText(str(busca[0][8]))  # ctps_func --
        cadastros.campo_identidade.setText(str(busca[0][9])) # identidade_func --
        cadastros.campo_pis.setText(str(busca[0][10]))  # pis_pasep_nit_func --
        cadastros.campo_cep.setText(str(busca[0][11]))  # cep_func --
        cadastros.campo_cod_empre_2.setText(str(busca[0][1]))  # endereco_func ---
        cadastros.campo_bairro.setText(str(busca[0][13]))  # bairro_func --
        cadastros.selec_estado.setCurrentText(str(busca[0][14]))  # estado_func --
        cadastros.campo_municipio.setText(str(busca[0][15]))  # municipio_func --
        cadastros.campo_telefone.setText(str(busca[0][16]))  # telefone_func --
        cadastros.campo_area.setText(str(busca[0][19]))  # area_func --
        cadastros.campo_cbo.setText(str(busca[0][17]))  # cbo_func --
        cadastros.select_apo.setCurrentText(str(busca[0][18]))  # aposentadoria_func --
        cadastros.campo_cpf.setText(str(busca[0][21]))  # cpf_func --
        cadastros.campo_ra.setText(str(busca[0][20]))  # ra_func --
        cadastros.selec_grau.setCurrentText(str(busca[0][23]))  # grau_instrucao_func --
        cadastros.campo_email.setText(str(busca[0][22]))  # email_func -- 

    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código não cadastrado ou campo nulo.")
        erro.exec_()

#remover funcionario
def remover_funcionario():
    cod_funcionario = cadastros.campo_cod_funci.text()

    cursor = banco.cursor()
    remover = f"DELETE FROM funcionario WHERE cod_funcionario = '{cod_funcionario}'"

    try:
        cursor.execute(remover)
        banco.commit()
        cursor.close()

        cadastros.campo_cod_funci.clear()
        cadastros.campo_cod_empre_2.clear()
        cadastros.campo_nome_func.clear()
        cadastros.campo_nome_mae.clear()
        cadastros.campo_data_nascimento.clear()
        cadastros.campo_remuneracao.clear()
        cadastros.campo_ctps.clear()
        cadastros.campo_identidade.clear()
        cadastros.campo_cpf.clear()
        cadastros.campo_ra.clear()
        cadastros.campo_cep.clear()
        cadastros.campo_bairro.clear()
        cadastros.campo_pis.clear()
        cadastros.campo_municipio.clear()
        cadastros.campo_endereco.clear()
        cadastros.campo_cbo.clear()
        cadastros.campo_area.clear()
        cadastros.campo_telefone.clear()
        cadastros.campo_email.clear()
        cadastros.select_apo.setCurrentIndex(0)
        cadastros.selec_grau.setCurrentIndex(0)
        cadastros.selec_sexo.setCurrentIndex(0)
        cadastros.selec_estado_civil.setCurrentIndex(0)
        cadastros.selec_estado.setCurrentIndex(0)
    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro!")
        erro.exec_()

#atualizar funcionario
def atualizar_func():
    # Carregar campos de funcionario
    cod_funcionario = cadastros.campo_cod_funci.text()
    cod_empresa = cadastros.campo_cod_empre_2.text()
    nome_func = cadastros.campo_nome_func.text()
    nome_mae_func = cadastros.campo_nome_mae.text()
    data_nascimento_func = cadastros.campo_data_nascimento.text()
    sexo_func = cadastros.selec_sexo.currentText()
    grau_instrucao_func = cadastros.selec_grau.currentText()
    estado_civil = cadastros.selec_estado_civil.currentText()
    remuneracao_func = cadastros.campo_remuneracao.text()
    ctps_func = cadastros.campo_ctps.text()
    identidade_func = cadastros.campo_identidade.text()
    cpf_func = cadastros.campo_cpf.text()
    ra_func = cadastros.campo_ra.text()
    cep_func = cadastros.campo_cep.text()[:10]  # Truncar para 10 caracteres
    bairro_func = cadastros.campo_bairro.text()
    pis_pasep_nit_func = cadastros.campo_pis.text()
    municipio_func = cadastros.campo_municipio.text()
    endereco_func = cadastros.campo_endereco.text()
    cbo_func = cadastros.campo_cbo.text()
    estado_func = cadastros.selec_estado.currentText()
    area_func = cadastros.campo_area.text()
    telefone_func = cadastros.campo_telefone.text()
    email_func = cadastros.campo_email.text()
    aposentadoria_func = cadastros.select_apo.currentText()[:50]

    # Validação de data
    try:
        # Verifica se o formato está correto (ano/mês/dia)
        data_nascimento_validada = datetime.strptime(data_nascimento_func, '%Y/%m/%d')
    except ValueError:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! A data de nascimento deve estar preenchida ou no formato ano/mês/dia (AAAA/MM/DD).")
        erro.exec_()
        return

    atualizar = """
    UPDATE funcionario SET
        cod_empresa=%s, nome_func=%s, nome_mae_func=%s, data_nascimento_func=%s, sexo=%s, estado_civil=%s,
        remuneracao_func=%s, ctps_func=%s, identidade_func=%s, pis_pasep_nit_func=%s, cep_func=%s, endereco_func=%s,
        bairro_func=%s, estado_func=%s, municipio_func=%s, telefone_func=%s, area_func=%s, cbo_func=%s,
        aposentadoria_func=%s, cpf_func=%s, ra_func=%s, grau_instrucao_func=%s, email_func=%s
    WHERE cod_funcionario=%s
    """
    valores = (
        cod_empresa, nome_func, nome_mae_func, data_nascimento_func, sexo_func, estado_civil,
        remuneracao_func, ctps_func, identidade_func, pis_pasep_nit_func, cep_func, endereco_func,
        bairro_func, estado_func, municipio_func, telefone_func, area_func, cbo_func,
        aposentadoria_func, cpf_func, ra_func, grau_instrucao_func, email_func, cod_funcionario
    )

    cursor = banco.cursor()
    try:
        cursor.execute(atualizar, valores)
        banco.commit()
        cursor.close()

        cadastros.campo_cod_funci.clear()
        cadastros.campo_cod_empre_2.clear()
        cadastros.campo_nome_func.clear()
        cadastros.campo_nome_mae.clear()
        cadastros.campo_data_nascimento.clear()
        cadastros.campo_remuneracao.clear()
        cadastros.campo_ctps.clear()
        cadastros.campo_identidade.clear()
        cadastros.campo_cpf.clear()
        cadastros.campo_ra.clear()
        cadastros.campo_cep.clear()
        cadastros.campo_bairro.clear()
        cadastros.campo_pis.clear()
        cadastros.campo_municipio.clear()
        cadastros.campo_endereco.clear()
        cadastros.campo_cbo.clear()
        cadastros.campo_area.clear()
        cadastros.campo_telefone.clear()
        cadastros.campo_email.clear()
        cadastros.select_apo.setCurrentIndex(0)

            # Limpar campos de seleção
        cadastros.selec_grau.setCurrentIndex(0)
        cadastros.selec_sexo.setCurrentIndex(0)
        cadastros.selec_estado_civil.setCurrentIndex(0)
        cadastros.selec_estado.setCurrentIndex(0)
    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro!")
        erro.exec_()


#Medico
#cadastrar medico
def cad_medico():
    cod = cadastros.campo_cod_medico.text()
    nome = cadastros.campo_nome_medico.text()
    cpf = cadastros.campo_cpf_medico.text()
    email = cadastros.campo_email_medico.text()
    espec = cadastros.campo_especialidade.text()
    crm = cadastros.campo_crm.text()

    cursor = banco.cursor()
    cadastro = "INSERT INTO medico(cod_medico, nome_medico, cpf_medico, email_medico, especialidade_medico, crm_medico) VALUES(%s, %s, %s, %s, %s, %s)"
    campos = (cod, nome, cpf, email, espec, crm)

    try:
        cursor.execute(cadastro, campos)
        banco.commit()
        cursor.close()

        cadastros.campo_cod_medico.clear()
        cadastros.campo_nome_medico.clear()
        cadastros.campo_cpf_medico.clear()
        cadastros.campo_email_medico.clear()
        cadastros.campo_especialidade.clear()
        cadastros.campo_crm.clear()
    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código ou CRM já cadastrado ou campo nulo.")
        erro.exec_()

#atualizar medico
def atualizar_medico(): 
    cod = cadastros.campo_cod_medico.text()
    nome = cadastros.campo_nome_medico.text()
    cpf = cadastros.campo_cpf_medico.text()
    email = cadastros.campo_email_medico.text()
    espec = cadastros.campo_especialidade.text()
    crm = cadastros.campo_crm.text()

    cursor = banco.cursor()

    atualizar = f"UPDATE medico SET nome_medico = '{nome}', cpf_medico = '{cpf}', email_medico = '{email}', especialidade_medico = '{espec}', crm_medico = '{crm}' WHERE cod_medico = '{cod}'"

    try:
        cursor.execute(atualizar)

        banco.commit()
            
        cursor.close()

        cod = cadastros.campo_cod_medico.setText('')
        nome = cadastros.campo_nome_medico.setText('')
        cpf = cadastros.campo_cpf_medico.setText('')
        email = cadastros.campo_email_medico.setText('')
        espec = cadastros.campo_especialidade.setText('')
        crm = cadastros.campo_crm.setText('')
    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro!")
        erro.exec_()

#remover medico
def excluir_medico(): 
    cod = cadastros.campo_cod_medico.text()

    cursor = banco.cursor()

    excluir = f"DELETE FROM medico WHERE cod_medico = '{cod}'"

    try:
        cursor.execute(excluir)

        banco.commit()
            
        cursor.close()
        cod = cadastros.campo_cod_medico.setText('')
        nome = cadastros.campo_nome_medico.setText('')
        cpf = cadastros.campo_cpf_medico.setText('')
        email = cadastros.campo_email_medico.setText('')
        espec = cadastros.campo_especialidade.setText('')
        crm = cadastros.campo_crm.setText('')
    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro!")
        erro.exec_()

#consultar medico
def consulta_medico(): #codigo de consulta
    cod = cadastros.campo_cod_medico.text()

    cursor = banco.cursor()

    consulta = f"SELECT * FROM medico WHERE cod_medico = '{cod}'"

    try:
        cursor.execute(consulta)

        selecao = cursor.fetchall()
            
        cursor.close()

        nome = cadastros.campo_nome_medico.setText(str(selecao[0][1]))
        cpf = cadastros.campo_cpf_medico.setText(str(selecao[0][2]))
        email = cadastros.campo_email_medico.setText(str(selecao[0][3]))
        espec = cadastros.campo_especialidade.setText(str(selecao[0][4]))
        crm = cadastros.campo_crm.setText(str(selecao[0][5]))

    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código não cadastrado ou campo nulo.")
        erro.exec_()

#limpar dados da tela
def limpar_tela_med(): #codigo de limpeza dos campos
    cod = cadastros.campo_cod_medico.setText('')
    nome = cadastros.campo_nome_medico.setText('')
    cpf = cadastros.campo_cpf_medico.setText('')
    email = cadastros.campo_email_medico.setText('')
    espec = cadastros.campo_especialidade.setText('')
    crm = cadastros.campo_crm.setText('')


#Empresa
#cadastrar empresa
def cad_empresa():
    cod = cadastros.campo_cod_empre.text()
    nome = cadastros.campo_nome_empre.text()
    tipo = cadastros.campo_tipo_doc.text()
    cnpj = cadastros.campo_cnpj_empre.text()
    cnae = cadastros.campo_cnae.text()
    cep = cadastros.campo_cep_empre.text()
    ende = cadastros.campo_endereco_empre.text()
    bairro = cadastros.campo_bairro_empre.text()
    muni = cadastros.campo_municipio_empre.text()
    estado = cadastros.selec_estado_empre.currentText()
    tele = cadastros.campo_telefone_empre.text()
    email = cadastros.campo_email_empre.text()

    cursor = banco.cursor()
    cadastro = "INSERT INTO empresa (cod_empresa, nome_empresa, tipo_num_doc_empresa, cnpj_empresa, cnae_empresa, cep_empresa, endereco_empresa, bairro_empresa, municipio_empresa, estado_empresa, telefone_empresa, email_empresa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    campos = (cod, nome, tipo, cnpj, cnae, cep, ende, bairro, muni, estado, tele, email)

    try:
        cursor.execute(cadastro, campos)
        banco.commit()
        cursor.close()
        cadastros.campo_cod_empre.clear()
        cadastros.campo_nome_empre.clear()
        cadastros.campo_tipo_doc.clear()
        cadastros.campo_cnpj_empre.clear()
        cadastros.campo_cnae.clear()
        cadastros.campo_cep_empre.clear()
        cadastros.campo_endereco_empre.clear()
        cadastros.campo_bairro_empre.clear()
        cadastros.campo_municipio_empre.clear()
        cadastros.campo_telefone_empre.clear()
        cadastros.campo_email_empre.clear()
        cadastros.selec_estado_empre.setCurrentIndex(0) 
    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código ou CNPJ já cadastrado ou campo nulo.")
        erro.exec_()

#remover empresa  
def excluir_empresa():
    cod = cadastros.campo_cod_empre.text()

    cursor = banco.cursor()

    excluir = f"DELETE FROM empresa WHERE cod_empresa = '{cod}'"

    try:
        cursor.execute(excluir)

        banco.commit()
            
        cursor.close()
        cod = cadastros.campo_cod_empre.clear()
        nome = cadastros.campo_nome_empre.clear()
        tipo = cadastros.campo_tipo_doc.clear()
        cnpj = cadastros.campo_cnpj_empre.clear()
        cnae = cadastros.campo_cnae.clear()
        cep = cadastros.campo_cep_empre.clear()
        ende = cadastros.campo_endereco_empre.clear()
        bairro = cadastros.campo_bairro_empre.clear()
        muni = cadastros.campo_municipio_empre.clear()
        tele = cadastros.campo_telefone_empre.clear()
        email = cadastros.campo_email_empre.clear()
        cadastros.selec_estado_empre.setCurrentIndex(0)
    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro!")
        erro.exec_()

#atualizar empresa
def atualizar_empresa():
    cod = cadastros.campo_cod_empre.text()
    nome = cadastros.campo_nome_empre.text()
    tipo = cadastros.campo_tipo_doc.text()
    cnpj = cadastros.campo_cnpj_empre.text()
    cnae = cadastros.campo_cnae.text()
    cep = cadastros.campo_cep_empre.text()
    ende = cadastros.campo_endereco_empre.text()
    bairro = cadastros.campo_bairro_empre.text()
    muni = cadastros.campo_municipio_empre.text()
    estado = cadastros.selec_estado_empre.currentText()
    tele = cadastros.campo_telefone_empre.text()
    email = cadastros.campo_email_empre.text()

    cursor = banco.cursor()

    atualizar = f"update empresa set nome_empresa = '{nome}', tipo_num_doc_empresa = '{tipo}', cnae_empresa = '{cnae}', cep_empresa = '{cep}', bairro_empresa = '{bairro}', estado_empresa = '{estado}', municipio_empresa = '{muni}', endereco_empresa = '{ende}', cnpj_empresa = '{cnpj}', telefone_empresa = '{tele}', email_empresa = '{email}' where cod_empresa = '{cod}'"

    try:
        cursor.execute(atualizar)

        banco.commit()
                    
        cursor.close()

        cod = cadastros.campo_cod_empre.clear()
        nome = cadastros.campo_nome_empre.clear()
        tipo = cadastros.campo_tipo_doc.clear()
        cnpj = cadastros.campo_cnpj_empre.clear()
        cnae = cadastros.campo_cnae.clear()
        cep = cadastros.campo_cep_empre.clear()
        ende = cadastros.campo_endereco_empre.clear()
        bairro = cadastros.campo_bairro_empre.clear()
        muni = cadastros.campo_municipio_empre.clear()
        tele = cadastros.campo_telefone_empre.clear()
        email = cadastros.campo_email_empre.clear()
        cadastros.selec_estado_empre.setCurrentIndex(0)
    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro!")
        erro.exec_()

#consultar empresa
def consulta_empresa():
    cod = cadastros.campo_cod_empre.text()

    cursor = banco.cursor()

    consulta = f"SELECT * FROM empresa WHERE cod_empresa = '{cod}'"

   
    cursor.execute(consulta)

    selecao = cursor.fetchall()
            
    cursor.close()

    try:
        nome = cadastros.campo_nome_empre.setText(str(selecao[0][1]))
        tipo = cadastros.campo_tipo_doc.setText(str(selecao[0][2]))
        cnpj = cadastros.campo_cnpj_empre.setText(str(selecao[0][3]))
        cnae = cadastros.campo_cnae.setText(str(selecao[0][4]))
        cep = cadastros.campo_cep_empre.setText(str(selecao[0][5]))
        ende = cadastros.campo_endereco_empre.setText(str(selecao[0][6]))
        bairro = cadastros.campo_bairro_empre.setText(str(selecao[0][7]))
        muni = cadastros.campo_municipio_empre.setText(str(selecao[0][8]))
        estado = cadastros.selec_estado_empre.setCurrentText(str(selecao[0][9]))
        tele = cadastros.campo_telefone_empre.setText(str(selecao[0][10]))
        email = cadastros.campo_email_empre.setText(str(selecao[0][11]))

    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código não cadastrado ou campo nulo.")
        erro.exec_()

#limpar dados da tela
def limpar_tela_empre():
    cod = cadastros.campo_cod_empre.setText('')
    nome = cadastros.campo_nome_empre.setText('')
    tipo = cadastros.campo_tipo_doc.setText('')
    cnpj = cadastros.campo_cnpj_empre.setText('')
    cnae = cadastros.campo_cnae.setText('')
    cep = cadastros.campo_cep_empre.setText('')
    ende = cadastros.campo_endereco_empre.setText('')
    bairro = cadastros.campo_bairro_empre.setText('')
    muni = cadastros.campo_municipio_empre.setText('')
    tele = cadastros.campo_telefone_empre.setText('')
    email = cadastros.campo_email_empre.setText('')
    cadastros.selec_estado_empre.setCurrentIndex(0)


#Cid

def cadastrar_cid():
    cod_cid = cadastros.campo_cod_cid.text()
    descricao_cid = cadastros.campo_descricao_cid.toPlainText()

    try:
        # Conecte ao banco de dados
        cursor = banco.cursor()

        # Defina a query de inserção
        query = """
            INSERT INTO CID (cod_cid, descricao_cid)
            VALUES (%s, %s)
        """
        
        # Defina os valores a serem inseridos
        valores = (cod_cid, descricao_cid)

        # Execute a query com os dados fornecidos
        cursor.execute(query, valores)

        # Faça commit da transação
        banco.commit()

        print("CID cadastrado com sucesso.")

        cadastros.campo_cod_cid.setText("")
        cadastros.campo_descricao_cid.setPlainText("")

    except:

        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código já cadastrado ou campo nulo.")
        erro.exec_()

    finally:
        # Feche o cursor e a conexão
        cursor.close()
        # Se houver uma variável de conexão `banco`, você pode também fechá-la aqui se necessário
        # banco.close()  # Apenas se a conexão não for usada em outro lugar

def atualizar_cid():
    cod_cid = cadastros.campo_cod_cid.text()
    descricao_cid = cadastros.campo_descricao_cid.toPlainText()

    try:
        # Conecte ao banco de dados
        cursor = banco.cursor()

        # Defina a query de atualização
        query = """
            UPDATE CID 
            SET descricao_cid = %s
            WHERE cod_cid = %s
        """
        
        # Defina os valores a serem atualizados
        valores = (descricao_cid, cod_cid)

        # Execute a query com os dados fornecidos
        cursor.execute(query, valores)

        # Faça commit da transação
        banco.commit()

        print("CID atualizado com sucesso.")

        cadastros.campo_cod_cid.setText("")
        cadastros.campo_descricao_cid.setPlainText("")

    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro!")
        erro.exec_()

    finally:
        # Feche o cursor e a conexão
        cursor.close()
        # Feche a conexão se necessário
        # banco.close()  # Apenas se a conexão não for usada em outro lugar

def excluir_cid():
    cod_cid = cadastros.campo_cod_cid.text()

    try:
        # Conecte ao banco de dados
        cursor = banco.cursor()

        # Defina a query de exclusão
        query = "DELETE FROM CID WHERE cod_cid = %s"
        
        # Defina os valores a serem usados na query
        valores = (cod_cid,)

        # Execute a query com o código CID fornecido
        cursor.execute(query, valores)

        # Faça commit da transação
        banco.commit()

        print("CID excluído com sucesso.")

        cadastros.campo_cod_cid.setText("")
        cadastros.campo_descricao_cid.setPlainText("")

    except :
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro!")
        erro.exec_()

    finally:
        # Feche o cursor e a conexão
        cursor.close()
        # Feche a conexão se necessário
        # banco.close()  # Apenas se a conexão não for usada em outro lugar

def consultar_cid():
    cod_cid = cadastros.campo_cod_cid.text()

    try:
        # Conecte ao banco de dados
        cursor = banco.cursor()

        # Defina a query de consulta
        query = "SELECT cod_cid, descricao_cid FROM CID WHERE cod_cid = %s"
        
        # Defina os valores a serem usados na query
        valores = (cod_cid,)

        # Execute a query com o código CID fornecido
        cursor.execute(query, valores)

        # Obtenha o resultado da consulta
        resultado = cursor.fetchone()

        cursor.close()

        if resultado:
            # O resultado foi encontrado, mas não há ação adicional aqui
            # Se o resultado for encontrado, preencha os campos da interface
            cod_cid, descricao_cid = resultado
            cadastros.campo_cod_cid.setText(cod_cid)
            cadastros.campo_descricao_cid.setPlainText(descricao_cid)
            pass
        else:
            erro = QtWidgets.QErrorMessage()
            erro.showMessage("Erro! Código não cadastrado ou campo nulo.")
            erro.exec_()

    except :
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código não cadastrado ou campo nulo.")
        erro.exec_()

    finally:
        # Feche o cursor e a conexão
        cursor.close()
        # Feche a conexão se necessário
        # banco.close()  # Apenas se a conexão não for usada em outro lugar

def limpar_campos():
    try:
        # Limpar os campos da interface
        cadastros.campo_cod_cid.setText("")
        cadastros.campo_descricao_cid.setPlainText("")

        print("Campos limpos com sucesso.")
        
    except Exception as e:
        print(f"Erro ao limpar os campos: {e}")



#Tipo de lesão

def cadastrar_lesao():
    cod_lesao = cadastros.campo_cod_lesao.text()
    descricao_lesao = cadastros.campo_descricao_lesao.toPlainText()

    try:
        # Conecte ao banco de dados
        cursor = banco.cursor()

        # Defina a query de inserção
        query = """
            INSERT INTO Lesao (cod_lesao, descricao_lesao)
            VALUES (%s, %s)
        """
        
        # Defina os valores a serem inseridos
        valores = (cod_lesao, descricao_lesao)

        # Execute a query com os dados fornecidos
        cursor.execute(query, valores)

        # Faça commit da transação
        banco.commit()

        print("Lesão cadastrado com sucesso.")

        cadastros.campo_cod_lesao.setText("")
        cadastros.campo_descricao_lesao.setPlainText("")


    except :
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código já cadastrado ou campo nulo.")
        erro.exec_()

    finally:
        # Feche o cursor e a conexão
        cursor.close()
        # Se houver uma variável de conexão `banco`, você pode também fechá-la aqui se necessário
        # banco.close()  # Apenas se a conexão não for usada em outro luga

def atualizar_lesao():
    cod_lesao = cadastros.campo_cod_lesao.text()
    descricao_lesao = cadastros.campo_descricao_lesao.toPlainText()

    try:
        # Conecte ao banco de dados
        cursor = banco.cursor()

        # Defina a query de atualização
        query = """
            UPDATE Lesao
            SET descricao_lesao = %s
            WHERE cod_lesao = %s
        """
        
        # Defina os valores a serem atualizados
        valores = (descricao_lesao, cod_lesao)

        # Execute a query com os dados fornecidos
        cursor.execute(query, valores)

        # Faça commit da transação
        banco.commit()

        print("Lesão atualizada com sucesso.")

        cadastros.campo_cod_lesao.setText("")
        cadastros.campo_descricao_lesao.setPlainText("")

    except :
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro!")
        erro.exec_()

    finally:
        # Feche o cursor e a conexão
        cursor.close()
        # Se houver uma variável de conexão `banco`, você pode também fechá-la aqui se necessário
        # banco.close()  # Apenas se a conexão não for usada em outro lugar

def excluir_lesao():
    cod_lesao = cadastros.campo_cod_lesao.text()

    try:
        # Conecte ao banco de dados
        cursor = banco.cursor()

        # Defina a query de exclusão
        query = "DELETE FROM Lesao WHERE cod_lesao = %s"
        
        # Defina os valores a serem usados na query
        valores = (cod_lesao,)

        # Execute a query com o código da lesão fornecido
        cursor.execute(query, valores)

        # Faça commit da transação
        banco.commit()

        print("Lesão excluída com sucesso.")

        cadastros.campo_cod_lesao.setText("")
        cadastros.campo_descricao_lesao.setPlainText("")

    except :
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro!")
        erro.exec_()

    finally:
        # Feche o cursor e a conexão
        cursor.close()
        # Se houver uma variável de conexão `banco`, você pode também fechá-la aqui se necessário
        # banco.close()  # Apenas se a conexão não for usada em outro lugar

def consultar_lesao():
    cod_lesao = cadastros.campo_cod_lesao.text()

    try:
        # Conecte ao banco de dados
        cursor = banco.cursor()

        # Defina a query de consulta
        query = "SELECT cod_lesao, descricao_lesao FROM Lesao WHERE cod_lesao = %s"
        
        # Defina o valor a ser usado na query
        valores = (cod_lesao,)

        # Execute a query com o código da lesão fornecido
        cursor.execute(query, valores)

        # Obtenha o resultado da consulta
        resultado = cursor.fetchone()

        cursor.close()

        if resultado:
            # Se o resultado for encontrado, preencha os campos da interface
            cod_lesao, descricao_lesao = resultado
            cadastros.campo_cod_lesao.setText(cod_lesao)
            cadastros.campo_descricao_lesao.setPlainText(descricao_lesao)
        else:
            erro = QtWidgets.QErrorMessage()
            erro.showMessage("Erro! Código não cadastrado ou campo nulo.")
            erro.exec_()

    except :
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código não cadastrado ou campo nulo.")
        erro.exec_()

    finally:
        # Feche o cursor e a conexão
        cursor.close()
        # Feche a conexão se necessário
        # banco.close()  # Apenas se a conexão não for usada em outro lugar

def limpar_campos_lesao():
    try:
        # Limpar os campos da interface
        cadastros.campo_cod_lesao.setText("")
        cadastros.campo_descricao_lesao.setPlainText("")

        print("Campos de lesão limpos com sucesso.")
        
    except Exception as e:
        print(f"Erro ao limpar os campos de lesão: {e}")

# Agente causador

def cadastrar_agente():
    cod_agente = cadastros.campo_cod_agente.text()
    nome_agente = cadastros.campo_nome_agen.toPlainText()
    descricao_agente = cadastros.campo_descricao_agen.toPlainText()

    try:
        # Conecte ao banco de dados
        cursor = banco.cursor()

        # Defina a query de inserção
        query = """
            INSERT INTO Agente (cod_agente, nome_agente, descricao_agente)
            VALUES (%s, %s, %s)
        """
        
        # Defina os valores a serem inseridos
        valores = (cod_agente, nome_agente, descricao_agente)

        # Execute a query com os dados fornecidos
        cursor.execute(query, valores)

        # Faça commit da transação
        banco.commit()

        print("Agente cadastrado com sucesso.")

        cadastros.campo_cod_agente.setText("")
        cadastros.campo_nome_agen.setPlainText("")
        cadastros.campo_descricao_agen.setPlainText("")

    except :
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código já cadastrado ou campo nulo.")
        erro.exec_()

    finally:
        # Feche o cursor e a conexão
        cursor.close()
        # Feche a conexão se necessário
        # banco.close()  # Apenas se a conexão não for usada em outro lugar

def atualizar_agente():
    cod_agente = cadastros.campo_cod_agente.text()
    nome_agente = cadastros.campo_nome_agen.toPlainText()
    descricao_agente = cadastros.campo_descricao_agen.toPlainText()

    try:
        # Conecte ao banco de dados
        cursor = banco.cursor()

        # Defina a query de atualização
        query = """
            UPDATE Agente
            SET nome_agente = %s, descricao_agente = %s
            WHERE cod_agente = %s
        """
        
        # Defina os valores a serem atualizados
        valores = (nome_agente, descricao_agente, cod_agente)

        # Execute a query com os dados fornecidos
        cursor.execute(query, valores)

        # Faça commit da transação
        banco.commit()

        print("Agente atualizado com sucesso.")

        cadastros.campo_cod_agente.setText("")
        cadastros.campo_nome_agen.setPlainText("")
        cadastros.campo_descricao_agen.setPlainText("")

    except :
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro!")
        erro.exec_()

    finally:
        # Feche o cursor e a conexão
        cursor.close()
        # Feche a conexão se necessário
        # banco.close()  # Apenas se a conexão não for usada em outro lugar

def excluir_agente():
    cod_agente = cadastros.campo_cod_agente.text()

    try:
        # Conecte ao banco de dados
        cursor = banco.cursor()

        # Defina a query de exclusão
        query = "DELETE FROM Agente WHERE cod_agente = %s"
            
        # Defina o valor a ser usado na query
        valores = (cod_agente,)

        # Execute a query com o código do agente fornecido
        cursor.execute(query, valores)

        # Faça commit da transação
        banco.commit()

        print("Agente excluído com sucesso.")

        cadastros.campo_cod_agente.setText("")
        cadastros.campo_nome_agen.setPlainText("")
        cadastros.campo_descricao_agen.setPlainText("")

    except :
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro!")
        erro.exec_()

    finally:
        # Feche o cursor e a conexão
        cursor.close()
        # Feche a conexão se necessário
        # banco.close()  # Apenas se a conexão não for usada em outro lugar

def consultar_agente():
    cod_agente = cadastros.campo_cod_agente.text()

    try:
        # Conecte ao banco de dados
        cursor = banco.cursor()

        # Defina a query de consulta
        query = "SELECT cod_agente, nome_agente, descricao_agente FROM Agente WHERE cod_agente = %s"
        
        # Defina o valor a ser usado na query
        valores = (cod_agente,)

        # Execute a query com o código do agente fornecido
        cursor.execute(query, valores)

        # Obtenha o resultado da consulta
        resultado = cursor.fetchone()

        cursor.close()

        if resultado:
            # Se o resultado for encontrado, preencha os campos da interface
            cod_agente, nome_agente, descricao_agente = resultado
            cadastros.campo_cod_agente.setText(cod_agente)
            cadastros.campo_nome_agen.setPlainText(nome_agente)
            cadastros.campo_descricao_agen.setPlainText(descricao_agente)
        else:
            erro = QtWidgets.QErrorMessage()
            erro.showMessage("Erro! Código não cadastrado ou campo nulo.")
            erro.exec_()

    except :
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Código não cadastrado ou campo nulo.")
        erro.exec_()

    finally:
        # Feche o cursor e a conexão
        cursor.close()
        # Feche a conexão se necessário
        # banco.close()  # Apenas se a conexão não for usada em outro lugar

def limpar_campos_agente():
    try:
        # Limpar os campos da interface
        cadastros.campo_cod_agente.setText("")
        cadastros.campo_nome_agen.setPlainText("")
        cadastros.campo_descricao_agen.setPlainText("")

        print("Campos de agente limpos com sucesso.")
        
    except Exception as e:
        print(f"Erro ao limpar os campos de agente: {e}")

#entrar e sair das telas de cat
#1
def chamar_cat1():
    cat1.show()
    inicial.close()
    
def sair_cat():
    inicial.show()
    cat1.close()
    
#2
def chamar_cat2():
    cat2.show()
    cat1.close()
    
def voltar_cat1():
    cat1.show()
    cat2.close()
    
#3    
def chamar_cat3():
    cat3.show()
    cat2.close()
    
def voltar_cat2():
    cat2.show()
    cat3.close()

#4
def chamar_cat4():
    cat4.show()
    cat3.close()
    
def voltar_cat3():
    cat3.show()
    cat4.close()

from datetime import datetime

def verificar_data_aaaa_mm_dd(data):
    if not data:  # Se a data estiver vazia, retorna None
        return None
    try:
        # Verifica se a data está no formato AAAA/MM/DD e a retorna no formato YYYY-MM-DD
        return datetime.strptime(data, '%Y/%m/%d').strftime('%Y-%m-%d')
    except ValueError:
        return None  # Retorna None se a data for inválida


#cadastro da cat
def cad_cat():
    #informações do emitente
    emitente = cat1.campo_emitente.text()
    data_emissao = cat1.campo_data_emissao.text()
    tipo_cat = cat1.selec_tipo_cat.currentText()
    comu_obito = cat1.selec_obito.currentText()
    filiacao = cat1.campo_filiacao.text()
    email_emi = cat1.campo_email.text()

    #informações do empregador
    cnpj = cat1.campo_cnpj.text()
    nome_empre = cat1.campo_razao_nome.text()
    tipo = cat1.campo_tipo_doc.text()
    cnae = cat1.campo_cnae.text()
    tele_empre = cat1.campo_telefone_empregador.text()
    cep_empre = cat1.campo_cep_empregador.text()
    endereco_empre = cat1.campo_endereco_empregador.text()
    bairro_empre = cat1.campo_bairro_cep.text()
    municipio_empre = cat1.campo_municipio_empregador.text()
    estado_empre = cat1.selec_estado_empregador.currentText()

    #informações do acidentado
    cpf = cat2.campo_cpf.text()
    nome_func = cat2.campo_nome.text()
    nome_mae_func = cat2.campo_nome_mae.text()
    nascimento = cat2.campo_data_nascimento.text()
    sexo = cat2.selec_sexo.currentText()
    grau_instru = cat2.selec_grau.currentText()
    estado_civil = cat2.selec_estado_civil.currentText()
    identidade = cat2.campo_identidade.text()
    ctps = cat2.campo_ctps.text()
    remuneracao = cat2.campo_remune.text()
    pis = cat2.campo_pis.text()
    cep_func = cat2.campo_cep.text()
    endereco_func = cat2.campo_endereco.text()
    bairro_func = cat2.campo_bairro.text()
    municipio_func = cat2.campo_municipio.text()
    estado_func = cat2.selec_estado.currentText()
    tele_func= cat2.campo_telefone.text()
    cbo = cat2.campo_cbo.text()
    aposentadoria = cat2.select_apo.currentText()
    area_func = cat2.campo_area.text()

    #informações do acidente
    data_acidente = cat3.campo_data_aci.text()
    hora_acidente = cat3.campo_acidentehr.text()
    horas_trabalhadas = cat3.campo_horasT.text()
    tipo_lesao = cat3.campo_tipo.text()
    afastamento = cat3.selec_afastamento.currentText()
    reg_policial = cat3.selec_policia.currentText()
    local_acidente = cat3.campo_local.text()
    esp_local = cat3.campo_esplocal.text()
    cnpj_cgc_cei = cat3.campo_prestadora.text()
    uf_acidente = cat3.selec_estado.currentText()
    municipio_acidente = cat3.campo_municipio.text()
    ultimo_dia_trab = cat3.campo_dia_trab.text()
    parte_corpo = cat3.campo_pcorpo.text()
    agente_causador = cat3.campo_causador.text()
    sit_geradora = cat3.campo_geradora.text()
    morte = cat3.selec_obito.currentText()
    data_obito = cat3.campo_dt_obito.text()

    #informações do atestado médico
    unidade = cat4.campo_unidade.text()
    data_atendimento = cat4.campo_data_atendimento.text()
    hora_atendimento = cat4.campo_hora_atend.text()
    internacao = cat4.campo_sim_nao.currentText()
    afastamento2 = cat4.selec_afastado.currentText()
    nat_lesao = cat4.campo_nat_lesao.text()
    cid_10 = cat4.campo_cid_10.text()
    observacoes = cat4.campo_obs.text()
    crm = cat4.campo_crm.text()

    # Verificar datas no formato AAAA/MM/DD, aceitando nulos
    data_emissao = verificar_data_aaaa_mm_dd(data_emissao)
    nascimento = verificar_data_aaaa_mm_dd(nascimento)
    data_acidente = verificar_data_aaaa_mm_dd(data_acidente)
    data_obito = verificar_data_aaaa_mm_dd(data_obito)
    ultimo_dia_trab = verificar_data_aaaa_mm_dd(ultimo_dia_trab)
    data_atendimento = verificar_data_aaaa_mm_dd(data_atendimento)



    cursor = banco.cursor()

    cadastro = """
    INSERT INTO cat(
        emitente_cat,data_emissao_cat,tipo_cat,comunicacao_obito,filiacao,email_emitente,cnpj_empresa,nome_empresa,
        tipo_num_doc_empresa,cnae_empresa,telefone_empresa,cep_empresa,bairro_empresa,estado_empresa,endereco_empresa,
        municipio_empresa,cpf_func,nome_func,nome_mae_func,data_nascimento_func,sexo,grau_instrucao_func,identidade_func,estado_civil,
        ctps_func,remuneracao_func,pis_pasep_nit_func,cep_func,endereco_func,bairro_func,municipio_func,estado_func,
        telefone_func,cbo_func,aposentadoria_func,area_func,data_acidente,hora_acidente,horas_trabalhadas,tipo_acidente,
        afastamento,reg_policial,local_acidente,esp_local,cnpj_cgc_empresa,uf_acidente,municipio_acidente,ult_dia_trab,
        parte_corpo,agente_causador,sit_geradora,morte,data_obito,unidade,data_atendimento_medico,hora_atendimento_medico,
        houve_internacao,afastado,nat_lesao,cid,observacao,crm
    ) VALUES (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s
    )
    """
    valores = (
        emitente,data_emissao,tipo_cat,comu_obito,filiacao,email_emi,cnpj,nome_empre,tipo,cnae,tele_empre,cep_empre,endereco_empre,
        bairro_empre,municipio_empre,estado_empre,cpf,nome_func,nome_mae_func,nascimento,sexo,grau_instru,estado_civil,identidade,
        ctps,remuneracao,pis,cep_func,endereco_func,bairro_func,municipio_func,estado_func,tele_func,cbo,aposentadoria,area_func,
        data_acidente,hora_acidente,horas_trabalhadas,tipo_lesao,afastamento,reg_policial,local_acidente,esp_local,cnpj_cgc_cei,
        uf_acidente,municipio_acidente,ultimo_dia_trab,parte_corpo,agente_causador,sit_geradora,morte,data_obito,unidade,
        data_atendimento,hora_atendimento,internacao,afastamento2,nat_lesao,cid_10,observacoes,crm
    )
    
    try:
        cursor.execute(cadastro, valores)
        banco.commit()
        cursor.close()

        #informações do emitente
        emitente = cat1.campo_emitente.setText('')
        data_emissao = cat1.campo_data_emissao.setText('')
        tipo_cat = cat1.selec_tipo_cat.setCurrentIndex(0)
        comu_obito = cat1.selec_obito.setCurrentIndex(0)
        filiacao = cat1.campo_filiacao.setText('')
        email_emi = cat1.campo_email.setText('')

        #informações do empregador
        cnpj = cat1.campo_cnpj.setText('')
        nome_empre = cat1.campo_razao_nome.setText('')
        tipo = cat1.campo_tipo_doc.setText('')
        cnae = cat1.campo_cnae.setText('')
        tele_empre = cat1.campo_telefone_empregador.setText('')
        cep_empre = cat1.campo_cep_empregador.setText('')
        endereco_empre = cat1.campo_endereco_empregador.setText('')
        bairro_empre = cat1.campo_bairro_cep.setText('')
        municipio_empre = cat1.campo_municipio_empregador.setText('')
        estado_empre = cat1.selec_estado_empregador.setCurrentIndex(0)

        #informações do acidentado
        cpf = cat2.campo_cpf.setText('')
        nome_func = cat2.campo_nome.setText('')
        nome_mae_func = cat2.campo_nome_mae.setText('')
        nascimento = cat2.campo_data_nascimento.setText('')
        sexo = cat2.selec_sexo.setCurrentIndex(0)
        grau_instru = cat2.selec_grau.setCurrentIndex(0)
        estado_civil = cat2.selec_estado_civil.setCurrentIndex(0)
        identidade = cat2.campo_identidade.setText('')
        ctps = cat2.campo_ctps.setText('')
        remuneracao = cat2.campo_remune.setText('')
        pis = cat2.campo_pis.setText('')
        cep_func = cat2.campo_cep.setText('')
        endereco_func = cat2.campo_endereco.setText('')
        bairro_func = cat2.campo_bairro.setText('')
        municipio_func = cat2.campo_municipio.setText('')
        estado_func = cat2.selec_estado.setCurrentIndex(0)
        tele_func= cat2.campo_telefone.setText('')
        cbo = cat2.campo_cbo.setText('')
        aposentadoria = cat2.select_apo.setCurrentIndex(0)
        area_func = cat2.campo_area.setText('')
        #informações do acidente
        data_acidente = cat3.campo_data_aci.setText('')
        hora_acidente = cat3.campo_acidentehr.setText('')
        horas_trabalhadas = cat3.campo_horasT.setText('')
        tipo_lesao = cat3.campo_tipo.setText('')
        afastamento = cat3.selec_afastamento.setCurrentIndex(0)
        reg_policial = cat3.selec_policia.setCurrentIndex(0)
        local_acidente = cat3.campo_local.setText('')
        esp_local = cat3.campo_esplocal.setText('')
        cnpj_cgc_cei = cat3.campo_prestadora.setText('')
        uf_acidente = cat3.selec_estado.setCurrentIndex(0)
        municipio_acidente = cat3.campo_municipio.setText('')
        ultimo_dia_trab = cat3.campo_dia_trab.setText('')
        parte_corpo = cat3.campo_pcorpo.setText('')
        agente_causador = cat3.campo_causador.setText('')
        sit_geradora = cat3.campo_geradora.setText('')
        morte = cat3.selec_obito.setCurrentIndex(0)
        data_obito = cat3.campo_dt_obito.setText('')

        #informações do atestado médico
        unidade = cat4.campo_unidade.setText('')
        data_atendimento = cat4.campo_data_atendimento.setText('')
        hora_atendimento = cat4.campo_hora_atend.setText('')
        internacao = cat4.campo_sim_nao.setCurrentIndex(0)
        afastamento2 = cat4.selec_afastado.setCurrentIndex(0)
        nat_lesao = cat4.campo_nat_lesao.setText('')
        cid_10 = cat4.campo_cid_10.setText('')
        observacoes = cat4.campo_obs.setText('')
        crm = cat4.campo_crm.setText('')

        concluido.show()

    except:
        erro = QtWidgets.QErrorMessage()
        erro.showMessage("Erro! Confira o preenchimento dos campos.")
        erro.exec_()

#voltar para a tela de cat1
def voltar_cat1_fin():
    cat1.show()
    concluido.close()
    cat4.close()

def cad_cons_func():
    cpf = cat2.campo_cpf.text()

    cursor = banco.cursor()
    consulta = """SELECT cpf_func, nome_func, nome_mae_func, data_nascimento_func, sexo, estado_civil, remuneracao_func, 
                  ctps_func, identidade_func, pis_pasep_nit_func, cep_func, endereco_func, bairro_func, estado_func, 
                  municipio_func, telefone_func, cbo_func, aposentadoria_func, area_func, grau_instrucao_func 
                  FROM funcionario WHERE cpf_func = %s"""
    valores = (cpf,)
    cursor.execute(consulta, valores)

    busca = cursor.fetchone()
    cursor.close()

    if busca:
        try:
            (cpf_func, nome_func, nome_mae_func, data_nascimento_func, sexo, estado_civil, remuneracao_func, ctps_func,
             identidade_func, pis_pasep_nit_func, cep_func, endereco_func, bairro_func, estado_func, municipio_func,
             telefone_func, cbo_func, aposentadoria_func, area_func, grau_instrucao_func) = busca
            
            # Preenchendo os campos de texto
            cat2.campo_cpf.setText(cpf_func)
            cat2.campo_nome.setText(nome_func)
            cat2.campo_nome_mae.setText(nome_mae_func)

            # Exibindo a data no formato "YYYY-MM-DD"
            if data_nascimento_func:
                cat2.campo_data_nascimento.setText(str(data_nascimento_func))

            # Preenchendo os campos de seleção (QComboBox)
            sexo_index = cat2.selec_sexo.findText(sexo, QtCore.Qt.MatchFixedString)
            if sexo_index >= 0:
                cat2.selec_sexo.setCurrentIndex(sexo_index)

            estado_civil_index = cat2.selec_estado_civil.findText(estado_civil, QtCore.Qt.MatchFixedString)
            if estado_civil_index >= 0:
                cat2.selec_estado_civil.setCurrentIndex(estado_civil_index)

            estado_func_index = cat2.selec_estado.findText(estado_func, QtCore.Qt.MatchFixedString)
            if estado_func_index >= 0:
                cat2.selec_estado.setCurrentIndex(estado_func_index)

            aposentadoria_index = cat2.select_apo.findText(aposentadoria_func, QtCore.Qt.MatchFixedString)
            if aposentadoria_index >= 0:
                cat2.select_apo.setCurrentIndex(aposentadoria_index)

            grau_instrucao_index = cat2.selec_grau.findText(grau_instrucao_func, QtCore.Qt.MatchFixedString)
            if grau_instrucao_index >= 0:
                cat2.selec_grau.setCurrentIndex(grau_instrucao_index)

            # Preenchendo os outros campos de texto, convertendo para string
            cat2.campo_remune.setText(str(remuneracao_func))  # Certifique-se de que seja string
            cat2.campo_ctps.setText(str(ctps_func) if ctps_func else "")
            cat2.campo_identidade.setText(str(identidade_func) if identidade_func else "")
            cat2.campo_pis.setText(str(pis_pasep_nit_func) if pis_pasep_nit_func else "")
            cat2.campo_cep.setText(str(cep_func) if cep_func else "")
            cat2.campo_endereco.setText(str(endereco_func) if endereco_func else "")
            cat2.campo_bairro.setText(str(bairro_func) if bairro_func else "")
            cat2.campo_municipio.setText(str(municipio_func) if municipio_func else "")
            cat2.campo_telefone.setText(str(telefone_func) if telefone_func else "")
            cat2.campo_cbo.setText(str(cbo_func) if cbo_func else "")  # Garantindo que cbo_func seja string
            cat2.campo_area.setText(str(area_func) if area_func else "")

        except Exception as e:
            # Exibir erro em uma caixa de diálogo
            erro = QtWidgets.QMessageBox()
            erro.setIcon(QtWidgets.QMessageBox.Critical)
            erro.setWindowTitle("Erro")
            erro.setText(f"Erro ao carregar dados: {str(e)}")
            erro.exec_()

    else:
        # Caso a consulta não retorne nenhum dado
        erro = QtWidgets.QMessageBox()
        erro.setIcon(QtWidgets.QMessageBox.Warning)
        erro.setWindowTitle("Consulta não encontrada")
        erro.setText("Nenhum funcionário encontrado com este CPF ou campo nulo.")
        erro.exec_()

def cad_cons_empre():
    cnpj = cat1.campo_cnpj.text()

    cursor = banco.cursor()

    consulta = """SELECT cnpj_empresa, nome_empresa, tipo_num_doc_empresa, cnae_empresa, cep_empresa, 
                  endereco_empresa, bairro_empresa, municipio_empresa, estado_empresa, telefone_empresa 
                  FROM empresa WHERE cnpj_empresa = %s"""
    valores = (cnpj,)
    
    cursor.execute(consulta, valores)

    selecao = cursor.fetchone()
    cursor.close()

    if selecao:
        try:
            (cnpj_empresa, nome_empresa, tipo_num_doc_empresa, cnae_empresa, cep_empresa, endereco_empresa,
             bairro_empresa, municipio_empresa, estado_empresa, telefone_empresa) = selecao

            # Preenchendo os campos da interface
            cat1.campo_cnpj.setText(cnpj_empresa)
            cat1.campo_razao_nome.setText(nome_empresa)
            cat1.campo_tipo_doc.setText(tipo_num_doc_empresa)
            cat1.campo_cnae.setText(cnae_empresa)
            cat1.campo_cep_empregador.setText(cep_empresa)
            cat1.campo_endereco_empregador.setText(endereco_empresa)
            cat1.campo_bairro_cep.setText(bairro_empresa)
            cat1.campo_municipio_empregador.setText(municipio_empresa)

            # Verificando e ajustando a seleção no ComboBox (estado)
            estado_index = cat1.selec_estado_empregador.findText(estado_empresa, QtCore.Qt.MatchFixedString)
            if estado_index >= 0:
                cat1.selec_estado_empregador.setCurrentIndex(estado_index)

            cat1.campo_telefone_empregador.setText(telefone_empresa)
        
        except Exception as e:
            # Tratamento de erro ao preencher os campos
            erro = QtWidgets.QMessageBox()
            erro.setIcon(QtWidgets.QMessageBox.Critical)
            erro.setWindowTitle("Erro")
            erro.setText(f"Erro ao carregar os dados da empresa: {str(e)}")
            erro.exec_()

    else:
        # Exibir mensagem de erro caso a consulta não retorne resultados
        erro = QtWidgets.QMessageBox()
        erro.setIcon(QtWidgets.QMessageBox.Warning)
        erro.setWindowTitle("Consulta não encontrada")
        erro.setText("Nenhuma empresa encontrada com este CNPJ ou campo nulo.")
        erro.exec_()

#chamar tela de consulta
#entrar
def chamar_consulta():
    consulta.show()
    inicial.close()
    
#sair
def sair_consulta():
    consulta.campo_pesquisa.setText('')
    consulta.campo_cod.setText('')

    inicial.show()
    consulta.close()


def pesquisa_consulta():
    # Campo de pesquisa
    pesq = consulta.campo_pesquisa.text()

    # Criando cursor
    cursor = banco.cursor()

    # Selecionar a tabela (substitua 'sua_tabela' pelo nome real da tabela)
    pesquisa = f"SELECT cod_cat, emitente_cat, data_emissao_cat, cnpj_empresa, nome_empresa, cpf_func, nome_func, data_nascimento_func FROM cat  WHERE cnpj_empresa = '{pesq}' OR cpf_func = '{pesq}' "

    try:
        # Executar o cursor
        cursor.execute(pesquisa)

        # Varrer os dados
        selecao = cursor.fetchall()

        # Fechar cursor
        cursor.close()


        # Gerar o PDF
        # gerar_pdf(selecao)

    except Exception as e:
        print(f'ERRO: {e}')
        return
    
    # Montar a tabela (ajuste o número de colunas conforme necessário)
    consulta.tab_consulta.setRowCount(len(selecao))
    consulta.tab_consulta.setColumnCount(8)
    
    for i in range(0, len(selecao)):
        for j in range(0, 8):
            consulta.tab_consulta.setItem(i, j, QtWidgets.QTableWidgetItem(str(selecao[i][j])))

import os
from fpdf import FPDF
import mysql.connector

# Dicionário de apelidos
apelidos = {
    'João Silva': 'Joãozinho',
    'Maria Souza': 'Mari',
    'Carlos Pereira': 'Carlão',
}

# Dicionário para renomear as colunas
colunas_personalizadas = {
    # Adicione suas colunas personalizadas aqui
}

class CustomPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_left_margin(15)
        self.set_right_margin(15)
        self.set_top_margin(15)
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.page_no() == 1:
            self.image('Telas/Imagens/ProSafe-removebg-preview.png', x=80, y=10, w=50)
            self.ln(30)
            self.set_font('Arial', 'B', 14)
            self.set_text_color(33, 37, 41)
            self.cell(0, 15, 'Relatório de CAT', 0, 1, 'C')
            self.ln(10)

    def footer(self):
        self.set_y(-20)
        self.set_draw_color(169, 169, 169)
        self.set_line_width(0.5)
        self.line(15, self.get_y(), 200, self.get_y())
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(169, 169, 169)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        if self.page_no() == 1:
            self.set_font('Arial', 'B', 14)
            self.set_text_color(0, 102, 204)
            self.cell(0, 12, title, 0, 1, 'C')
            self.ln(8)

    def add_section(self, title, content):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 200, 200)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, title, 1, 1, 'L', fill=True)
        self.set_font('Arial', '', 11)
        self.set_fill_color(255, 255, 255)
        self.multi_cell(0, 10, content, 1, 'L', fill=True)
        self.ln(5)

def gerar_pdfs():
    # Conectar ao banco de dados
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        port='3308',
        password='Senac',
        database='CAT_TREINEE'
    )
    cursor = conn.cursor()

    # Consulta ao banco de dados
    cursor.execute("SELECT * FROM cat")
    resultados = cursor.fetchall()

    # Obter os nomes das colunas
    colunas = [desc[0] for desc in cursor.description]

    # Obtendo o caminho da pasta Downloads do Windows
    caminho_downloads = os.path.join(os.path.expanduser('~'), 'Downloads')

    # Gera um PDF para cada registro
    for idx, row in enumerate(resultados, start=1):
        pdf = CustomPDF()
        pdf.add_page()

        # Título do Relatório na primeira página
        if pdf.page_no() == 1:
            pdf.chapter_title(f'Relatório de CAT - Registro {idx}')

        # Adiciona os dados ao PDF em seções estilo CAT
        colunas_processadas = set()

        for i, item in enumerate(row):
            if colunas[i] not in colunas_processadas:
                valor = str(item)
                if colunas[i] == 'nome_func' and valor in apelidos:
                    valor = apelidos[valor]

                titulo_coluna = colunas_personalizadas.get(colunas[i], colunas[i])
                pdf.add_section(titulo_coluna, valor)
                colunas_processadas.add(colunas[i])

        # Define o caminho completo para salvar o PDF na pasta Downloads
        caminho_pdf = os.path.join(caminho_downloads, f'relatorio_cat_{idx}.pdf')
        
        # Salva o PDF no caminho especificado
        pdf.output(caminho_pdf)

    conn.close()

# Chame a função para gerar os PDFs
gerar_pdfs()



# Adicionar telas
login = uic.loadUi('Telas/tela_login_cat_diego.ui')

cad_inicial = uic.loadUi('Telas/cad_func_inicial.ui')

inicial = uic.loadUi('Telas/tela_inicial_cat_diego.ui')

cadastros = uic.loadUi('Telas/tela_cadastros_diego.ui')

cat1 = uic.loadUi('Telas/cadastro_cat_1.ui')

cat2 = uic.loadUi('Telas/cadastro_cat_2.ui')

cat3 = uic.loadUi('Telas/cadastro_cat_3.ui')

cat4 = uic.loadUi('Telas/cadastro_cat_4.ui')

concluido = uic.loadUi('Telas/tela_cat_concluida.ui')

consulta = uic.loadUi('Telas/consulta.ui')


# Adicionar função aos botões
#botao para ir para inicial
login.bt_logar.clicked.connect(chamar_inicial)

#botao ir para cadastro inicial
login.bt_cadastrese.clicked.connect(chamar_cad_inicial)
#botao para sair da cad inicial
cad_inicial.bt_voltar_func.clicked.connect(sair_cad_inicial)
#cadastro inicial
cad_inicial.bt_cadastrar_func.clicked.connect(cad_func_inicial)

#botao para entrar na tela de cadastro
inicial.bt_cadastros.clicked.connect(chamar_cadastros)

#botoes referentes aos funcionarios
cadastros.bt_voltar_func.clicked.connect(sair_cadastros)
cadastros.bt_cadastrar_func.clicked.connect(func_cadastros)
cadastros.bt_consultar_func.clicked.connect(culsutar_func)
cadastros.bt_excluir_func.clicked.connect(remover_funcionario)
cadastros.bt_atualizar_func.clicked.connect(atualizar_func)
cadastros.bt_limpar_func.clicked.connect(limpar_func)

#botoes referentes as empresas
cadastros.bt_voltar_empre.clicked.connect(sair_cadastros)
cadastros.bt_cadastrar_empre.clicked.connect(cad_empresa)
cadastros.bt_atualizar_empre.clicked.connect(atualizar_empresa)
cadastros.bt_excluir_empre.clicked.connect(excluir_empresa)
cadastros.bt_consultar_empre.clicked.connect(consulta_empresa)
cadastros.bt_limpar_empre.clicked.connect(limpar_tela_empre)

#botoes referentes aos medicos
cadastros.bt_voltar_med.clicked.connect(sair_cadastros)
cadastros.bt_cadastrar_med.clicked.connect(cad_medico)
cadastros.bt_atualizar_med.clicked.connect(atualizar_medico)
cadastros.bt_excluir_med.clicked.connect(excluir_medico)
cadastros.bt_consultar_med.clicked.connect(consulta_medico)
cadastros.bt_limpar_med.clicked.connect(limpar_tela_med)

#CID
cadastros.bt_cadastrar_cid.clicked.connect(cadastrar_cid)
cadastros.bt_atualizar_cid.clicked.connect(atualizar_cid)
cadastros.bt_excluir_cid.clicked.connect(excluir_cid)
cadastros.bt_consultar_cid.clicked.connect(consultar_cid)
cadastros.bt_limpar_cid.clicked.connect(limpar_campos)
cadastros.bt_voltar_cid.clicked.connect(sair_cadastros)

#Tipo de lesão
cadastros.bt_cadastrar_lesao.clicked.connect(cadastrar_lesao)
cadastros.bt_atualizar_lesao.clicked.connect(atualizar_lesao)
cadastros.bt_excluir_lesao.clicked.connect(excluir_lesao)
cadastros.bt_consultar_lesao.clicked.connect(consultar_lesao)
cadastros.bt_limpar_lesao.clicked.connect(limpar_campos_lesao)
cadastros.bt_voltar_lesao.clicked.connect(sair_cadastros)

#Agente Causador
cadastros.bt_cadastrar_agen.clicked.connect(cadastrar_agente)
cadastros.bt_atualizar_agen.clicked.connect(atualizar_agente)
cadastros.bt_excluir_agen.clicked.connect(excluir_agente)
cadastros.bt_consultar_agen.clicked.connect(consultar_agente)
cadastros.bt_limpar_agen.clicked.connect(limpar_campos_agente)
cadastros.bt_voltar_agen.clicked.connect(sair_cadastros)


#botoes das telas de cat
#1
inicial.bt_cat.clicked.connect(chamar_cat1)
cat1.bt_voltar.clicked.connect(sair_cat)

cat1.bt_pesquisa.clicked.connect(cad_cons_empre)

#2
cat1.bt_proximo.clicked.connect(chamar_cat2)
cat2.bt_anterior.clicked.connect(voltar_cat1)

cat2.bt_pesquisa.clicked.connect(cad_cons_func)

#3
cat2.bt_proximo.clicked.connect(chamar_cat3)
cat3.bt_anterior.clicked.connect(voltar_cat2)

#4
cat3.bt_proximo.clicked.connect(chamar_cat4)
cat4.bt_anterior.clicked.connect(voltar_cat3)

#botao de cadastro de cat
cat4.bt_finalizar.clicked.connect(cad_cat)

#botao para voltar para a cat1
concluido.bt_fechar.clicked.connect(voltar_cat1_fin)

#botoes de consulta da cat
#entrar
inicial.bt_consultas.clicked.connect(chamar_consulta)

#sair
consulta.bt_voltar.clicked.connect(sair_consulta)

#pesquisar na tabela
consulta.bt_pesquisa.clicked.connect(pesquisa_consulta)

#gerar pdf
consulta.gerar_pdf.clicked.connect(gerar_pdfs)




login.show()
app.exec_()