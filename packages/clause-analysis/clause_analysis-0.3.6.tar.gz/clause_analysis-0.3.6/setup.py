import subprocess
from setuptools import setup, find_packages
from setuptools.command.install import install

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        subprocess.call(['python', '-m', 'spacy', 'download', 'en_core_web_sm'])

setup(
    name='clause_analysis',
    version='0.3.6',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'spacy',
        'requests',  # เพิ่มไลบรารีที่จำเป็นอื่น ๆ ถ้ามี
    ],
    entry_points={
        'console_scripts': [
            'clause_analyzer = clause_analysis.clause_analyzer:main',
            'passive_tense_classifier = clause_analysis.passive_tense_classifier:main',
            'tense_analyzer = clause_analysis.tense_analyzer:main',
        ],
    },
    author='Kritpofrankss',
    author_email='Krit.poshakrishna@gmail.com',
    description='A library to analyze clauses and classify tenses.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Kritpofrankss/clause_analysis',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    cmdclass={
        'install': PostInstallCommand,
    },
)
