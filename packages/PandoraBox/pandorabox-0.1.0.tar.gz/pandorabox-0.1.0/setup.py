from setuptools import setup, find_packages

setup(
    name='PandoraBox',
    version='0.1.0',
    packages=find_packages(),
    description='Python Box Is All You Need. You Can Create Python Environment, Execut Python, Close Python Environment Freely and Easily.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='pydaxing',
    author_email='pydaxing@gmail.com',
    url='https://github.com/pydaxing/PythonBox',
    entry_points={
        'console_scripts': [
            'pybox=src.app.main',
        ],
    },
    install_requires=[
        # 依赖列表
        'requests',
        'fastapi',
        'uvicorn',
        'pydantic',
        'jupyter-client',
        'ipython',
        'pandas',
        'numpy',
        'matplotlib',
        'loguru',
        'jsonlines',
    ],

)


