from selenium import webdriver
from time import sleep

dados = {'nome': ['João', 'Carlos', 'André', 'Felipe', 'Ana', 'Carla', 'Bruna', 'Sabrina'],
         'sobrenome': ['Silveira', 'Silva', 'Santos', 'Bragança', 'Prado', 'Santana', 'Almeida', 'Barros'],
         'email': ['Joao.Silveira@gmail.com', 'Carlos.Silveira@gmail.com', 'Andre.Silveira@gmail.com', 'Felipe.Silveira@gmail.com', 'Ana.Silveira@gmail.com', 'Carla.Silveira@gmail.com', 'Bruna.Silveira@gmail.com', 'Sabrina.Silveira@gmail.com'],
         'pessoas': ['2', '5', '1', '4', '4', '1', '4', '3'],
         'mês': ['January','February', 'March', 'April', 'Mai', 'June', 'July', 'August'],
         'dia': ['22', '2', '4', '15', '15', '7', '26', '15'],
         'ano': ['2002', '1987', '1965', '1992', '1997', '1967', '1999', '2014'],
         'freepickup': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
         'numero_voo': ['569360', '711065', '315099', '191524', '157563', '959979', '547274', '775766'],
         'requisitos': ['Não tem requisitos especiais', 'Não tem requisitos especiais', 'Não tem requisitos especiais', 'Não tem requisitos especiais', 'Não tem requisitos especiais', 'Não tem requisitos especiais', 'Não tem requisitos especiais', 'Não tem requisitos especiais']
         }

navegador = webdriver.Edge()
link = 'https://form.jotform.com/230504787541659'
navegador.get(link)
sleep(5)

for i in range(8):

    navegador.find_element('id', 'first_105').send_keys(dados['nome'][i])
    navegador.find_element('id', 'last_105').send_keys(dados['sobrenome'][i])
    navegador.find_element('id', 'input_17').send_keys(dados['email'][i])

    # navegador.find_element('id', 'input_42').send_keys(dados['pessoas'])
    # navegador.find_element('id', 'input_42').send_keys(dados['mês'])
    # navegador.find_element('id', 'input_42').send_keys(dados['dia'])
    # navegador.find_element('id', 'input_42').send_keys(dados['ano'])

    # if freepickup[i] == 'Yes':
    #   navegador.find_element('id', 'label_input_10_0').click()
    # elif freepickup[i] == 'No':
    #   navegador.find_element('id', 'label_input_10_1').click()

    navegador.find_element('id', 'input_28').send_keys(dados['numero_voo'][i])
    navegador.find_element('id', 'input_30').send_keys(dados['requisitos'][i])

    navegador.find_element('id', 'input_2').click()