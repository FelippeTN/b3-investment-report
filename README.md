# b3-investment-report

💻 Atualização Diária Automática por E-mail de Ativos da Bolsa de Valores (B3), Resumidos por IA – Deploy no Railway! 💻
Desde que comecei a investir na bolsa, sempre procurei informações na internet sobre os ativos nos quais já investi para acompanhar suas performances.
Foi então que, anteontem, tive a ideia de criar um serviço em Python para extrair informações do Status Invest. O sistema faz Web Scraping da página e envia os dados para o modelo Llama 3 70B, que os resume, analisa e me envia um relatório por e-mail todos os dias às 9h da manhã.


## Instalation

1. Clone the repository:

```bash
  git clone https://github.com/FelippeTN/b3-investment-report.git
  cd llama_pdf_summarizer
```

2. Create a virtual environment:

```bash
  python -m venv venv
  venv/Scripts/Activate
```

3. Install the dependencies:

```bash
  pip install -r requirements.txt
```
