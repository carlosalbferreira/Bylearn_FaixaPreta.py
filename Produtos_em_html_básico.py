produtos = {
    'Chocolates': ['Suflair', 'Bubbly', 'Nutella', 'Brigadeiro' ],
    'Salgadinhos': ['Torcida', 'Fofura', 'Pururuca', 'Lobits'],
    'Gulosemas': ['Paçoca', 'Gibi', 'Geleia d agua', 'Cone de Leite'],
    'Pacotinhos': ['Bolinha Branca', 'Suspiro', 'Tang', 'Polvilho']
    }

pagina=open("Doceria.html","w")
pagina.write("""
<html lang="pt-BR">
<head>
    <title>Produtos da doceria</title>
</head>
<body>
""")
for c, v in produtos.items():
    pagina.write("<h1>%s</h1>" % c)
    for e in v:
        pagina.write("<h1>%s</h1>" % e)
pagina.write("""
</body>
</html>
""")
pagina.close()
