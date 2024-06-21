# DHuolib um produto do DHuo.data

Dhuolib é uma biblioteca projetada para gerenciar o ciclo de vida de modelos de machine learning de forma rápida e eficaz. Com a Dhuolib, é possível implementar e gerenciar ciclos de deploy, controle de versões e gerenciamento de modelos em predição de maneira simples e intuitiva. Este documento tem como objetivo demonstrar essas funcionalidades, facilitando o uso da ferramenta e potencializando sua eficiência.

**==versão: 0.5.1==**

<https://pypi.org/project/dhuodata-lib/>


 ![](assets/imgs/dhuo.png)

# Funcionalidades 

Nesta sessão serão abordadas as principais funcionalidades presentes na dhuolib 

### **Login Não implementado**

* [x] login
  * Auth.login
  * Auth.is_logged

## **Análise Exploratória / Persistencia / Aquisição de Dados**

A análise exploratória de dados envolve a persistência e aquisição de dados de forma eficiente. Utiliza métodos para inserção direta de dados, atualização de tabelas com DataFrames, recuperação paginada de registros e conversão de resultados em DataFrames, facilitando o trabalho dos desenvolvedores na predição de modelos de machine learning.

## **Class: GenericRepository**

A classe GenericRepository Simplifica o uso e o acesso ao datalake. Possui diversos métodos, incluindo inserção e busca de dados. Seu objetivo é facilitar o trabalho dos desenvolvedores no processo de predição de modelos de machine learning, fornecendo uma interface simplificada para a interação com os dados.

### **__init__(self, db_connection)**

O repositorio é iniciado passando uma conexão com o banco de dados como parametro no construtor

* **Parameters:**
  * **db_connection**: Uma instancia do DatabaseConnection que prove a connecção e controle de acesso com o datalake

### **create_table_by_dataframe(self, table_name: str, df: pd.DataFrame)**

Cria uma tabela baseada em um dataframe existente

* **Parameters:**
  * **table_name**: Nome da tabela onde o dado sera inserido.
  * **dataframe**: Um dataframe representando a tabela e os dados a serem inseridos
* **Returns:**
  * Retorna o numero de itens inseridos na tabela

**Example:**

```python
df = pd.DataFrame({"name": ["example"], "value": [42]})
number_lines = repo.create_table_by_dataframe("my_table", data)
```

### **insert(self, table_name: str, data: dict)**

Insere um novo dado na base de dados. Uma boa opção para inserir dados no database sem utilizar dataframe pandas

* **Parameters:**
  * **table_name**: Nome da tabela onde o dado sera inserido.
  * **data**: Um dicionario representando o dado a ser inserido.
* **Returns:**
  * Retorna o dado inserido.
* **Example:**

  ```python
  data = {"name": "example", "value": 42}
  inserted_record = repo.insert("my_table", data)
  ```

### **update_table_by_dataframe(self, table_name: str, df_predict: pd.DataFrame, if_exists: str = "append", is_update_version: bool)**

Atualiza uma tabela adicionando ou substituindo registros usando um DataFrame do pandas.

* **Parâmetros:**
* **table_name**: O nome da tabela a ser atualizada.
* **df_predict**: Um DataFrame do pandas contendo os registros a serem inseridos.
* **if_exists**: Especifica o comportamento se a tabela já existir. O padrão é "append".
* **is_update_version:** Faz update  da versão do dado a ser inderido na tabela que vai receber o resultado da predição . A table precisa ter três colunas  ==PREDICT, CREATED_AT e VERSION.==
* **Example:**

  ```python
  df = pd.DataFrame({"name": ["example"], "value": [42]})
  repo.update_table_by_dataframe("my_table", df)
  ```

### **get_items_with_pagination(self, table_name: str, page: int = 1, page_size: int = 10000)**

Recupera registros da tabela especificada utilizando paginação.

* **Parâmetros:**
  * **table_name**: O nome da tabela a ser consultada.
  * **page**: O número da página a ser recuperada. O padrão é 1.
  * **page_size**: O número de registros por página. O padrão é 10000.
* **Retorna:**
  * Um dicionário contendo os registros, número da página, tamanho da página e total de itens.
* **Exemplo:**

  ```python
  result = repo.get_items_with_pagination("my_table", page=1, page_size=10)
  ```

**to_dataframe(self, table_name: str = None, filter_clause: str = None, list_columns: list = None)**

Converte os resultados da consulta em um DataFrame do pandas.

* **Parâmetros:**
  * **table_name**: O nome da tabela a ser consultada.
  * **filter_clause**: Uma cláusula de filtro opcional para aplicar à consulta.
  * **list_columns**: Uma lista opcional de colunas a serem incluídas na consulta.
* **Retorna:**
  * Um DataFrame do pandas contendo os resultados da consulta.
* **Exemplo:**

  ```python
  df = repo.to_dataframe("my_table", filter_clause="value > 10", list_columns=["name", "value"])
  ```

### **Criação de Experimentos, Ciclo de vida do modelo e Predição**

## **Class: DhuolibExperimentClient**

DhuolibExperimentClient  interage com o serviço Dhuolib para gerenciar experimentos, executar modelos, criar modelos e fazer previsões. Inclui métodos para criar e executar experimentos, criar modelos e fazer previsões em lote.

### **__init__(self, service_endpoint=None)**

Inicializa o cliente com um endpoint de serviço.

* **Parâmetros:**
  * service_endpoint: O endpoint do serviço Dhuolib.
* **Lança:**
  * ValueError: Se service_endpoint não for fornecido.

### **create_experiment(self, experiment_name: str, experiment_tags: dict = None) -> dict**

Cria um novo experimento com o nome e tags especificados.

* **Parâmetros:**
  * **experiment_name**: O nome do experimento.
  * **experiment_tags**: Dicionário opcional de tags para o experimento.
* **Retorna:**
  * Um dicionário contendo os detalhes do experimento criado ou uma mensagem de erro.

**Exemplo:**

```python
experiment_response = dholib_client.create_experiment(
        experiment_name="iris-classification", experiment_tags={"tag": "iris"}
    )
```

### **run_experiment(self, type_model: str, experiment_id: str, modelpkl_path: str, requirements_path) -> dict**

Executa um experimento com o modelo e requisitos especificados.

* **Parâmetros:**
  * **type_model**: O tipo do modelo.
  * **experiment_id**: O ID do experimento.
  * **modelpkl_path**: O caminho para o arquivo pickle do modelo.
  * **requirements_path**: O caminho para o arquivo de requisitos.
* **Retorna:**
  * Um dicionário contendo os detalhes da resposta ou uma mensagem de erro.
* **Exemplo:**

  ```python
  experiment_run = dholib_client.run_experiment(
          type_model="lightgbm",
          experiment_id=experiment_response["experiment_id"],
          modelpkl_path="{path}/iris.pkl",
          requirements_path="{path}/requirements.txt",
      )
  ```

### **create_model(self, model_params) -> dict**

Cria um novo modelo com os parâmetros especificados.

* **Parâmetros:**
  * **model_params**: Um dicionário contendo os parâmetros do modelo.
* **Retorna:**
  * Um dicionário contendo os detalhes do modelo criado ou uma mensagem de erro.

**Exemplo:**

```python
run_params = {
        "modelname": "iris-classification",
        "modeltag": "lightgbm",
        "stage": "Production",
        "run_id": experiment_run["run_id"],
        "model_uri": experiment_run["model_uri"],
    }
result = dholib_client.create_model(run_params)
```

### **prediction_batch_with_dataframe(self, batch_params: dict, df: pd.DataFrame) -> dict**

Faz uma previsão em lote usando um DataFrame do pandas.

* **Parâmetros:**
  * batch_params: Um dicionário contendo os parâmetros da previsão em lote.
  * df: Um DataFrame do pandas contendo os dados para a previsão.
* **Retorna:**
  * Um dicionário contendo os resultados da previsão em lote ou uma mensagem de erro.

**Exemplo:**

```python
batch_params = {
        "modelname": "iris-classification-lightgbm",
        "stage": "Production",
        "experiment_name": "iris-classification",
        "type_model": "lightgbm",
        "run_id": "121",
        "batch_model_dir": "iris.pkl",
}
response = client.prediction_batch_with_dataframe(batch_params, dataframe)
```

## **Exemplo de Uso**

```python
dholib_client = DhuolibExperimentClient(
        service_endpoint="http://localhost:8000")
repository = get_repository(
        config_file_name="/home/diego/Documentos/eng/test-dhuodata/config/database.json"
)
df_iris_train = repository.to_dataframe(table_name="IRIS_TRAIN")

X = df_iris_train[["sepal_length", "sepal_width",
                       "petal_length", "petal_width"]]
y = df_iris_train["class"]
clf = lgb.LGBMClassifier()
clf.fit(X, y)
with open("iris.pkl", "wb") as f:
    pickle.dump(clf, f)

experiment_response = dholib_client.create_experiment(
    experiment_name="iris-classification", experiment_tags={"tag": "iris"}
)

experiment_run = dholib_client.run_experiment(
    type_model="lightgbm",
    experiment_id=experiment_response["experiment_id"],
    modelpkl_path="{path}/iris.pkl",
     requirements_path="{path}/requirements.txt",
  )
 print(experiment_run)
 run_params = {
        "modelname": "iris-classification",
        "modeltag": "lightgbm",
        "stage": "Production",
        "run_id": experiment_run["run_id"],
        "model_uri": experiment_run["model_uri"],
  }
 
 df_iris = repository.to_dataframe(
        table_name="IRIS_FEATURE",
        list_columns=["SEPAL_LENGTH", "SEPAL_WIDTH",
                      "PETAL_LENGTH", "PETAL_WIDTH"],
)

 result = dholib_client.create_model(run_params)
 predicts = dholib_client.prediction_batch_with_dataframe(
        batch_params=batch_params, df=df_iris
    )
 df_iris["predict"] = predicts
```

## **Class: DhuolibPlatformClient**

DhuolibPlatformClient interage com o serviço Dhuolib para gerenciar projetos em lote, implantar scripts, verificar o status do pipeline, criar clusters e executar pipelines em lote.

### **__init__(self, service_endpoint=None, project_name=None)**

Inicializa o cliente com um endpoint de serviço e um nome de projeto opcional.

* **Parâmetros:**
  * service_endpoint: O endpoint do serviço Dhuolib.
  * project_name: Nome opcional do projeto.
* **Lança:**
  * ValueError:  Se o projeto já existir.
  * ConnectionError: Se houver um erro de conexão.

### **create_batch_project(self, project_name: str)**

Cria um novo projeto em lote com o nome especificado.

* **Parâmetros:**
  * `project_name`: O nome do projeto.
* **Retorna:**
  * Um dicionário contendo os detalhes do projeto criado ou uma mensagem de erro.
* **Lança:**
  * `ValueError`: Se o projeto já existir.
  * `ConnectionError`: Se houver um erro de conexão.
* **Exemplo:**

  ```python
  response = dholib_platform.create_batch_project("MeuProjeto")
  ```

### **deploy_batch_project(self, script_filename: str, requirements_filename: str)**

Implanta um projeto em lote com o script e requisitos especificados.

* **Parâmetros:**
  * **script_filename**: O nome do arquivo do script.
  * **requirements_filename**: O nome do arquivo de requisitos.
* **Retorna:**
  * A resposta do serviço Dhuolib ou uma mensagem de erro.
* **Lança:**
  * ValueError: Se project_name, script_filename ou requirements_filename não foram fornecidos
  * FileNotFoundError: Se os arquivos especificados não forem encontrados.

**Exemplo:**

```python
 response = dholib_platform.deploy_batch_project(
        script_filename="{path}/script.py",
        requirements_filename="{path}/requirements.txt"
    )
```

### **pipeline_status_report(self)**

Gera um relatório de status do pipeline para o projeto em lote.

* **Retorna:**
  * Uma lista de dicionários contendo a data, etapa e status de cada log do pipeline.
* **Lança:**
  * ValueError: Se project_name não for fornecido
* **Exemplo:**

  ```python
  status_report = dholib_platform.pipeline_status_report()
  ```

### **create_cluster(self, cluster_size: int)**

Cria um cluster com o tamanho especificado para o projeto em lote.

* **Parâmetros:**
  * cluster_size: O tamanho do cluster (1, 2 ou 3).
* **Retorna:**
  * A resposta do serviço Dhuolib.
* **Lança:**
  * ValueError: Se project_name ou cluster_size não forem fornecidos ou se cluster_size não for 1, 2 ou 3.
* **Exemplo:**

  ```python
  response = dholib_platform.create_cluster(2)
  ```

### **batch_run(self)**

Executa o pipeline em lote para o projeto.

* **Retorna:**
  * A resposta do serviço Dhuolib.
* **Lança:**
  * ValueError: Se project_name não for fornecido.
* **Exemplo:**

  ```python
  response = dholib_platform.batch_run()
  ```

## **Exemplo de Uso**

```python
dholib_platform = DhuolibPlatformClient(
        service_endpoint="http://{server}",
        project_name="{pŕoject_name}")

response_create_cluster = dholib_platform.create_cluster(1)    
response_batch_run = dholib_platform.batch_run()
```


# **Demonstração da Aplicação**

## **Projeto Iris-t com lightgbm**


 ![](assets/imgs/iris.jpeg)


Para utilizar o Dhuolib para predição em batch usando o Data Lake, é necessário ter duas fontes de dados. A primeira fonte contém as features com os valores para treinamento e a segunda fonte contém os valores que serão usados para a inferência. Exemplos dessas fontes podem ser as tabelas: IRIS_TRAIN para treinamento e IRIS_DATA_FOR_INFERENCY para inferência.

Os dados para inferência e os dados de treinamento podem ser substituídos por DataFrames pandas obtidos de outras fontes. Ao salvar os dados no Data Lake, é importante ter em mente que a tabela deve conter, no mínimo, três colunas obrigatórias: ==PREDICT, CREATED_AT e VERSION.==

```sql
CREATE TABLE "DHUODATA"."IRIS_OUTPUT" 
   (
    "SEPAL_LENGTH" NUMBER, 
	"SEPAL_WIDTH" NUMBER, 
	"PETAL_LENGTH" NUMBER, 
	"PETAL_WIDTH" NUMBER, 
	"PREDICT" NUMBER(*,0), 
	"VERSION" NUMBER(*,0), 
	"CREATED_AT" TIMESTAMP (6)
   );
```

### Exemplo de Colunas Necessárias:

* **==PREDICT:==** Coluna que armazenará as previsões geradas pelo modelo.
* **==CREATED_AT==:** Coluna que registrará a data e hora em que a previsão foi feita.
* **==VERSION:==** Coluna que indicará a versão do modelo utilizado para a previsão.

Ao garantir que essas colunas estejam presentes, você assegura a integridade e a rastreabilidade dos dados no Data Lake, facilitando o monitoramento e a manutenção do pipeline de predição.

#### **Na primeira etapa é importante criar o código de treino para gerar o pickle**

#### **Apos o pickle ser gerado é necessário cadastrar o pickle**

* **dholib_client.create_experiment** - crie o experimento
* **dholib_client.run_experiment** - execute o experimento logando ele no nosso sistema
* **dholib_client.create_model** - crie o modelo. O modelo uma vez criado é apto para ser posto em produção. O modelo pode ter 4 estados None, Production, Stagging ou Archive
  * **None**: Este é o estado padrão de um modelo quando ele é registrado pela primeira vez. Ele indica que o modelo ainda não foi atribuído a nenhum dos outros estados.
  * **Staging**: Este estado é usado para modelos que estão em um ambiente de teste. Eles foram testados em um ambiente isolado e estão prontos para serem movidos para produção.
  * **Production**: Este estado é usado para modelos que estão atualmente em uso em um ambiente de produção.
  * **Archived**: Este estado é usado para modelos que não estão mais em uso. Eles são mantidos para fins de registro e não devem ser usados para inferência.

## **Treino:**

```python
import pickle
import lightgbm as lgb

from dhuolib.clients.experiment import DhuolibExperimentClient
from dhuolib.repository import DatabaseConnection, GenericRepository


def get_repository(config_file_name):
    if not config_file_name:
        raise ValueError("config_file_name is required")

    db = DatabaseConnection(config_file_name=config_file_name)
    repository = GenericRepository(db_connection=db)

    return repository


def train():
    dholib_client = DhuolibExperimentClient(
        service_endpoint="http://{uri_endpoint}")
    repository = get_repository(
        config_file_name="{path}/database.json"
    )
    df_iris_train = repository.to_dataframe(table_name="IRIS_TRAIN")

    X = df_iris_train[["sepal_length", "sepal_width",
                       "petal_length", "petal_width"]]
    y = df_iris_train["class"]
    clf = lgb.LGBMClassifier()
    clf.fit(X, y)
    with open("{path}/iris.pkl", "wb") as f:
        pickle.dump(clf, f)

    experiment_response = dholib_client.create_experiment(
        experiment_name="iris-classification", experiment_tags={"tag": "iris"}
    )

    experiment_run = dholib_client.run_experiment(
        type_model="lightgbm",
        experiment_id=experiment_response["experiment_id"],
        modelpkl_path="{path}/iris.pkl",
        requirements_path="{path}/requirements.txt",
    )
    print(experiment_run)
    run_params = {
        "modelname": "iris-classification",
        "modeltag": "lightgbm",
        "stage": "Production",
        "run_id": experiment_run["run_id"],
        "model_uri": experiment_run["model_uri"],
    }
    result = dholib_client.create_model(run_params)
    print(result)


if __name__ == "__main__":
    train()
```


## **Inferência**

#### **Esse é o script de predição. Para que o fluxo em lote seja executado é necessario fazer um deploy desse arquivo junto com o requirements na dhuolib. Ao fazer isso o script estará disponivel para o processamento em batch.**

Obs: O nome deve ser sempre script.py

```python
from dhuolib.clients.experiment import DhuolibExperimentClient
from dhuolib.repository import DatabaseConnection, GenericRepository


def get_repository(config_file_name):
    if not config_file_name:
        raise ValueError("config_file_name is required")

    db = DatabaseConnection(config_file_name=config_file_name)
    repository = GenericRepository(db_connection=db)

    return repository

def predict():
    dholib_client = DhuolibExperimentClient(
        service_endpoint="http://{uri_endpoint}")
    repository = get_repository(
        config_file_name="{path}/database.json"
    )
    df_iris = repository.to_dataframe(
        table_name="IRIS_FEATURE",
        list_columns=["SEPAL_LENGTH", "SEPAL_WIDTH",
                      "PETAL_LENGTH", "PETAL_WIDTH"],
    )

    print(df_iris.head(10))

    batch_params = {
        "modelname": "iris-classification-lightgbm",
        "stage": "Production",
        "experiment_name": "iris-classification",
        "type_model": "lightgbm",
        "run_id": "",
        "batch_model_dir": "iris.pkl",
    }
    predicts = dholib_client.prediction_batch_with_dataframe(
        batch_params=batch_params, df=df_iris
    )
    df_iris["predict"] = predicts
    repository.update_table_by_dataframe(
        table_name="IRIS_OUTPUT", df_predict=df_iris)


if __name__ == "__main__":
    predict()
```

## **Fazendo o deploy e executando a solução**

* **dholib_platform.create_batch_project** - Crie o projeto
* **dholib_platform.deploy_batch_project** - Faça o deploy do projeto. Lembre de passar o caminho do script e o caminho do requirements
* **dholib_platform.pipeline_status_report** - Verifique os status da execução

```python

from dhuolib.clients.platform import DhuolibPlatformClient

def deploy():
    dholib_platform = DhuolibPlatformClient(
        service_endpoint="http://{endpoint}")
    dholib_platform.create_batch_project('iris-classification-lightgbm-1')
    response = dholib_platform.deploy_batch_project(
        script_filename="{path}/script.py",
        requirements_filename="{path}/requirements.txt"
    )
    print(dholib_platform.pipeline_status_report())


if __name__ == "__main__":
    deploy()
```

### **Executando o projeto remotamente**

* **dholib_platform.create_cluster** - Crie o cluster. O cluster possui 3 niveis de capacidade. SMALL(1), MEDIUM(2) ou LARGE(3).
* **dholib_platform.batch_run** - Execute o script do projeto

```python
from dhuolib.clients.platform import DhuolibPlatformClient


def run():
    dholib_platform = DhuolibPlatformClient(
        service_endpoint="http://{uri_endpoint}",
        project_name="{project_name}")

    response_create_cluster = dholib_platform.create_cluster(1)
    response_batch_run = dholib_platform.batch_run()


if __name__ == "__main__":
    run()
```
