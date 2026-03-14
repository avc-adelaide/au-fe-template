# au-fe-template

## Manual installation steps

I use a Mac, this will likely colour some of the steps (e.g. using `python3` instead of `python`).

1. Install pixi:
```
curl -fsSL https://pixi.sh/install.sh | bash
```

2. Initialise pixi:
```
pixi init .
```

3. Add fenicsx and other dependencies:
```
pixi install
```
These dependencies are defined in `pixi.toml`.

4. There are two ways to execute using `pixi`. The first is to enter `pixi shell` and use standard CLI methods within it.
The second approach, which is my preference, is to call `pixi run` as a prefix to the standard commands.
To start, install the necessary `uv` requirements:
```
pixi run uv pip install -e . --system
```
Add to these in the `pyproject.toml` file.

5. If all has gone well, check that everything is installed:
```
pixi run python3 -c "import dolfinx; print(dolfinx.__version__)"
```

6. Now you can run an example file:
```
pixi run mpirun -n 4 python3 minimal_example.py
```
(`minimal_example.py` is in the repo already)

The steps above are hard-coded into the `Makefile`:
```
make quickstart
```
You can then delete all of the installed files and start from fresh using
```
make uninstall
```

## Published Documents

Both documents below are automatically built and published to **[GitHub Pages](https://avc-adelaide.github.io/finite-element-toolkit/)** on every push to `main`.

[![Publish Quarto Example and Theory Document](https://github.com/avc-adelaide/finite-element-toolkit/actions/workflows/publish-quarto.yml/badge.svg)](https://github.com/avc-adelaide/finite-element-toolkit/actions/workflows/publish-quarto.yml)

### Theory Document

A didactic introduction to the Finite Element Method (FEM) and its implementation in FEniCSx is available in the [`theory/`](theory/) folder.

**[View / Download PDF](https://avc-adelaide.github.io/finite-element-toolkit/fenics_theory.pdf)**

### Quarto Example

A hands-on walkthrough of a 1-D Poisson problem solved with pure NumPy (no FEM library required) is in the [`quarto/`](quarto/) folder.  The document includes code, maths, and a plot, and is rendered via [Quarto](https://quarto.org).

**[View Quarto document](https://avc-adelaide.github.io/finite-element-toolkit/quarto/)**
