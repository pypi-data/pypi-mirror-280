from setuptools import setup, find_packages

setup(
    name="simple-roman-numbers",  # Nombre del paquete
    version="0.1.0",  # Versión inicial
    packages=find_packages(),  # Encuentra automáticamente los paquetes en el proyecto
    install_requires=[],  # Lista de dependencias del proyecto
    author="Mon Maldonado",
    author_email="monterdi@gmail.com",
    description="Create a RomanNumber class to be able to do basic calculations with Roman numerals.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/digestiveThinking/roman_numbers",  # URL del proyecto
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)