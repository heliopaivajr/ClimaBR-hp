# 🚨 SOLUÇÃO RÁPIDA: AccessDeniedException no CodeBuild

## Seu Erro
```
AccessDeniedException: You are not authorized to perform: athena:StartQueryExecution
```

## ✅ Solução em 3 Passos

### 1️⃣ Vá para AWS Console

```
AWS Console → IAM → Roles
```

### 2️⃣ Procure a Role do CodeBuild

Procure por: `codebuild-` (nome do seu projeto)
- Pode ser: `codebuild-ClimaBR-hp-service-role`

### 3️⃣ Adicione Permissões

**Dentro da role encontrada:**

1. Clique em **"Add permissions"**
2. Selecione **"Create inline policy"**
3. Clique na aba **"JSON"**
4. Delete tudo e cole isto:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "athena:*",
        "glue:*",
        "s3:*",
        "logs:*"
      ],
      "Resource": "*"
    }
  ]
}
```

5. Clique **"Review policy"**
6. Nome: `codebuild-dbt-policy`
7. Clique **"Create policy"**

## ✨ Pronto!

Agora volte ao CodeBuild e rode novamente:

```
CodeBuild → Seu projeto → Start build
```

---

## 📋 Se ainda não funcionar:

**Verifique:**
- [ ] Database `landing` existe? (AWS Glue → Databases)
- [ ] S3 buckets `proj-clima-dbt-hp` existem?
- [ ] Region está correta? (us-east-1)
- [ ] Você clicou "Create policy" com sucesso?

**Testando localmente:**
```bash
cd climabr
dbt debug  # Deve conectar sem erros
```

---

## 📞 Dúvidas?

Veja o arquivo completo: **AWS_CODEBUILD_SETUP.md**

Desenvolvido para ClimaBR-hp ❤️
