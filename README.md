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



Para isso, eu criei algumas regras na hora da criação dos operadores 
