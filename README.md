# pyConics

Handle points, lines and conics by using algebraic geometry.

## Installation

From a local directory clones this project:

```bash
git clone https://github.com/osowsky/pyConics.git (by using http)
```

or

```bash
git clone git@github.com:osowsky/pyConics.git (by using ssh)
```

or you can install this package:

```bash
pip install pyConics
```

$\alpha * \sum_{i}^{\infty}$

$$
\alpha * \sum_{i}^{\infty}
$$

$$
\left[\begin{matrix}
1 & 2 & 3 \\
1 & 2 & 3 \\
1 & 2 & 3
\end{matrix}\right]
$$

## Usage

`pycounts` can be used to count words in a text file and plot results
as follows:

```python
from pycounts.pycounts import count_words
from pycounts.plotting import plot_words
import matplotlib.pyplot as plt

file_path = "test.txt"  # path to your file
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines.
Please note that this project is released with a Code of Conduct.
By contributing to this project, you agree to abide by its terms.

## License

`pyConics` was created by Jefferson Osowsky.
It is licensed under the terms of the GNU General Public License v3.0 license.

## Credits

`pyConics` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/)
and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
