from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='ziplip',
    version='1.0.9',
    description='ziplip - Zip File Password Brute Force Tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://mrfidal.in/cyber-security/ziplip',
    author='Fidal',
    author_email='mrfidal@proton.me',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
        'Topic :: Security',
    ],
    keywords='zip file, brute force, enumeration, scanning, mrfidal, cyber security',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'ziplip': ['ziplip.sh'],
    },
    install_requires=[
        'requests',
        'click', 
    ],
    entry_points={
        'console_scripts': [
            'ziplip=ziplip.cli:cli', 
        ],
    },
)
