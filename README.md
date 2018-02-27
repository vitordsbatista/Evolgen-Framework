# Evolgen-Framework
Framework para o auxílio no desenvolvimento de algoritmos evolutivos

Eu fiz esse framework para poder brincar com os parâmetros operadores genéticos/evolutivos de alguns algoritmos evolutivos, sem ter muito trabalho, como exemplo trocar o operador de cruzamento de um NSGA-II, ou transformar um GA (genetic algorithm) num ES (evolutionary strategies) e até mesmo fazer algum algoritmo maluco misturando PAES e SPEA num só programa sem muito esforço.

## Requisitos

- numpy
- matplotlib

## Utilização

### População inicial
Primeiramente você deve ter "em mãos" uma população inicial, caso não tenhas uma população inicial, o framework tem a capacidade de criar uma população para a execução, mas somente inteiro, decimal e binário. Qualquer variação disso (ou mistura delas, parte binário, parte inteiro) você que deve passar. Exemplo:

#### Código com uma população inicial (parêmetro has_pop verdadeiro)
Caso você passe uma população, é importante que ela seja organizada da seguinte maneira:
- A população deverá ser compatível com a função de avaliação
- Ela dever ser do tipo *list* ou *np.array*
- Os valores da dimensão *x*, devem ser os indivíduos da população, por exemplo, numa matrix [n, m], os valores em *n* devem ser os indivíduos, da mesma forma, em uma matriz 3D [n, m, o], os valores em *n* devem ser os indivíduos e assim por diante.

```python
egg = egg.evolgen(has_pop=True, population=sua_populacao, outros_parametros)
```
#### Código sem uma população inicial (parêmetro has_pop falso)
```python
pop_size = 100          #Tamanho da população
ind_size = 10           #Tamanho dos indivíduos
ind_range = [-10, 10]   #Intervalo dos gens dos indivíduos
ind_type = 'float'      #Tipo dos indivíduos, pode ser ['float', 'int', 'bin']

egg = egg.evolgen(has_pop=False, population=[pop_size, ind_size, ind_range, ind_type], outros_parametros)
```
*NOTA: os outros_parametros serão explicados a seguir, não execute seu código ainda*

### Função de avaliação
Você deve passar a função de avaliação (*fitness*) para o programa, ela é obrigatória!

#### Modelo de função objetivo
As funções objetivo devem seguir o modelo abaixo para que o evolgen execute normalmente

```python
def sua_funcao(self, ind):          #Ela irá apenas ler um indivíduo, e não uma população
    #Agora vem a sua função avaliando apenas um indivíduo (tenha isso em mente)
    x, y = ind                      #Descompactando o indivíduo (opcional)
    res = x**2 + y**2               #Faça o que você quiser para avaliar
    return res                      #Saída da função, deve ser apenas um valor
```
*Nota: o 'self' passado na sua_funcao é uma palavra reservada da POO (Programação Orientada a Objetos) do pyhton, ela será utilizada para passar algum valor que você precise para fazer a avaliação do indivíduo, mas não está relacionado à população, clique aqui para saber mais*

#### Passagem de parâmetro
A função de avaliação como parâmetro deve ser uma lista (por causa do multiobjetivo). Se você têm apenas uma função de avaliação, basta passar ela como uma lista unitária, e se for multiobjetivo, basta passar como parâmetro todas as funções objetivo numa lista:

```python
#Apenas uma função objetivo
egg = egg.evolgen(has_pop=True, population=sua_populacao, 
                                fit_func=[sua_funcao_fitness], 
                                outros_parametros)

#Mais de uma função objetivo
egg = egg.evolgen(has_pop=True, population=sua_populacao, 
                                fit_func=[sua_funcao_1, sua_funcao_2, sua_funcao_3], 
                                outros_parametros)
```
#### Bônus
O evolgen fornece algumas funções de avaliação para você brincar um pouco (vou acrescentando mais quando der), basta importar elas do arquivo *fit_func.py* e passar elas como parâmetro.

A lista completa de funções de avaliação pode ser encontrada (*AQUI*)

```python
import fit_func as fit
#Exemplo multiobjetivo
egg = egg.evolgen(has_pop=True, population=sua_populacao, 
                                fit_func=[fit.pol_f1, fit.pol_f2], 
                                outros_parametros)
```
### Operadores genéticos/evolutivos e seus parâmetros

Quase finalizando, agora você deve passar os operadores genéticos/evolutivos que o evolgen irá executar. Neste caso você vai ter que passar duas (2) listas, uma dos operadores evolutivos e a outra com os seus respectivos parâmetros. Existe uma lista com todos os algoritmos já feitos por mim, e pelos usuários, e seus parâmetros, basta clicar (*AQUI*)

#### Lista com os operadores
Esta é uma lista de *strings* contendo as siglas da sequência dos operadores que o programa irá executar. Por exemplo, para um 
algoritmo evolutivo normal, com seleção por torneio, cruzamento de um ponto, e mutação uniformemente aleatória, basta ter uma 
lista da seguinte forma:

```python
ope = ['sto',       #Seleção por torneio
       'cop',       #Cruzamento por um ponto
       'mru']       #Mutação uniformemente aleatória
```
#### Lista com os parâmetros dos operadores
Esta é uma lista de listas (alguns chamam de matriz), contendo os parâmetros de cada um dos operadores. Caso um operador não possua parâmetros, no lugar dele basta passar uma lista vazia, exemplo:
```python
#Parâmtros para os operadores acima
ope_par = [[0.8],       #Parâmentro da seleção por torneio
           [0.7],       #Parâmetros do cruzamento por um ponto
           [0.03]]      #Parâmetro da mutação uniformemente aleatória

#Exemplo de parâmetros vazios
ope_par = [[],          #Parâmetro vazio
           [0.4],       #Outros parâmetros
           [22]]        #Outros parâmetros
```

#### Passando para o evolgen
Terminando de realizar as escolhas dos operadores e de seus parâmetros, basta passar todos esses valores para o evolgen da seguinte forma:

```python
egg = egg.evolgen(has_pop=True, population=sua_populacao, 
                                fit_func=[sua_funcao_fitness], 
                                fun=ope, parm=ope_par, outros_parâmentros)
```
### Número de gerações
Para finalizar, basta apenas informar o número de gerações para o programa:
```python
egg = egg.evolgen(has_pop=True, population=sua_populacao, 
                                fit_func=[sua_funcao_fitness], 
                                fun=ope, parm=ope_par, generations=1000)
```

Agora você pode executar o seu programa. Se ainda possui alguma dúvida, dê uma olhada nos exemplos abaixo e sinta-se livre para perguntar.
