from setuptools import setup

classifiers=[
    'Intendent Audience :: Education',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License'
    
]

setup(name='OpenCU',
version='0.0.0',
description='Package to compute equations used in optics.',
long_description='Developed by students of Department of AOP, CU, batch-2018-2022',
url='#',
author='Rajarshi Banerjee',
author_email='raju.banerjee.720@email.com',
license='MIT',
classifiers=classifiers,
packages=['fourier'],
install_requires=["numpy"],

zip_safe=False)