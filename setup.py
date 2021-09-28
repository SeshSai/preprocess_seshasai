import setuptools

with open('README.md', 'r') as  file:
    long_description = file.read()
    
setuptools.setup(
    name = 'preprocess_seshasai', #This should be unique
    version = '0.0.1',
    author = 'SeshaSai Guna',
    author_email = 'seshu.guna@live.com',
    description = 'Complete textdata preprocessing package',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Aproved :: MIT License',
	"Operating System :: OS Independent"],
	python_requires = '>=3.5'
    )