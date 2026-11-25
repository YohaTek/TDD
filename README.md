# TDD Calculator

A small Python calculator built with test-driven development (TDD): the tests in
`test_calculator.py` describe the behaviour of the implementation in
`calculator.py`.

The project is intentionally tiny — it exists to demonstrate the red/green/refactor
loop on a real, runnable example rather than to be a general-purpose calculator.

## Features

- Binary arithmetic on two operands: `+`, `-`, `*`, `/`
- Input parsing from a single expression string, e.g. `5+5` or `8/2`
- Clear `ValueError` for malformed input or out-of-format expressions
- Interactive command-line entry point

## Layout

| Path                | Purpose                                              |
| ------------------- | ---------------------------------------------------- |
| `calculator.py`     | Parser (`parse_input`) and evaluator (`calculate`)    |
| `test_calculator.py`| `unittest` suite covering all four operations + errors|
| `run_tests.sh`      | Convenience script that runs the test suite           |

## Prerequisites

- Python 3.8 or newer (standard library only — no dependencies to install)

## Run the tests

From the repository root:

```sh
./run_tests.sh
```

The script changes into its own directory, so it also works when called from
elsewhere. The equivalent direct invocation is:

```sh
python3 -m unittest -v test_calculator
```

Expected output ends with:

```
Ran 5 tests in 0.001s

OK
```

## Use the calculator from the command line

```sh
python3 calculator.py
```

```
Enter your first number, operation, and second number (e.g., 5+5): 5+5
Result: 10.0
```

Invalid expressions are reported instead of raising a traceback:

```
Enter your first number, operation, and second number (e.g., 5+5): 3&4
Error: Invalid input format
```

## Use it as a library

```python
from calculator import parse_input, calculate

calculate(parse_input("10-2"))  # 8.0
```

## Development workflow

1. Add a failing test to `test_calculator.py` that describes the desired behaviour.
2. Run `./run_tests.sh` and confirm the new test fails for the expected reason.
3. Make the smallest change in `calculator.py` that makes it pass.
4. Re-run the suite, then refactor with the tests green.

## Known limitations

These are deliberate scope boundaries rather than bugs, and good starting points
for the next test:

- Only one binary operation per expression (`1+2+3` is rejected).
- Operands must be plain unsigned integers; decimals and negative numbers are not
  parsed even though results are returned as `float`.
- Only a prefix match is validated, so trailing characters are currently ignored.
- Division by zero is not handled and will raise `ZeroDivisionError`.
- Percentage support is planned but not implemented yet.
- No `LICENSE` file is present, so the project is "all rights reserved" by default.

## License

No license has been declared. Add one before reusing this code elsewhere.
