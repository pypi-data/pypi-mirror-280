from setuptools import setup, find_packages

setup(
    name='unique-log-questions',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        
    ],
    package_data={
        'app1': ['*.py'],  # Include all Python files in question_answer_db
    },
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
