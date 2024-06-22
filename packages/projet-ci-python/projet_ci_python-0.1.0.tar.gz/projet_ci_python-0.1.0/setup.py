from setuptools import setup, find_packages

setup(
    name='projet-ci-python',  # Remplacez par le nom de votre package
    version='0.1.0',  # Version de votre package
    description='A simple example package',  # Description courte
    long_description=open('README.md').read(),  # Description longue tirée du fichier README.md
    long_description_content_type='text/markdown',  # Type de contenu de la description longue
    author='Lucas',  # Nom de l'auteur
    author_email='lccoc248@gmail.com',  # Email de l'auteur
    url='https://gitlab.com/LxzKyQ/projet-ci-python.git',  # URL du projet
    packages=find_packages(),  # Inclut tous les packages Python trouvés
    include_package_data=True,  # Inclut les fichiers de données spécifiés dans MANIFEST.in
    install_requires=[
        # Ajoutez d'autres dépendances ici si nécessaire
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Version minimale de Python requise
)
