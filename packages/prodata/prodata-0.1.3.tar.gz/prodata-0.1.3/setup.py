from setuptools import setup, find_packages

setup(
    name='prodata',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'scikit-learn'
    ],
    python_requires='>=3.6',
    author='Poorva Nande',
    author_email='poorva.nande@gmail.com',
    description='A Python library for data preprocessing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/poorvaN13/prodata',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
