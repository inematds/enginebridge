# Pedido para adaptar outro sistema

Copie o texto abaixo e substitua os campos entre colchetes.

```text
Adapte o sistema [nome e caminho do projeto] para provedores independentes por etapa,
seguindo a referência em /home/nmaldaner/projetos/wifi/provedores-independentes/.

Leia primeiro as regras e a documentação do projeto. Mapeie todas as chamadas de IA,
inclusive filtros, revisores, consultas de agenda e outros scripts indiretos.

Quero uma configuração própria do projeto, com tipo, motor, modelo e esforço por etapa.
Deixe as opções de assinatura Claude, assinatura Codex, API Anthropic, API OpenAI e
API OpenRouter explicadas com comentários # no próprio arquivo, para eu mudar depois
sem editar código. O comando de configuração deve preservar esses comentários.

Use os scripts para arquivos, validação, tentativas e publicação. Padronize a resposta
dos modelos e mantenha os validadores, travas, horários e retomada do sistema.

As imagens devem [continuar no motor atual / usar o motor indicado aqui].
Mapeie as capacidades necessárias por etapa. Não presuma que uma API de texto tem
shell, geração de imagem ou os conectores MCP do CLI. Documente as dependências
que continuarem presas a um provedor e o trabalho necessário para removê-las.

Use somente as autorizações que eu já dei para este serviço, finalidade e projeto.
Não copie a autorização do gitbombando. Na ausência de autorização, deixe APIs
desativadas e faça somente testes locais independentes. CLI Claude/Codex continua
pela assinatura; APIs diretas são adaptadores separados.

Faça testes sem rede e preserve os validadores reais do projeto. Testes reais de API
exigem autorização explícita válida. Use pastas isoladas, sem publicar nem gerar
mídia para testar apenas uma etapa de texto. Registre quais motores foram testados
com chamada real, quais foram apenas simulados e o que continua limitado.

O projeto deve passar a usar a configuração na próxima chamada de cada etapa,
sem depender da seleção de modelo/esforço do meu terminal. Não faça fallback
silencioso da assinatura para uma API paga.
```

Se quiser autorizar um teste de API, acrescente uma frase específica com serviço, tarefa e limite desejado. Para operação diária, registre também esse escopo. Pedir adaptação ou copiar esta referência não autoriza por si só o consumo de qualquer API.
