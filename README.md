# PROJETO MULHERADA

Crie o ambiente virtual na raiz o projeto
```sh
python3 -m venv env
```

Carregue os módulos do ambiente virtual
```sh
source ./env/bin/activate
```

Instale os pacotes necessários

```sh
pip install -r requirements.txt
```

Para rodar o projeto vá para a pasta raiz e digite o comando abaixo:

```sh
python3 manage.py runserver
```

Acesse o link: http://localhost:8000

Ná pagina principal digite uma profissão, uma localização, ou ambos e depois clique em pesquisar.

Exemplo: digite `dev` no campo **profissão** e clique no botão **pesquisar**