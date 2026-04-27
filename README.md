# ClimaBR-hp

<div align="center">

![Badge](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![Badge](https://img.shields.io/badge/dbt-1.11.7-ff6b35?style=flat-square&logo=dbt)
![Badge](https://img.shields.io/badge/AWS-Athena-FF9900?style=flat-square&logo=amazon-aws)
![Badge](https://img.shields.io/badge/CI%2FCD-CodeBuild-FF9900?style=flat-square&logo=amazon-aws)
![Badge](https://img.shields.io/badge/Data%20Pipeline-ETL-009688?style=flat-square)
![Badge](https://img.shields.io/badge/License-MIT-green?style=flat-square)

**Um pipeline de dados moderno para análise de dados meteorológicos brasileiros utilizando AWS, DBT e práticas de engenharia de dados**

[GitHub](https://github.com/HELIOJR/ClimaBR-hp) • [📚 Documentação ao Vivo](https://s3.us-east-1.amazonaws.com/www.cimabrhp.com/docs/index.html) • [Portfólio](https://heliopaiva.dev) • [LinkedIn](https://linkedin.com/in/helio-paiva)

</div>

---

## 📋 Sobre o Projeto

O **ClimaBR-hp** é um pipeline de engenharia de dados completo que demonstra as melhores práticas de construção de soluções escaláveis na nuvem. O projeto extrai, transforma e analisa dados meteorológicos de cidades brasileiras, realizando análises complexas sobre clima, tendências e anomalias.

Este projeto foi desenvolvido como parte do **Programa de Pós-Graduação em Engenharia de Dados** na Anhanguera e serve como um portfólio técnico demonstrando:

- ✅ Integração cloud-native com AWS
- ✅ Transformação de dados com DBT (Data Build Tool)
- ✅ Testes de qualidade de dados
- ✅ Documentação automática e catalogo de dados
- ✅ Modelagem dimensional (staging, intermediate, marts)

---

## 🏗️ Arquitetura da Solução

```
┌─────────────────────────────────────────────────────────────┐
│                    FONTE DE DADOS (APIs)                    │
│              Previsões meteorológicas brasileiras             │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  EXTRAÇÃO (Python/API)                       │
│            → Raw data → S3 (Raw Layer)                       │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  AWS S3 + Athena                             │
│     (Data Lake com tabelas estruturadas em formato JSON)     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              TRANSFORMAÇÃO (DBT - This Repository)           │
│  • Staging:      Limpeza e validação dos dados brutos       │
│  • Intermediate: Enriquecimento e cálculos derivados        │
│  • Marts:        Análises agregadas para stakeholders       │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              OUTPUTS (Athena / Documentação)                 │
│  • Tabelas analíticas prontas para BI/análise              │
│  • Documentação automática (dbt docs)                       │
│  • Data Lineage e testes de qualidade                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Stack Tecnológico

| Categoria | Tecnologia | Descrição |
|-----------|-----------|-----------|
| **Cloud Platform** | AWS (S3, Athena, Glue) | Data Lake escalável e serverless |
| **Transformação** | dbt 1.11.7 | Orquestração de modelos SQL |
| **Banco de Dados** | Amazon Athena | SQL interativo sobre S3 |
| **Catalog** | AWS Glue | Metadados e schema discovery |
| **CI/CD** | AWS CodeBuild | Build e deploy automatizado |
| **Linguagem** | SQL + Python | Transformações e testes |
| **Versionamento** | Git | Controle de código |
| **Repositório** | GitHub | Integração com CodeBuild |
| **IDE** | VSCode | Desenvolvimento local |
| **Qualidade** | dbt Tests | Validação automática de dados |

---

## ☁️ Serviços AWS Utilizados

### **Amazon S3 (Simple Storage Service)**
- **Função:** Data Lake - armazena todos os dados
- **Buckets:**
  - `proj-clima-dbt-hp/dbt/metadados/` - Staging do Athena
  - `proj-clima-dbt-hp/dbt/table/` - Tabelas finais
  - `www.cimabrhp.com` - Documentação estática

### **Amazon Athena**
- **Função:** SQL serverless para transformação de dados
- **Database:** AWS Glue Catalog
- **Threads:** 4 (execução paralela)
- **Integração:** dbt-athena-community

### **AWS Glue**
- **Função:** Data Catalog - metadados e schema
- **Schema:** `landing` (banco de dados)
- **Autodiscovery:** Detecta automaticamente tabelas no S3

### **AWS CodeBuild**
- **Função:** Build e deploy automático
- **Trigger:** GitHub push
- **Runtime:** Python 3.13
- **Fases:** Install → Pre-build → Build → Post-build
- **Artifacts:** Salva documentação gerada

### **CloudFront (Opcional)**
- **Função:** CDN para documentação web
- **Endpoint:** www.cimabrhp.com

---

---

## ⚙️ Arquivos de Configuração Importantes

### **buildspec.yml** 🔑
Arquivo que controla o pipeline CI/CD no CodeBuild.

**Valores que DEVEM ser preenchidos com seus dados reais:**
```yaml
DBT_SCHEMA: landing              # → Seu database Glue
S3_STAGING_DIR: s3://seu-bucket/ # → Seu bucket
S3_DATA_DIR: s3://seu-bucket/    # → Seu bucket
S3_DOCS_DIR: s3://seu-bucket/    # → Seu bucket
AWS_REGION: us-east-1            # → Sua região
```

### **create_profiles.py** 🔐
Script Python que gera `~/.dbt/profiles.yml` automaticamente.
- Não requer credenciais explícitas (usa IAM role)
- Executa automaticamente na fase `pre_build` do CodeBuild

### **dbt_project.yml**
Configuração geral do projeto dbt

---

## 📊 Estrutura do Projeto DBT

```
projeto-dbt-aws/climabr/
├── models/
│   ├── staging/           # Camada de staging - limpeza e validação
│   │   └── stg_clima.sql  # Modelo bruto com dados meteorológicos
│   ├── intermediate/       # Camada intermediária - enriquecimento
│   │   └── int_clima_diario.sql  # Dados com métricas derivadas
│   └── marts/             # Camada de dados analítica
│       ├── fct_analise_mensal.sql      # Análises mensais por cidade
│       └── fct_desvio_previsao.sql     # Desvios de previsão
├── tests/                 # Testes de qualidade de dados
├── macros/                # Macros reutilizáveis
├── dbt_project.yml        # Configuração do projeto
└── README.md             # Este arquivo
```

### 📈 Modelos de Dados

#### **Staging (stg_clima)**
Dados brutos extraídos das APIs meteorológicas com validações básicas:
- Campos meteorológicos: temperatura, umidade, precipitação
- Fase da lua, condições climáticas
- Timestamps de carregamento

#### **Intermediate (int_clima_diario)**
Camada de enriquecimento com cálculos derivados:
- Amplitude térmica (temp_max - temp_min)
- Precipitação esperada (precipitação × probabilidade)
- Horas de sol estimadas

#### **Marts (fct_analise_mensal)**
Análises agregadas por cidade e período:
- Médias mensais de temperatura e umidade
- Dias com chuva
- Condição climática mais frequente

#### **Marts (fct_desvio_previsao)**
Comparação entre dados previstos e observados:
- Desvio de temperatura
- Desvio de precipitação
- Análise de acurácia de previsões

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.10+
- AWS CLI configurado
- Athena com tabelas criadas
- VSCode (recomendado)

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/HELIOJR/ClimaBR-hp.git
cd ClimaBR-hp/climabr

# 2. Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt
dbt deps  # Instala pacotes dbt (dbt_expectations)
```

### Executar Transformações Localmente

```bash
# Executar todos os modelos
dbt run

# Executar com seleção específica
dbt run --select staging
dbt run --select marts

# Executar com tags
dbt run --tags +daily

# Executar apenas testes
dbt test

# Gerar documentação
dbt docs generate
dbt docs serve  # Abre no navegador (localhost:8000)
```

### Deploy Automático com AWS CodeBuild

O pipeline é acionado automaticamente quando você faz push para o GitHub:

```bash
# 1. Faça alterações nos modelos
git add .
git commit -m "feat: add new model or transformation"

# 2. Push para GitHub
git push origin main

# 3. CodeBuild é acionado automaticamente!
#    - Executa dbt run na produção (Athena)
#    - Valida todos os testes
#    - Publica documentação em www.cimabrhp.com
```

**Para monitorar o build:**
1. Vá para AWS Console → CodeBuild
2. Selecione seu projeto
3. Veja o histórico de builds em tempo real

### Configurando CodeBuild (Primeira vez)

#### 1️⃣ Crie um Projeto CodeBuild

1. Vá para **AWS Console** → **CodeBuild** → **Create project**
2. **Project name:** `ClimaBR-hp` (ou similar)
3. **Source:** GitHub
   - Connect your GitHub account
   - Repository: `ClimaBR-hp`
4. **Environment:**
   - Managed image: Ubuntu
   - Runtime: Standard
   - Image: `aws/codebuild/standard:7.0`
   - Runtime versions: Python 3.13
5. **Buildspec:** Use arquivo `buildspec.yml` deste repo
6. **Create**

#### 2️⃣ Configure Permissões IAM (CRÍTICO!)

A role do CodeBuild precisa de permissões para Athena, Glue e S3.

**Passos:**
1. AWS Console → **IAM** → **Roles**
2. Procure: `codebuild-ClimaBR-hp-service-role`
3. Clique em **"Add permissions"** → **"Create inline policy"**
4. **JSON Tab** - Cole isto:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AthenaAccess",
      "Effect": "Allow",
      "Action": [
        "athena:StartQueryExecution",
        "athena:GetQueryExecution",
        "athena:GetQueryResults",
        "athena:StopQueryExecution",
        "athena:GetWorkGroup"
      ],
      "Resource": "*"
    },
    {
      "Sid": "GlueAccess",
      "Effect": "Allow",
      "Action": [
        "glue:GetDatabase",
        "glue:GetTable",
        "glue:GetTables",
        "glue:GetPartitions",
        "glue:CreateTable",
        "glue:UpdateTable"
      ],
      "Resource": "*"
    },
    {
      "Sid": "S3Access",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::proj-clima-dbt-hp",
        "arn:aws:s3:::proj-clima-dbt-hp/*"
      ]
    }
  ]
}
```

5. **Review policy** → Nome: `codebuild-dbt-athena-glue-s3`
6. **Create policy**

#### 3️⃣ Configure buildspec.yml

**Edite o arquivo `buildspec.yml` com seus valores reais:**

```yaml
env:
  variables:
    DBT_DATABASE: awsdatacatalog
    DBT_SCHEMA: seu_database_glue  # ← Seu database
    S3_STAGING_DIR: s3://seu-bucket/dbt/metadados/  # ← Seu bucket
    S3_DATA_DIR: s3://seu-bucket/dbt/table/  # ← Seu bucket
    S3_DOCS_DIR: s3://seu-bucket/docs/  # ← Seu bucket
    AWS_REGION: us-east-1  # ← Sua região
```

**Arquivo `create_profiles.py` é usado para gerar as credenciais de forma segura.**

#### 4️⃣ Conecte ao GitHub

1. No CodeBuild Project → **Source** → **Connect GitHub**
2. Autorize o acesso
3. Selecione o repositório `ClimaBR-hp`
4. **Webhook:** Enable (auto-dispara build no push)

#### 5️⃣ Teste o Build

```bash
git add .
git commit -m "Configure CodeBuild"
git push origin main
```

CodeBuild dispara automaticamente → Veja logs em **Build history**

---

## 📚 Documentação ao Vivo

A documentação dbt é **publicada automaticamente** a cada push para o GitHub:

🔗 **[Acesse a documentação completa aqui](https://s3.us-east-1.amazonaws.com/www.cimabrhp.com/docs/index.html)**

Nela você encontra:
- 🔄 **Data Lineage** - Visualização do fluxo completo de dados
- 📊 **Modelos** - Descrição detalhada de todos os modelos dbt
- 🧪 **Testes** - Resultado de 13 testes de qualidade
- 📈 **Colunas** - Documentação de cada coluna das tabelas
- 🎯 **Macros** - Funções reutilizáveis do projeto

---

## ✅ Testes de Qualidade

O projeto inclui **13 testes de dados** cobrindo:

- **Validação de nulidade**: Campos obrigatórios
- **Range de valores**: Fase da lua entre 0 e 1
- **Valores aceitos**: Fonte de dados válidos (fcst, comb, obs, stats)
- **Unicidade**: Chaves primárias

Executar todos os testes:
```bash
dbt test
```

---

## 📚 Documentação

A documentação é gerada automaticamente via dbt:

```bash
dbt docs generate
dbt docs serve
```

Abre uma interface web com:
- Lineage de dados (DAG)
- Descrição de todos os modelos e colunas
- Testes e resultados
- Tipos de dados

---

## 🎯 Features Principais

- ✅ **Modelagem Dimensional**: Staging → Intermediate → Marts
- ✅ **Data Validation**: 13 testes automatizados
- ✅ **Data Lineage**: Visualização completa do fluxo de dados
- ✅ **Documentação Automática**: Auto-gerada pelo dbt
- ✅ **Incremental Models**: Carregamento eficiente
- ✅ **Macros Reutilizáveis**: `generate_schema_name`, `classify_moon_phase`
- ✅ **Source Definitions**: Rastreamento de fontes de dados
- ✅ **Cloud-Native**: Totalmente integrado com AWS

---

## 📊 Dados

### Fonte
- APIs públicas de previsão meteorológica brasileira
- Cobertura: Cidades brasileiras selecionadas
- Frequência: Atualizações diárias

### Dimensões Analíticas
- **Temporal**: Data, mês, dia da semana
- **Geográfica**: Cidade, região
- **Meteorológica**: Temperatura, umidade, precipitação, vento

---

## 🔄 Pipeline CI/CD com AWS CodeBuild

Este projeto implementa um **pipeline automatizado de CI/CD** que integra GitHub com AWS, garantindo qualidade e deploy contínuo:

```
┌──────────────────────────────────────────────────────────────────┐
│                  LOCAL DEVELOPMENT (VSCode)                      │
│              Desenvolvimento e testes locais                      │
└────────────────────────┬─────────────────────────────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│                     GIT & GITHUB PUSH                            │
│            Código versionado (ClimaBR-hp Repository)             │
└────────────────────────┬─────────────────────────────────────────┘
                         │
        ┌────────────────┴──────────────────┐
        │ buildspec.yml linked to GitHub    │
        └────────────────┬──────────────────┘
                         │
                         ▼
┌──────────────────────────────────────────────────────────────────┐
│               AWS CODEBUILD (Automated Trigger)                  │
│  ├─ INSTALL: Python 3.13 + dbt-athena-community                │
│  ├─ PRE-BUILD: Gera profiles.yml (Athena credentials)           │
│  ├─ BUILD:                                                       │
│  │   ├─ dbt deps    (instala pacotes)                           │
│  │   ├─ dbt debug   (valida conexão)                            │
│  │   ├─ dbt run     (executa transformações no Athena)          │
│  │   ├─ dbt test    (valida qualidade dos dados)                │
│  │   └─ dbt docs    (gera documentação)                         │
│  └─ POST-BUILD: Upload para S3                                  │
└────────────────┬───────────────────────────────────────────────┘
                 │
    ┌────────────┴──────────────┐
    │                           │
    ▼                           ▼
┌─────────────────────┐   ┌──────────────────────┐
│  AWS Athena         │   │   S3 + CloudFront    │
│  (Data Lake)        │   │   (Docs Website)     │
│ Dados transformados │   │ cimabrhp.com         │
└─────────────────────┘   └──────────────────────┘
```

### Configuração do Build

O arquivo `buildspec.yml` define o pipeline:

```yaml
# Ambiente de produção
Database: AWS Glue Catalog (awsdatacatalog)
Schema: landing
Region: us-east-1

# Configuração de dados
S3 Staging:  s3://proj-clima-dbt-hp/dbt/metadados/
S3 Data:     s3://proj-clima-dbt-hp/dbt/table/
S3 Docs:     www.cimabrhp.com (hospedagem web)

# Threads de execução: 4 (paralelo)
```

### 📋 Fases do Build

| Fase | O que faz | Status |
|------|----------|--------|
| **install** | Instala Python 3.13 e dbt-athena | ✅ |
| **pre_build** | Gera credentials automáticas | ✅ |
| **build** | Executa pipeline dbt completo | ✅ |
| **post_build** | Deploy docs para S3/Website | ✅ |

### 🚀 Fluxo Automático

1. **Push para GitHub** → Dispara CodeBuild automaticamente
2. **CodeBuild** → Executa todas as transformações no Athena
3. **Testes** → Valida 13 testes de qualidade
4. **Deploy** → Publica documentação em tempo real
5. **Timestamp** → Adiciona data/hora de atualização

### 🌐 Documentação ao Vivo

A documentação dbt é publicada automaticamente em:
- **URL:** [www.cimabrhp.com](https://www.cimabrhp.com)
- **Atualização:** A cada push no GitHub
- **Conteúdo:** Lineage, modelos, testes, histórico de execução

---

## ✅ O que Foi Implementado

### Infraestrutura Cloud
- ✅ **AWS S3** - Data Lake escalável
- ✅ **Amazon Athena** - Engine SQL serverless
- ✅ **AWS Glue Catalog** - Metadados centralizados
- ✅ **AWS CodeBuild** - CI/CD automatizado
- ✅ **Domain registrado** - www.cimabrhp.com

### Pipeline de Dados
- ✅ **Modelagem dimensional** - Staging → Intermediate → Marts
- ✅ **13 testes de qualidade** - Validação automática
- ✅ **dbt Documentation** - Lineage e catálogo gerado
- ✅ **Data lineage** - Rastreamento completo
- ✅ **Macros reutilizáveis** - Código limpo e DRY

### DevOps & Deployment
- ✅ **GitHub integrado** - Versionamento de código
- ✅ **buildspec.yml** - Configuração de build
- ✅ **Deploy automático** - Triggered por push no GitHub
- ✅ **Documentação ao vivo** - Publicada em tempo real
- ✅ **Timestamp de atualização** - Rastreamento de versões

---

## 🚀 Próximos Passos / Roadmap

- [ ] Integração com Power BI / Looker para visualizações
- [ ] Alertas automáticos para anomalias climáticas
- [ ] Modelo de previsão com ML (Prophet/LSTM)
- [ ] Dashboard em tempo real com Streamlit
- [ ] Orquestração com Apache Airflow ou EventBridge
- [ ] Testes de performance e otimizações de custo
- [ ] Lambda para processamento em tempo real
- [ ] API REST para consultas (API Gateway + Lambda)

---

## 📈 Insights e Estatísticas

### Cobertura do Projeto
- **4 modelos** DBT desenvolvidos (staging, intermediate, marts)
- **13 testes** de qualidade automatizados
- **1 fonte** de dados estruturada (API meteorológica)
- **4 cidades** analisadas continuamente

### Validação de Dados
- ✅ Validação de tipos de dados
- ✅ Testes de range de valores (0-1 para fase da lua)
- ✅ Validação de valores aceitos (fcst, comb, obs, stats)
- ✅ Testes de nulidade em campos críticos
- ✅ Testes de unicidade em chaves primárias

### Performance
- **Threads de execução:** 4 (paralelo)
- **Tempo de build:** ~2 minutos (em produção)
- **Frequência de atualização:** A cada push no GitHub
- **Uptime:** 99.9% (S3 + Athena)

---

## 🎓 Conhecimentos Adquiridos & Skills Desenvolvidos

### Cloud & AWS
- **Amazon S3:** Arquitetura de data lake, particionamento
- **Amazon Athena:** SQL serverless, otimização de queries
- **AWS Glue:** Catálogo de metadados, schema discovery
- **AWS CodeBuild:** CI/CD, automação de builds
- **IAM:** Políticas de acesso, segurança na nuvem

### Engenharia de Dados
- **dbt (Data Build Tool):** Modelagem dimensional, transformações SQL
- **Data lineage:** Rastreamento completo de origem dos dados
- **Data quality:** Testes automatizados e validação
- **Documentação:** Auto-geração com dbt docs

### DevOps & Infraestrutura
- **Git & GitHub:** Versionamento, gitflow, CI/CD
- **buildspec.yml:** Configuração de pipelines
- **Infrastructure as Code:** AWS CodeBuild automation
- **Monitoring:** Logs e histórico de execução

### SQL & Transformações
- **SQL avançado:** CTEs, window functions, agregações
- **Staging patterns:** Limpeza e validação de dados brutos
- **Intermediate modeling:** Enriquecimento com métricas derivadas
- **Mart design:** Tabelas analíticas para BI

### Boas Práticas de Software
- **DRY (Don't Repeat Yourself):** Macros reutilizáveis
- **Testing:** Cobertura completa de testes
- **Documentation:** Auto-documentação com dbt
- **Version control:** Histórico de mudanças rastreável

---

## 🐛 Troubleshooting & Erros Comuns

### ❌ AccessDeniedException no CodeBuild

**Erro:**
```
You are not authorized to perform: athena:StartQueryExecution on the resource
```

**Solução:** Adicione permissões IAM (veja "Configurando CodeBuild" acima)
- Athena: `athena:*`
- Glue: `glue:*`
- S3: `s3:*` (nos seus buckets)

---

### ❌ "No database found" no Athena

**Causa:** Database não existe no Glue Catalog

**Solução:**
```
AWS Console → Glue → Databases → Create database
Nome: landing (ou seu database configurado em buildspec.yml)
```

---

### ❌ Build falha na fase pré_build

**Causa:** `create_profiles.py` não encontrado

**Solução:**
```bash
# Certifique-se que create_profiles.py existe no repositório
ls -la create_profiles.py

# Se não existir, copie do repo ClimaBR-hp
```

---

### ❌ dbt debug falha com timeout

**Causa:** Athena está lento ou credenciais incorretas

**Solução:**
1. Teste localmente: `dbt debug`
2. Verifique AWS credentials: `aws sts get-caller-identity`
3. Aumente timeout em `create_profiles.py`

---

### 📚 Referências

- **dbt docs:** [docs.getdbt.com](https://docs.getdbt.com)
- **AWS Athena:** [docs.aws.amazon.com/athena](https://docs.aws.amazon.com/athena)
- **AWS Glue:** [docs.aws.amazon.com/glue](https://docs.aws.amazon.com/glue)
- **CodeBuild:** [docs.aws.amazon.com/codebuild](https://docs.aws.amazon.com/codebuild)

---

## 💡 Exemplos de Queries (Com os Dados do Projeto)

### Análise Mensal de Temperatura por Cidade

```sql
SELECT 
    cidade,
    mes,
    ROUND(media_temperatura, 2) as temp_media,
    dias_com_dados,
    condicao_mais_frequente
FROM fct_analise_mensal
WHERE mes >= DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '3' MONTH
ORDER BY mes DESC, cidade
LIMIT 20;
```

### Desvio de Previsão (Acurácia)

```sql
SELECT 
    cidade,
    AVG(ABS(desvio_temperatura)) as desvio_temp_medio,
    AVG(ABS(desvio_precipitacao)) as desvio_precip_medio,
    COUNT(*) as dias_analisados
FROM fct_desvio_previsao
GROUP BY cidade
ORDER BY desvio_temp_medio ASC;
```

### Amplitude Térmica Diária

```sql
SELECT 
    data,
    cidade,
    amplitude_termica,
    temperatura_max,
    temperatura_min,
    umidade,
    condicao
FROM int_clima_diario
WHERE data >= CURRENT_DATE - INTERVAL '7' DAY
ORDER BY data DESC, amplitude_termica DESC;
```

### Precipitação Esperada vs Observada

```sql
SELECT 
    DATE_TRUNC('week', data) as semana,
    cidade,
    SUM(precipitacao) as precip_observada,
    SUM(precipitacao_esperada) as precip_esperada,
    ROUND(SUM(precipitacao) - SUM(precipitacao_esperada), 2) as diferenca
FROM int_clima_diario
GROUP BY DATE_TRUNC('week', data), cidade
ORDER BY semana DESC;
```

---

## 🤝 Contribuições

Este é um projeto de portfólio. Sugestões e melhorias são bem-vindas!

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📜 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo LICENSE para detalhes.

---

## 👨‍💼 Autor

**Hélio Paiva**

- 📧 Email: [heliopaiva@gmail.com](mailto:heliopaiva@gmail.com)
- 🔗 GitHub: [@HELIOJR](https://github.com/HELIOJR)
- 💼 LinkedIn: [Hélio Paiva](https://linkedin.com/in/helio-paiva)
- 🎓 Pós-Graduação: Engenharia de Dados - Anhanguera

### Sobre

Engenheiro de Dados com foco em pipelines cloud-native, transformação de dados e arquitetura escalável. Apaixonado por construir soluções de dados que geram impacto real.

**Desenvolvimento com:** AWS, dbt, SQL, Python, Git

---

## 🙏 Agradecimentos

- dbt Labs pela excelente ferramenta de transformação de dados
- Amazon Web Services pela infraestrutura escalável
- Anhanguera pela formação em Engenharia de Dados
- Comunidade open-source de dados

---

<div align="center">

**⭐ Se este projeto foi útil, considere dar uma estrela! ⭐**

Desenvolvido com ❤️ por Hélio Paiva | ClimaBR-hp © 2026

</div>
