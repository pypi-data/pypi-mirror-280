from setuptools import setup, find_packages

setup(
    name='activity_4_entrega_Programacion_Ciencia_de_datos',
    version='0.1.1',
    description='A data analysis project for PEC4 UOC, Master Data Science',
    author='Massimiliano Brevini',
    author_email='mbrevini@uoc.edu',
    url='https://github.com/mbreviniuoc/PEC4-ProgCienciadedatos',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'folium',
        'Pillow',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'run-analysis=main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
