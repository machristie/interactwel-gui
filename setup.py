import setuptools

setuptools.setup(
    name="interactwel_gui",
    version="0.0.1",
    description="Django app for visualizing InterACTWEL simulations",
    packages=setuptools.find_packages(),
    install_requires=[
        'django>=1.11.15'
    ]
)
