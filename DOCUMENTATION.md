# 📚 Documentação ClimaBR-hp

## 🗂️ Índice de Documentação

### 📖 Documentos Principais

| Documento | Descrição | Para Quem |
|-----------|-----------|-----------|
| **README.md** | Visão geral do projeto, arquitetura, como usar | Todos |
| **FIX_CODEBUILD_ERROR.md** | Solução rápida para erros de permissão AWS | Quem tem erro no CodeBuild |
| **AWS_CODEBUILD_SETUP.md** | Guia completo de configuração AWS | DevOps / Arquitetos |
| **DOCUMENTATION.md** | Este arquivo - índice de docs | Todos |

---

## 🎯 Fluxos de Uso

### 👨‍💻 Você é um desenvolvedor querendo usar o projeto

1. Leia: **README.md** (Overview)
2. Siga: "Como Usar" → "Instalação"
3. Execute: `dbt run` e `dbt docs serve`

### ⚙️ Você está configurando CodeBuild pela primeira vez

1. Leia: **FIX_CODEBUILD_ERROR.md** (Solução rápida)
2. Se precisar mais detalhes: **AWS_CODEBUILD_SETUP.md**
3. Configure permissões IAM conforme indicado

### 🐛 Você tem um erro no CodeBuild

1. Vá para: **README.md** → "Troubleshooting"
2. Se for permissão: **FIX_CODEBUILD_ERROR.md**
3. Se for configuração: **AWS_CODEBUILD_SETUP.md**

### 📚 Você quer entender a arquitetura completa

1. **README.md** → "Arquitetura da Solução"
2. **README.md** → "Pipeline CI/CD com AWS CodeBuild"
3. **AWS_CODEBUILD_SETUP.md** → "Fluxo de Resolução"

---

## 📋 Estrutura do Projeto

```
projeto-dbt-aws/climabr/
├── README.md                      # ⭐ COMECE AQUI
├── DOCUMENTATION.md               # Este arquivo
├── FIX_CODEBUILD_ERROR.md        # Solução rápida (erro IAM)
├── AWS_CODEBUILD_SETUP.md        # Guia completo AWS
├── buildspec.yml                 # Configuração CodeBuild
├── dbt_project.yml              # Configuração dbt
├── models/
│   ├── staging/
│   │   ├── stg_clima.sql        # Dados brutos
│   │   └── schema.yml           # Validações
│   ├── intermediate/
│   │   ├── int_clima_diario.sql # Transformações
│   │   └── schema.yml
│   └── marts/
│       ├── fct_analise_mensal.sql
│       ├── fct_desvio_previsao.sql
│       └── schema.yml
├── tests/                        # Testes customizados
├── macros/
│   ├── generate_schema_name.sql
│   ├── classify_moon_phase.sql
│   └── schema.yml
└── target/
    ├── catalog.json              # Documentação auto-gerada
    ├── manifest.json             # Manifesto dbt
    └── index.html                # Website documentação
```

---

## 🔍 Referência Rápida de Comandos

### Local Development
```bash
# Instalar dependências
dbt deps

# Testar conexão
dbt debug

# Executar transformações
dbt run

# Rodar testes
dbt test

# Gerar documentação
dbt docs generate

# Ver documentação no navegador
dbt docs serve
```

### CodeBuild (Automático)
```
GitHub push → CodeBuild automatic trigger → Athena execution → S3 docs publish
```

---

## 🚀 Principais Tecnologias

| Tecnologia | Versão | Função |
|-----------|--------|--------|
| **dbt** | 1.11.7 | Transformação de dados |
| **Python** | 3.13 | Runtime do CodeBuild |
| **Athena** | - | SQL serverless |
| **S3** | - | Data Lake |
| **Glue Catalog** | - | Metadados |
| **CodeBuild** | - | CI/CD |

---

## 📊 Modelos de Dados

### Staging Layer
- **stg_clima**: Dados brutos com validações

### Intermediate Layer
- **int_clima_diario**: Enriquecimento com métricas

### Mart Layer
- **fct_analise_mensal**: Análises agregadas mensais
- **fct_desvio_previsao**: Comparação previsão vs observado

---

## ✅ Checklist de Configuração

- [ ] Repository clonado localmente
- [ ] `.venv` criado e ativado
- [ ] `pip install -r requirements.txt` executado
- [ ] AWS credentials configuradas (`aws configure`)
- [ ] `dbt debug` funcionando
- [ ] GitHub conta conectada
- [ ] CodeBuild projeto criado
- [ ] IAM role com permissões (athena, glue, s3)
- [ ] Variáveis de ambiente no CodeBuild configuradas
- [ ] Primeiro build executado com sucesso
- [ ] Documentação publicada em www.cimabrhp.com

---

## 🔗 Links Úteis

### Documentação Oficial
- [dbt Documentation](https://docs.getdbt.com)
- [AWS Athena](https://docs.aws.amazon.com/athena)
- [AWS CodeBuild](https://docs.aws.amazon.com/codebuild)
- [AWS Glue](https://docs.aws.amazon.com/glue)

### Este Projeto
- **GitHub:** https://github.com/HELIOJR/ClimaBR-hp
- **Website Docs:** https://www.cimabrhp.com
- **Email:** heliopaiva@gmail.com

---

## 🆘 Precisa de Ajuda?

1. **Erro técnico?** → Veja Troubleshooting no README.md
2. **Erro IAM?** → Abra FIX_CODEBUILD_ERROR.md
3. **Configuração?** → Consulte AWS_CODEBUILD_SETUP.md
4. **dbt?** → [docs.getdbt.com](https://docs.getdbt.com)
5. **AWS?** → Abra um ticket no AWS Support

---

## 📝 Histórico de Mudanças

### v1.0 - 2026-04-27
- ✅ Setup inicial de documentação
- ✅ Guias de troubleshooting criados
- ✅ buildspec.yml melhorado
- ✅ README com arquitetura completa

---

## 👨‍💼 Autor

**Hélio Paiva**
- 📧 heliopaiva@gmail.com
- 🔗 GitHub: @HELIOJR
- 💼 LinkedIn: [Hélio Paiva](https://linkedin.com/in/helio-paiva)

---

<div align="center">

**Documentação do Projeto ClimaBR-hp**

Desenvolvido com ❤️ para o Programa de Pós-Graduação em Engenharia de Dados

</div>
