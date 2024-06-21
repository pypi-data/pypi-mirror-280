from setuptools import setup, find_packages


setup(
    name="rail_tpu_utils",
    version="0.0.3",
    packages=find_packages(),
    install_requires=[
        "google-cloud-storage",
        "requests"
    ],
)
