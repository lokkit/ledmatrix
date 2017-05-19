=========
ledmatrix
=========
Tool to display stuff on 8x8 matrix of lokkit


* Free software: MIT license
* Documentation: https://ledmatrix.readthedocs.io.


Features
--------

Code for showing random numbers and a blinking 1 after 50 iterations
```
python ledmatrix/cli.py roll_the_number 50 && python ledmatrix/cli.py number 1 && python ledmatrix/cli.py inverse_number 1 && python ledmatrix/cli.py number 1 && python ledmatrix/cli.py inverse_number 1 && python ledmatrix/cli.py number 1 && python ledmatrix/cli.py inverse_number 1 && python ledmatrix/cli.py number 1 && python ledmatrix/cli.py inverse_number 1 && python ledmatrix/cli.py number 1 && python ledmatrix/cli.py number 1
```

Code for showing random dice and a blinking 2 after 50 iterations
```
python ledmatrix/cli.py roll_the_dice 50 && python ledmatrix/cli.py dice 2 && python ledmatrix/cli.py inverse_dice 2 && python ledmatrix/cli.py dice 2 && python ledmatrix/cli.py inverse_dice 2 && python ledmatrix/cli.py dice 2 && python ledmatrix/cli.py inverse_dice 2 && python ledmatrix/cli.py dice 2 && python ledmatrix/cli.py inverse_dice 2 && python ledmatrix/cli.py dice 2 && python ledmatrix/cli.py number 2
```