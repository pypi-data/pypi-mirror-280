from setuptools import setup, find_packages

setup(name='thematch',
		version='0.2',
		description='thematch',
		url='https://github.com/ExpertOfAI/thematch',
		author='ExpertOfAI',
		license='MIT',
		packages=find_packages(),
		classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		],
		python_requires='>=3.6',
      		install_requires = ["rapidfuzz"]
		)
