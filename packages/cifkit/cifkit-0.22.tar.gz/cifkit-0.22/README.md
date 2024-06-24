# cifkit: Python toolkit for high-throughput analysis of CIF files

cifkit is designed for the high-throughput analysis of Crystallographic Information File (.cif) formats. In just 2-4 lines of code, cifkit allows users to (1) automatically format files, filter files based on a comprehensive set of attributes, (2) determine nearest neighbor and coordination environments at each site, (3) facilitate the plotting of polyhedrons.

## Overview

cifkit provides two primary objects: `Cif` and `CifEnsemble`.

- **`Cif`**: Initializes with a `.cif` file path. It parses the .cif file, preprocesses ill-formatted files, generates supercells, and computes nearest neighbors. It also determines coordination numbers using four different methods and generates polyhedrons for each site.

- **`CifEnsemble`**: Initializes with a folder path containing `.cif` files. It identifies unique attributes, such as space groups and elements, across the .cif files, moves and copies files based on these attributes. It generates histograms for all attribute.

## Motivation

- I build high-throughput analysis tools using `.cif` files for research. The tools analyze bonding distances, site analysis, and coordination numbers.
- Each tool requires preprocesing, formatting, copying, moving, and sorting .cif files.
- To streamline the above tasks, I developed `CifPy` that can be easily imported for the above tasks.


## Principle

I believe that the best product is intuitive. Therefore, I have limited to the use of two objects only so that this can be easily imported and used without the need to look up the documentation.

## Documentation

Please see the tutorial provided here (TBA).

## Installation

To run locally:

```bash
pip install -e .
```

## Progerss

- 20240619: Implement logging, 
- 20240618: Draw polyhedron from each site



## Tasks

- CifEnsemble: generate histograms on cif attributes
- Test: include coverage percent
- Test: include supported Python versions
- Test: include requirements.txt
- Test: include GitHub integration test
- GitHub: include contribution
- GitHub: include GitHub pull request/issue template
- Doc: write features/tutorials
- Doc: host the documentation


## Developer

Sangjoon Bob Lee (@bobleesj)