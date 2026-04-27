# 🔧 Configuração AWS CodeBuild - Guia Completo

## 🚨 Problema: AccessDeniedException

```
An error occurred (AccessDeniedException) when calling the StartQueryExecution operation: 
You are not authorized to perform: athena:StartQueryExecution on the resource
```

### ✅ Solução: Adicionar Permissões IAM

A IAM Role do CodeBuild precisa ter permissões para acessar Athena, S3 e Glue.

---

## 📋 Passo 1: Encontrar a Role do CodeBuild

1. Vá para **AWS Console** → **CodeBuild**
2. Selecione seu projeto **ClimaBR-hp**
3. Vá para **Environment** → **Service role**
4. Anote o nome da role (ex: `codebuild-ClimaBR-hp-service-role`)

---

## 🔐 Passo 2: Adicionar Política IAM

### Opção A: AWS Console (Recomendado para iniciantes)

1. Vá para **IAM** → **Roles**
2. Procure pela role do CodeBuild
3. Clique em **Add permissions** → **Create inline policy**
4. Escolha **JSON**
5. Cole a política abaixo:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AthenaAccess",
      "Effect": "Allow",
      "Action": [
        "athena:*",
        "glue:*",
        "s3:*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "CloudWatchLogs",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    }
  ]
}
```

6. Nomeie a policy: `codebuild-athena-policy`
7. Clique em **Create policy**

### Opção B: Política Mais Restrita (Segurança)

Se preferir limitar permissões por recurso específico:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AthenaQueryExecution",
      "Effect": "Allow",
      "Action": [
        "athena:StartQueryExecution",
        "athena:GetQueryExecution",
        "athena:GetQueryResults",
        "athena:StopQueryExecution",
        "athena:GetWorkGroup"
      ],
      "Resource": "arn:aws:athena:us-east-1:ACCOUNT_ID:workgroup/primary"
    },
    {
      "Sid": "GlueAccess",
      "Effect": "Allow",
      "Action": [
        "glue:GetDatabase",
        "glue:GetTable",
        "glue:GetPartitions",
        "glue:CreateTable",
        "glue:UpdateTable",
        "glue:DeleteTable"
      ],
      "Resource": [
        "arn:aws:glue:us-east-1:ACCOUNT_ID:catalog",
        "arn:aws:glue:us-east-1:ACCOUNT_ID:database/landing",
        "arn:aws:glue:us-east-1:ACCOUNT_ID:table/landing/*"
      ]
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
        "arn:aws:s3:::proj-clima-dbt-hp/*",
        "arn:aws:s3:::proj-clima-dbt-hp",
        "arn:aws:s3:::www.cimabrhp.com/*",
        "arn:aws:s3:::www.cimabrhp.com"
      ]
    },
    {
      "Sid": "CloudWatchLogs",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:us-east-1:*:*"
    }
  ]
}
```

> **Substitua `ACCOUNT_ID` pelo seu número de conta AWS!**

---

## 🔍 Como Encontrar seu Account ID

1. Vá para **AWS Console** → **Account**
2. Procure por "Account ID" no topo
3. Copie o número (ex: `123456789012`)

---

## ✅ Passo 3: Verificar as Permissões

Depois de adicionar a política:

1. Vá para **CodeBuild** → Selecione seu projeto
2. Clique em **Start build** para testar

Se ainda tiver erros, vá para **Build logs** para ver detalhes.

---

## 📝 Passo 4: Variáveis de Ambiente no CodeBuild

Certifique-se que as variáveis estão corretas no **Environment variables**:

| Nome | Valor | Descrição |
|------|-------|-----------|
| `DBT_DATABASE` | `awsdatacatalog` | Athena data catalog |
| `DBT_SCHEMA` | `landing` | Nome do seu database no Glue |
| `S3_STAGING_DIR` | `s3://proj-clima-dbt-hp/dbt/metadados/` | Dados temporários |
| `S3_DATA_DIR` | `s3://proj-clima-dbt-hp/dbt/table/` | Tabelas finais |
| `S3_DOCS_DIR` | `s3://www.cimabrhp.com` | Documentação |
| `AWS_REGION` | `us-east-1` | Região AWS |

---

## 🐛 Troubleshooting

### Erro: "No database found"
- Verifique se o database `landing` existe no **AWS Glue** → **Databases**
- Se não existir, crie um novo database

### Erro: "No tables found"
- Certifique-se que as tabelas estão no Glue Catalog
- Execute `dbt debug` localmente para validar

### Erro: "S3 sync failed"
- Verifique se os buckets existem
- Confirme que a role tem `s3:*` permissions

### Build passes mas docs não aparecem no S3
- Verifique o S3_DOCS_DIR no buildspec.yml
- Confirme que o bucket existe e é acessível

---

## 📊 Fluxo de Resolução

```
┌─────────────────────────────┐
│ GitHub Push                 │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│ CodeBuild Triggered         │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│ Install Phase (OK)          │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│ Pre-Build Phase (OK)        │
│ (gera profiles.yml)         │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│ Build Phase                 │
│ ├─ dbt deps (OK)           │
│ ├─ dbt debug ❌ (ERRO AQUI) │
│ └─ Precisa de permissão IAM│
└─────────────────────────────┘
```

**Solução:** Adicione `athena:StartQueryExecution` à role

---

## 🎯 Checklist Final

- [ ] IAM Role criada/associada ao CodeBuild
- [ ] Política IAM com permissões Athena adicionada
- [ ] Variáveis de ambiente configuradas
- [ ] Database `landing` existe no Glue
- [ ] S3 buckets criados e acessíveis
- [ ] buildspec.yml commitado no GitHub
- [ ] GitHub conectado ao CodeBuild
- [ ] Build executado com sucesso
- [ ] Logs mostram "dbt run completed"
- [ ] Documentação publicada no S3

---

## 📚 Referências

- [dbt Athena Setup](https://docs.getdbt.com/docs/core/connect-data-platform/athena-setup)
- [AWS IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [CodeBuild Documentation](https://docs.aws.amazon.com/codebuild/latest/userguide/getting-started.html)
- [Athena Permissions](https://docs.aws.amazon.com/athena/latest/ug/access-control.html)

---

## ❓ Ainda com dúvidas?

1. Verifique os **Build logs** em CloudWatch
2. Procure por mensagens de erro específicas
3. Valide localmente com `dbt debug` antes de fazer push

Desenvolvido com ❤️ para seu projeto ClimaBR-hp
