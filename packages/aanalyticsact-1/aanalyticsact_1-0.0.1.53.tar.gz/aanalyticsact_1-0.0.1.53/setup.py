from setuptools import setup, find_packages

setup(
    name='aanalyticsact-1',
    version='0.0.1.53',
    description='adobe analytics library for Team ACT',
    author='Youngkwang Cho',
    author_email='youngkwang.cho@gmail.com',
    url='https://github.com/YK124/Glory-s',
    install_requires=['aanalytics2', 'pymysql', 'aanalyticsactauth','pandas'],
    packages=find_packages(exclude=[]),
    keywords=['adobe','analytics','api'],
    python_requires='>=3.12',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
