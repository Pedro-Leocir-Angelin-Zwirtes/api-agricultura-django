# 🌱 Sistema de Monitoramento e Recomendação Agrícola (SMRA)

API RESTful para gestão de propriedades rurais com foco em agricultura de precisão. Permite o registro de fazendas, talhões, sensores, atividades agrícolas e fornece recomendações automatizadas com base em dados coletados.

## 👤 Público-Alvo

Cooperativas agrícolas, agrônomos e produtores rurais que desejam monitorar e otimizar a produção agrícola de forma centralizada e inteligente.

---

## 📦 Funcionalidades

- Autenticação de usuários com JWT
- Cadastro de fazendas e talhões
- Registro de atividades agrícolas (plantio, irrigação, colheita, etc.)
- Geração de recomendações automáticas de manejo
- Exportação de dados em JSON ou CSV
- (Opcional) Alertas automáticos via tarefas assíncronas

---

## 🗂️ Modelagem e Relacionamentos

### Agricultor
- Campos: `nome`, `cpf`, `telefone`, `data_requisito` (datefield auto_now_add)
- Um usuário pode ter várias fazendas

### Fazenda
- Campos: `nome`, `municipio`, `estado`, `area_total`, `geolocalizacao (opcional)`
- Relação: pertence a um `Agricultor`

### Talhão
- Campos: `nome`, `cultura_atual`, `area`, `data_plantio`
- Relação: pertence a uma `Fazenda`

### AtividadeAgricola
- Campos: `tipo`, `produto_utilizado`, `quantidade`, `operador`, `observacoes`, `data_execucao`
- Relação: pertence a um `Talhão`

### Recomendacao
- Campos: `tipo`, `descricao`, `gerado_em`
- Relação: pertence a um `Talhão`

### Alerta (opcional)
- Campos: `mensagem`, `criticidade`, `enviado_em`
- Relação: pode estar ligado a um `Talhão`

---

## 🔐 Autenticação e Permissões

- Autenticação por JWT (djangorestframework-simplejwt)
- Cada usuário só pode acessar dados das suas próprias fazendas
- Endpoints seguros com permissões personalizadas

---

## 🧪 Tecnologias Utilizadas

- Python 3.11+
- Django 4.x
- Django REST Framework
- Simple JWT
- Django Filter
- PostgreSQL ou SQLite
- (Opcional) Celery + Redis
- (Opcional) drf-yasg ou drf-spectacular (docs)

---

## 🚜 Exemplos de Uso

1. Usuário se registra e cadastra suas fazendas
2. Em cada fazenda, adiciona talhões com culturas diferentes
3. O sistema gera recomendações automáticas de manejo
4. O usuário registra atividades como adubação ou colheita
5. No final da safra, exporta os dados para análise

---

## 📁 Organização dos Models (resumo)

- `Agricultor` (padrão Django)
- `Fazenda` → FK para `Agricultor`
- `Talhao` → FK para `Fazenda`
- `AtividadeAgricola` → FK para `Talhao`
- `Recomendacao` → FK para `Talhao`

---

## ✅ Extras recomendados

- Paginação customizada
- Filtros com django-filter
- Serializers aninhados
- Testes com Pytest + coverage
- CI com GitHub Actions

---

## 📄 Autor

Pedro Leocir Angelin Zwirtes
📧 Contato: pedroangelinzwirtes@gmail.com