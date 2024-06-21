from setuptools import setup, find_packages

setup(
    name="chessanalytics_st",  
    version="0.2.2",  
    packages=find_packages(),  
    install_requires=[  
        "numpy",
        "streamlit",
        "pandas",
        "plotly",
        "chessanalytics",
    ],
    author="lot022",
    description="Graphical representation of functions from chessanalytics library designed for Streamlit apps.",
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",
    url="https://github.com/lot022/chessanalytics_st",  # Project URL
    classifiers=[  
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  

)
