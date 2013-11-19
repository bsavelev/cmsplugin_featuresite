from setuptools import setup, find_packages

setup(
    name='cmsplugin-featuresite',
    version='1.0.0',
    description='plugin for Django-CMS with Topic, Feature, Client, Service',
    long_description='plugin for Django-CMS with Topic, Feature, Client, Service',
    author='Boris Savelev',
    author_email='boris.savelev@gmail.com',
    url='https://github.com/bsavelev/cmsplugin_featuresite',
    packages=find_packages(),
    keywords='django cms django-cms feature client topic service',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
