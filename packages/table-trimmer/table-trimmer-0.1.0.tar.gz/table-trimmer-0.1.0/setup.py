from setuptools import setup, find_packages

setup(
    name='table-trimmer',
    version='0.1.0',
    description=(
        "Uma ferramenta utilitária para otimizar bancos de dados SQLite ao permitir que os usuários "
        "selecionem e mantenham apenas as colunas essenciais em novas tabelas derivadas. Isso ajuda "
        "na criação de tabelas mais enxutas, melhorando a gestão e o desempenho do banco de dados ao "
        "reduzir a quantidade de dados desnecessários. Ideal para limpeza de dados, análises "
        "específicas e para otimizar o armazenamento e a consulta em bancos de dados grandes."
    ),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Woul Schneider',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "table-trimmer=table_trimmer.main:main",
        ]
    },
    install_requires=[]
)
