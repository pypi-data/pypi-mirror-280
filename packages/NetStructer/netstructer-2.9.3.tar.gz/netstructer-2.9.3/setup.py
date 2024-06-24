import setuptools

setuptools.setup(
	name = 'NetStructer',
	version = '2.9.3',
	author='Haytam-Zakaria',
	description="",
	packages=['NetStructer'],
	long_description='',
	long_description_content_type='text/markdown',
    install_requires=[
        'cryptography',
        'psutil',
        'requests'],
	classifiers=[
	'Programming Language :: Python :: 3',
	'Operating System :: OS Independent',
	'License :: OSI Approved :: MIT License']
)


'''
python setup.py sdist bdist_wheel
twine upload dist/*

'''
__token__ = '__token__'
token = 'pypi-AgEIcHlwaS5vcmcCJGQ0ZDQ0YWQ2LWUyODQtNDllMC04ODIwLWZjNWYyNmQyOTVjNQACKlszLCIxMTc1ZTVmYi0yNTlkLTRmMDAtOTA0Ni03NWQzMWZjODNiYzEiXQAABiBhLsWfaHKsv6KN2EDEv53Gnxi8F1_1kqpga1fiDdl_gg'