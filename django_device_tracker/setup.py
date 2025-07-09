from setuptools import setup, find_packages


setup(
    name='django-device-tracker',
    version='0.1.0',
    description='Reusable device tracking app for Django projects',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2'
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
    ],
)