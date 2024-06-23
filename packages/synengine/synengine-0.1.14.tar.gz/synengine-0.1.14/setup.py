from setuptools import setup, find_packages

setup(
    name='synengine',
    version='0.1.14',
    license='MIT',
    description='automation tool for unity content integration',
    author='esun',
    author_email='esun@voteb.com',
    url='https://github.com/SyngularXR/SynPusher-Unity-Engine',
    keywords=['python', 'grpc'],
    packages=find_packages(),
    install_requires=[
        'aenum==3.1.11',
        'pydantic',
        'engine_grpc',
        'compipe'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.10'
    ]
)
