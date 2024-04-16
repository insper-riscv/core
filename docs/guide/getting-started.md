# Começando

## Dependências

### Visual Studio Code

::: danger TO DO

Sobre o VS Code

:::

#### Instalação

::: danger TO DO

Instalando o VS Code

:::

### Docker

Docker é uma plataforma de código aberto que permite a criação, implantação e
execução de aplicativos em contêineres. Os contêineres são como máquinas
virtuais leves que permitem que os desenvolvedores embalem e distribuam
facilmente seus aplicativos junto com todas as dependências necessárias. Isso
garante que o aplicativo funcione de forma consistente em qualquer ambiente,
independentemente de diferenças entre sistemas operacionais ou configurações.
Docker permite aos desenvolvedores aumentar a eficiência do desenvolvimento,
teste e implantação de aplicativos, além de facilitar a escalabilidade e
gerenciamento de aplicativos. Ele também fornece um ecossistema de ferramentas
para gerenciamento de contêineres e clusters, incluindo o Docker Compose e o
Docker Swarm.

#### Instalação

Existem várias maneiras de instalar o Docker, mas aqui está uma forma geral de
fazê-lo:

::: warning Windows

Caso você esteja utilizando o Windows, é preciso primeiro estar com o sistema
atualizado, instalar o WSL 2 e uma distribuição linux para ele. Recomendamos
seguir o tutorial oficial e instalar o Ubuntu 22.04 LTS.

:::

1. Baixe o instalador do Docker para o seu sistema operacional a partir do
   [site oficial do Docker](https://www.docker.com/get-started). Certifique-se
   de baixar a versão mais recente e compatível com o seu sistema operacional.
2. Execute o instalador baixado. Siga as instruções na tela para instalar o
   Docker em seu sistema. Certifique-se de selecionar as opções de instalação
   padrão. Verifique se a instalação foi bem-sucedida executando o seguinte
   comando no seu prompt de comando. Se a instalação foi bem-sucedida, você verá
   a versão do Docker instalada.

```sh
docker -v
```

::: danger Dica

Dependendo do seu sistema operacional, alguns passos podem variar. Alguns
sistemas operacionais precisam de configurações adicionais, como habilitar
virtualização no BIOS, e alguns usuários precisam adicionar sua conta ao grupo
"docker" para poder usar o docker sem precisar usar "sudo".

:::

## Iniciando o ambiente

::: danger **Para usuários Linux**

Antes de iniciar o ambiente, caso esteja utilizando o **Ubuntu** e possivelmente outras distros Linux, 
é necessário adicionar o caminho `/run` em **Settings** > **Resources** > **File Sharing** e clique em **Apply & Restart**. 
Caso não faça isso, é provável que o ambiente não inicie pois o Docker não terá permissão para acessar o diretório.

![Docker Config](/images/docker_config.png)  

:::

::: danger TO DO

Explicação

:::
