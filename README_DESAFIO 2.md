# DESAFIO 2
# Como subir e Testar a API

## O ARQUIVO 'server.py' É REFERENTE AO DESAFIO 2

 * Inicializando a api:

    a api foi construída utilizando o FastAPI por isso para inicializar o servidor você irá precisar utilizar o comando:
   * ```
     uvicorn server:app --reload
     ```
     
     * ou

    * ```
      python -m uvicorn server:app --reload
      ```

 ## 1º requisição: ESTUDANTES PO CURSO:
   após a api estiver rodando existe alguns parâmetros para se utilizar
 * http://127.0.0.1:8000/students/ascendente (localhost/students/ascendente) que vai mostrar os alunos listados de maneira crescente baseado no campo 'grade'

 * http://127.0.0.1:8000/students/descendente (localhost/students/descendente) mostraos alunos listados de maneira decrescente baseado no campo Grade

 as duas requisições acima correspondem ao primeiro critério do desafio 2, 1.Listagem de estudantes por curso incluindo filtros por nota do curso

## 2º requisição: API PARA RELATORIO CONTENDO TOP 5 ESTUDANTES 

api para relatorio contendo top 5 estudantes, para listar o top 5 estudantes utilizei o campo "ranking" do banco de dados 
para usar essa requisição acesse: http://127.0.0.1:8000/relatorio/aluno  (localhost/relatorio/aluno)

## 3º requisição: PROFESSORES POR POPULARIDADE
Api que mostra os professores listados por popularidade, para usar essa api acesse http://127.0.0.1:8000/relatorio/professor  (localhost/relatorio/professor)

## 4º requisição: QUANTIDADE DE ALUNOS POR CURSO
api que mostra a quantidade de alunos em cada curso, para usar essa API acesse: http://127.0.0.1:8000/relatorio/curso (localhost/relatorio/curso)

# TECNOLOGIAS

para fazer esse projeto usei o pewee para criar a camada de acesso ao banco de dados e o pandas para manipular os dados
