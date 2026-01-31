# Welcome to Biomathhh

| Category     | Badges                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  |
| **CI/CD**    | [![Tests](https://github.com/ubc-mds/DSCI_524_group27_biomathhh/actions/workflows/test.yml/badge.svg)](https://github.com/ubc-mds/DSCI_524_group27_biomathhh/actions/workflows/test.yml) [![Docs](https://github.com/ubc-mds/DSCI_524_group27_biomathhh/actions/workflows/docs.yml/badge.svg)](https://github.com/ubc-mds/biomathhh/actions/workflows/docs.yml) [![Build](https://github.com/ubc-mds/DSCI_524_group27_biomathhh/actions/workflows/release.yml/badge.svg)](https://github.com/ubc-mds/DSCI_524_group27_biomathhh/actions/workflows/release.yml) |
| **Coverage** | [![codecov](https://codecov.io/gh/ubc-mds/DSCI_524_group27_biomathhh/branch/main/graph/badge.svg)](https://codecov.io/gh/ubc-mds/DSCI_524_group27_biomathhh)                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Meta**     | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) [![License](https://img.shields.io/github/license/ubc-mds/DSCI_524_group27_biomathhh.svg)](LICENSE)                                                                                                                                                                                                                                                                                                                                    |

# Biomathhh

[Documentation](https://ubc-mds.github.io/DSCI_524_group27_biomathhh/)

## Contributors

- [Delnaz Dadkhah Tirani](https://github.com/dianadadkhah)
- [Victoria Farkas](https://github.com/farkasvic)
- [Gurveer Madurai](https://github.com/gurverm)
- [Zhihao Xie](https://github.com/lightgl)

## Overview

Biomathhh is a Python package designed to efficiently provide common mathematical calculations used in biological research and analysis. This package provides life science researchers with easy-to-use functions for population dynamics, laboratory calculations, chemical properties, and biodiversity metrics. By consolidating these frequently-used formulas into a single package, Biomathhh aims to reduce repetitive coding and improve reproducibility in biological data analysis.

## Python Ecosystem

Biomathhh occupies a niche space in the Python ecosystem by focusing specifically on fundamental biological calculations that are frequently needed but not necessarily available in one package.

While comprehensive scientific computing packages like **NumPy** and **SciPy** provide the underlying mathematical operations, they do not offer biology-specific implementations. Packages like **Biopython** focus primarily on molecular biology, sequence analysis, and bioinformatics rather than general biological mathematics. Ecological analysis packages such as **scikit-bio** do include diversity indices, but lack the laboratory calculation functions that bench scientists use daily.

**Related packages:**

- [NumPy](https://numpy.org/) - General numerical computing
- [SciPy](https://scipy.org/) - Scientific computing and statistics
- [Biopython](https://biopython.org/) - Molecular biology and bioinformatics tools
- [scikit-bio](http://scikit-bio.org/) - Bioinformatics and diversity metrics

Biomathhh fills the gap by providing a focused toolkit for the everyday mathematical needs of biologists across multiple subfields.

## Functions

- **exponential_growth**: Calculates exponential growth or decay over time using the continuous growth model  
  $$N(t) = N_0 e^{rt}$$  
  Useful for modeling population growth, bacterial culture expansion, radioactive decay, etc.

- **calculate_dilution**: Performs dilution and concentration calculations using the standard laboratory equation  
  $$C_1 V_1 = C_2 V_2$$  
  Helps researchers determine volumes and concentrations needed for preparing solutions, dilutions, and experimental reagents.

- **calculate_pH**: Converts between hydrogen ion concentration and pH using  
  $$\text{pH} = -\log_{10}([H^+])$$

- **sw_diversity_index**: Computes the Shannon–Wiener Diversity Index  
  $$H' = -\sum_{i=1}^{S} p_i \ln(p_i)$$  
  where \(p_i\) is the proportion of individuals belonging to species \(i\).


## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install git+https://github.com/UBC-MDS/DSCI_524_group27_biomathhh.git
```

## Example Usage

For more examples on how to use Biomathhh, use cases can be found in the package documentation [here](https://ubc-mds.github.io/DSCI_524_group27_biomathhh/).

Below are working examples for each function in Biomathhh.

### Calculate Dilution

```python
from biomathhh.dilution import calculate_dilution

final_conc = calculate_dilution(
    stock_concentration=5.0,
    stock_volume=1.0,
    final_volume=5.0
)

print(final_conc)
````

**Output:**

```
1.0
```

### Exponential Growth

```python
from biomathhh.exponential_growth import exponential_growth

value = exponential_growth(100, 0.05, 10)
print(round(value, 6))
```

**Output:**

```
164.872127
```

### pH Calculation

```python
from biomathhh.pH_scale import calculate_pH

ph_value = calculate_pH(1e-4)
print(ph_value)
```

**Output:**

```
4.0
```

### Shannon–Wiener Diversity Index

```python
from biomathhh.sw_diversity_index import sw_diversity_index

species_counts = [50, 30, 20]
diversity_index = sw_diversity_index(species_counts)

print(round(diversity_index, 4))
```

**Output:**

```
1.0297
```


## Contributing

Interested in contributing? Please check out the [contributing guidelines](https://github.com/UBC-MDS/DSCI_524_group27_biomathhh/blob/main/CONTRIBUTING.md) for this project. Note that this project is released with a [code of conduct](https://github.com/UBC-MDS/DSCI_524_group27_biomathhh/blob/main/CODE_OF_CONDUCT.md) and by contributing you agree to abide by its terms.

## Copyright

- Copyright © 2026 Diana Dadkhah Tirani Victoria Farkas Gurveer Madurai Zhihao Xie
  .
- Free software distributed under the [MIT License](./LICENSE).

## Credits

LLMs (Gemini, Claude, ChatGPT) were used to format docstrings/documentation and with assistance in debugging workflow errors.
