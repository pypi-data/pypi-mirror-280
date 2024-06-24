from setuptools import setup, find_packages

setup(
    name='searchbar_component',
    version='0.1.5',  # Increment this number
    description='A Streamlit component for a search bar with autosuggestions',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit>=0.63',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
