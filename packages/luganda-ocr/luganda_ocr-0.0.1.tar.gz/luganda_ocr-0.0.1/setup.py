from setuptools import setup, find_packages

setup(
    name='luganda_ocr',
    version='0.0.1',
    author='LugandaOCR',
    author_email='beijukab@gmail.com',
    description='An OCR package for Luganda language',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'tensorflow == 2.14.0',
        'numpy',
        'pandas',
    ],
    include_package_data=True,
    package_data={'luganda_ocr': ['models/*.h5', 'models/*.py']}, 
    license='MIT', 
)

