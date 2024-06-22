from setuptools import setup, find_packages

setup(
    name='vital-model-paraphrase-MiniLM-onnx',
    version='0.2.1',
    author='Marc Hadfield',
    author_email='marc@vital.ai',
    description='Vital Onnx version of paraphrase-MiniLM-L3-v2',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vital-ai/vital-onnx-model-packages',
    packages=find_packages(exclude=[]),
    entry_points={
    },
    scripts=[],
    package_data={
        'vital-model-paraphrase-MiniLM-onnx': ['model/*']
    },
    license='Apache License 2.0',
    install_requires=[

    ],
    extras_require={

    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
