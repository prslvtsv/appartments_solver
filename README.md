# work in progress version

uses py 3.9 only 

generate board with gh definition 

run gh_solver in any IDE

based on [polyomino](https://github.com/jwg4/polyomino) and [exact-cover](https://github.com/jwg4/exact_cover) by [jwg4](https://github.com/jwg4)

## installing

Opt A:
  1. clone conda env provided

Opt B:
  1. Create clean conda venv
  2. populate is with setuptools=51.1.3 ⚠️ and numpy >= 1.21
  3. install exact_cover using
  ```
  pip install exact_cover=0.4.3
  ```

## dependencies

 - numpy >= 1.21
 - exact-cover=0.4.3 ⚠️
  [exact-cover](https://github.com/jwg4/exact_cover)
 - setuptools=51.1.3 ⚠️
