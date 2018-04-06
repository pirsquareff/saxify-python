# Saxify

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

An implementation of Symbolic Aggregate approXimation (SAX) in python.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Quickstart](#quickstart)
- [Project's Structure](#projects-structure)
- [How to Run](#how-to-run)
  - [Jupyter Notebook](#jupyter-notebook)
  - [Python](#python)
- [Appendix](#appendix)
  - [Quiz Instruction](#quiz-instruction)
  - [Result](#result)
- [License](#license)

## Prerequisites
- [Docker Community Edition](https://www.docker.com/community-edition) `17.12.0-ce` or higher
- [Docker Compose](https://docs.docker.com/compose/install) `1.18.0` or higher
- [Yarn](https://yarnpkg.com/en/docs/install) `1.3.2` or higher (a `npm` replacement)

## Quickstart

1. Start JupyterLab by running `docker-compose up` or `yarn start`.
2. Copy and paste the URL with a token key shown in the shell output into your browser to access JupyterLab.

## Project's Structure

- All data are located in [`workspace/data`](./workspace/data) directory.
  1. Time series data: [`ts_a.txt`](./workspace/data/ts_a.txt) and [`ts_b.txt`](./workspace/data/ts_b.txt)
  2. Normalized time series data: [`ts_a_normalized.txt`](./workspace/data/ts_a_normalized.txt) and [`ts_b_normalized.txt`](./workspace/data/ts_b_normalized.txt)
  3. Result: [`result.txt`](./workspace/data/result.txt)
- Source code
  1. Jupyter Notebook: [`saxify.ipynb`](./workspace/saxify.ipynb)
  2. Python: [`saxify.py`](./workspace/saxify.py)

## How to Run
### Jupyter Notebook
1. Open [`saxify.ipynb`](./workspace/saxify.ipynb) by double-clicking this file in the left panel.
2. Go to Run > Run All Cells

### Python
1. Open terminal from JupyterLab: File > New > Terminal.
2. Change a directory to `/home/jovyan/work/workspace` by running `cd /home/jovyan/work/workspace`.
3. Run `python3 saxify.py -a ./data/ts_a.txt -b ./data/ts_b.txt -x 7 -y 5 -z 6`

## Appendix
### Quiz Instruction
[Download here](https://www.mycourseville.com/sites/all/modules/courseville/files/uploads/2017_2/2110430/materials/QUIZ_2_2018.7381.1522384146.0567.pdf)

### Result
```txt
5730329521	Parinthorn Saithong (Aof)
X = 7
Y = 5
Z = 6
n = 128
w = 32
SAX_A = EDDCEDCCCBCDBBDECDDDCCDDDDECBDEC
SAX_B = CDCCCDFFCCBDCBDCDBEBECFBCECCCCDC
Distance between SAX_A & SAX_B = 3.82
```

## License

[MIT](LICENSE) © Parinthorn Saithong