from setuptools import setup, find_packages

setup(  name="text_data_visualization",              # Package name
        version="0.1.0",                       # Initial release version
        author="Giovana Voltoline",
        author_email="givoltoline@gmail.com",
        description="This program offers 10 different types of data visualizations, specifically designed to work with textual data.",
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        url="https://github.com/yourusername/yourproject",
        packages=find_packages(),              # Automatically find packages in the project
        classifiers=[                          # Optional: Classify your package
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"],
        python_requires='>=3.6',               # Minimum Python version
        install_requires=[                     # Dependencies
            "numpy"     ]                      # Example dependency
    )