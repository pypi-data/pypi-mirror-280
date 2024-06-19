from setuptools import setup, find_packages

setup(
    name='python-icd10',
    version='1.0.0',
    url='https://gitlab.com/marcnealer/python-icd10.git',
    author='Marc Nealer',
    author_email='marcnealer@gmail.com',
    description='Downloads ICD10 codes from the CDC and makes them available in a searchable database',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'pydantic',
        'xmltodict',
        'tinydb'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],
)
