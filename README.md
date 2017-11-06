Did I Finish my Sudoku?
==========
Solution for the [codewars](https://www.codewars.com) challenge.
* Task description: https://www.codewars.com/kata/did-i-finish-my-sudoku/python


The Task
----------
Write a function `done_or_not` passing a board (`list[list_lines]`) as parameter. If the board is valid — return 'Finished!', otherwise return 'Try again!'

### Sudoku Rules

Complete the Sudoku puzzle so that each and every row, column, and region contains the numbers one through nine only once.

#### Rows

![Sudoku row](http://www.sudokuessentials.com/images/Row.gif "Sudoku row")

There are 9 rows in a traditional Sudoku puzzle. Every row must contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. There may not be any duplicate numbers in any row. In other words, there can not be any rows that are identical.

In the illustration, the numbers 5, 3, 1, and 2 are the "givens". They can not be changed. The remaining numbers in black are the numbers that you fill in to complete the row.

#### Columns

![Sudoku column](http://www.sudokuessentials.com/images/Column.gif "Sudoku column")

There are 9 columns in a traditional Sudoku puzzle. Like the Sudoku rule for rows, every column must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Again, there may not be any duplicate numbers in any column. Each column will be unique as a result.

In the illustration, the numbers 7, 2, and 6 are the "givens". They can not be changed. You fill in the remaining numbers as shown in black to complete the column.

#### Regions

![Sudoku region](http://www.sudokuessentials.com/images/Region.gif "Sudoku region")

A region is a 3x3 box like the one shown to the left. There are 9 regions in a traditional Sudoku puzzle.

Like the Sudoku requirements for rows and columns, every region must also contain the numbers 1, 2, 3, 4, 5, 6, 7, 8, and 9. Duplicate numbers are not permitted in any region. Each region will differ from the other regions.

In the illustration, the numbers 1, 2, and 8 are the "givens". They can not be changed. Fill in the remaining numbers as shown in black to complete the region.

### Valid board example

![Sudoku valid board](http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/364px-Sudoku-by-L2G-20050714_solution.svg.png "Sudoku valid board")

For those who don't know the game, here are some information about rules and how to play Sudoku: https://en.wikipedia.org/wiki/Sudoku and http://www.sudokuessentials.com


Running Tests
----------
Tests are located in the `tests` directory. To run Sudoku related tests just use `python -m unittest tests.test_sudoku`


Authors
----------
* **Denis Z.** &#8212; *Initial work* &#8212; [d2718nis](https://github.com/d2718nis)

See also the list of [contributors](https://github.com/d2718nis/codewars-did-i-finish-my-sudoku/contributors)
who participated in this project.
