from setuptools import setup, find_packages


version = '0.0.0'


install_requires = (
    'djangorestframework>=2.3.14,<3',
    'django-imagekit>=3.2.1',
)

setup(
    name='django-image-api',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='',
    long_description='',
    author='Incuna',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/django-image-api/',
    install_requires=install_requires,
    extras_require=extras_require,
    zip_safe=False,
)
