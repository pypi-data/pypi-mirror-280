from setuptools import setup, find_packages

setup(
    name='vs_api_elastic_history',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    author='Lucca Fabro',
    author_email='lucca.fabro@viasoft.com.br',
    description='Biblioteca adpatação do langchain para uso mais fácil das ferramentas de histórico',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)