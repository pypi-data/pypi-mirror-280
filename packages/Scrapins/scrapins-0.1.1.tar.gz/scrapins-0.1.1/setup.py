from setuptools import setup, find_packages

setup(
    name='Scrapins',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        # Ajouter ici les dépendances nécessaires
    ],
    entry_points={
        'console_scripts': [
            # Ajouter ici des points d'entrée pour les scripts de la ligne de commande, si nécessaire
        ],
    },
    author='Lùkas K.',
    author_email='lukas.koltes@hotmail.fr',
    description='Une description personnelle pour des outils de Scraping',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/votrecompte/ma_bibliotheque',  # Remplacer par l'URL de votre projet
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
