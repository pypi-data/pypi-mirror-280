# typipe

Extremely minimal package which implements a typed pipe. Some convenience functions are also implemented, e.g. a  map which is more restricted than the built-in map, but is typed.

Tested with pyright/pylance.

Example:

```python
import typipe as ty
def times_two(x: int) -> int:
    return 2 * x

out: Piped[str] = (
    ty.pipe(253)
    | times_two
    | times_two
    | times_two
    | str
    | ty.tap  # prints 2024
    | (lambda s: f"hello {s}!!")
    | (lambda s: cast(str, s).upper())
)

print(out.get())  # HELLO 2024!!
```

Note: lambda functions cannot be typed but you can use cast as above to get autocomplete inside the lambda.
