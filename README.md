# Welcome to Biomathhh

|         |                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/biomathhh.svg)](https://pypi.org/project/biomathhh/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/biomathhh.svg)](https://pypi.org/project/biomathhh/) |
| Meta    | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md)                                                                                                              |

_TODO: the above badges that indicate python version and package version will only work if your package is on PyPI.
If you don't plan to publish to PyPI, you can remove them._

# Biomathhh

[!Documentation](https://ubc-mds.github.io/DSCI_524_group27_biomathhh/)

## Overview

Biomathhh is a Python package designed to efficiently provide common mathematical calculations used in biological research and analysis. This package provides life science researchers with easy-to-use functions for population dynamics, laboratory calculations, chemical properties, and biodiversity metrics. By consolidating these frequently-used formulas into a single package, Biomathhh aims to reduce repetitive coding and improve reproducibility in biological data analysis.

## Functions

- **exponential_growth**: Calculates exponential growth or decay over time using the continuous growth model (N = N₀ \* e^(rt)). Useful for modeling population growth, bacterial culture expansion, radioactive decay, etc.

- **calculate_dilution**: Performs dilution and concentration calculations using the C₁V₁ = C₂V₂ formula. Helps researchers determine volumes and concentrations needed for preparing solutions, dilutions, and experimental reagents.

- **calculate_pH**: Converts between pH values and hydrogen ion concentrations ([H⁺]).

- **sw_diversity_index**: Computes the Shannon-Wiener Diversity Index (H') from species abundance data. This metric measures biodiversity in ecological communities.

## Python Ecosystem

Biomathhh occupies a niche space in the Python ecosystem by focusing specifically on fundamental biological calculations that are frequently needed but not necessarily available in one package.

While comprehensive scientific computing packages like **NumPy** and **SciPy** provide the underlying mathematical operations, they do not offer biology-specific implementations. Packages like **Biopython** focus primarily on molecular biology, sequence analysis, and bioinformatics rather than general biological mathematics. Ecological analysis packages such as **scikit-bio** do include diversity indices, but lack the laboratory calculation functions that bench scientists use daily.

**Related packages:**

- [NumPy](https://numpy.org/) - General numerical computing
- [SciPy](https://scipy.org/) - Scientific computing and statistics
- [Biopython](https://biopython.org/) - Molecular biology and bioinformatics tools
- [scikit-bio](http://scikit-bio.org/) - Bioinformatics and diversity metrics

Biomathhh fills the gap by providing a focused toolkit for the everyday mathematical needs of biologists across multiple subfields.

## Contributors

Delnaz Dadkhah Tirani, Victoria Farkas, Gurveer Madurai, Zhihao Xie

## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install git+https://github.com/UBC-MDS/DSCI_524_group27_biomathhh.git
```

## Usage

For more examples on how to use Biomathhh, use cases can be found in the package documentation [!here](https://ubc-mds.github.io/DSCI_524_group27_biomathhh/).

To use biomathhh in your code:

```python
>>> import biomathhh
>>> biomathhh.hello_world()
```

## Contributing

Interested in contributing? Please check out the [!contributing guidelines](https://github.com/UBC-MDS/DSCI_524_group27_biomathhh/blob/main/CONTRIBUTING.md) for this project. Note that this project is released with a [!code of conduct](https://github.com/UBC-MDS/DSCI_524_group27_biomathhh/blob/main/CODE_OF_CONDUCT.md) and by contributing you agree to abide by its terms.

## Copyright

- Copyright © 2026 Diana Dadkhah Tirani Victoria Farkas Gurveer Madurai Zhihao Xie
  .
- Free software distributed under the [MIT License](./LICENSE).

## Credits

LLMs (Gemini, Claude, ChatGPT) were used to format docstrings/documentation and with assistance in debugging workflow errors.
