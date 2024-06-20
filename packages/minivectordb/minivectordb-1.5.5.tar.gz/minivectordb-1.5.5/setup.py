from setuptools import setup, find_packages
import platform

architecture = platform.machine().lower()

is_arm = 'arm' in architecture or 'aarch64' in architecture

if is_arm:
    reqs = [
        "numpy==1.26.4",
        "transformers==4.37.2",
        "faiss-cpu",
        "torch",
        "pytest",
        "pytest-cov",
        "scikit-learn",
        "thefuzz[speedup]",
        "FlagEmbedding"
    ]
else:
    reqs = [
        "numpy==1.26.4",
        "onnx",
        "onnxruntime",
        "onnxruntime-extensions",
        "transformers==4.37.2",
        "faiss-cpu",
        "torch",
        "pytest",
        "pytest-cov",
        "scikit-learn",
        "thefuzz[speedup]",
        "FlagEmbedding"
    ]

setup(
    name='minivectordb',
    version='1.5.5',
    author='Carlo Moro',
    author_email='cnmoro@gmail.com',
    description="This is a Python project aimed at extracting embeddings from textual data and performing semantic search.",
    packages=find_packages(),
    package_data={
        'minivectordb': ['resources/embedding_model_quantized.onnx']
    },
    include_package_data=True,
    install_requires=reqs,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)