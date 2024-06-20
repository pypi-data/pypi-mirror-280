import codecs

import setuptools

# Read the README.md file for the long description
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open('version.txt', 'r') as f:
    current_version = f.read().strip()

# Split the current version into its components
version_parts = current_version.split('.')
major, minor, patch = map(int, version_parts)

# Increment the patch version
patch += 1

# Construct the new version string
new_version = f"{major}.{minor}.{patch}"

# Write the new version number back to the file
with open('version.txt', 'w') as f:
    f.write(new_version)

setuptools.setup(
    name='metacountregressor',
    version=new_version,
    description='Extensions for a Python package for estimation of count models.',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Specify the content type as Markdown
    url='https://github.com/zahern/CountDataEstimation',
    author='Zeke Ahern',
    author_email='zeke.ahern@hdr.qut.edu.au',
    license='QUT',
    packages=['metacountregressor'],
    zip_safe=False,
    python_requires='>=3.10',
    install_requires=[
        'numpy>=1.13.1',
        'scipy>=1.0.0'
    ]
)
