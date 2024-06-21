from setuptools import setup, find_packages

setup(
    name='jmeter-metrics-visualizer',
    version='0.4.0',
    description='A package to generate HTML reports from JMeter CSV files for Historical Data Comparision',
    author='Pavan Kumar',
    author_email='pavankumar.qae@gmail.com',
    url='https://github.com/yourusername/jmeter-metrics-visualizer',
    packages=find_packages(),
    package_data={
        'jmeter_metrics_visualizer': ['template/template.html'],
    },
    install_requires=[
        'pandas',
        'plotly',
        'jinja2'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
