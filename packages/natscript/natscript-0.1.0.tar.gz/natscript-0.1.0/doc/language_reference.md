# Natscript Language Reference v0.1

## Keywords

## Standard Library

The Natscript interpreter comes with a small standard library that contains several pre-installed Natscript modules:
- [math.nat](#math): math operations.
- [bitwise.nat](#bitwise): bitwise operations.
- [collections.nat](#collections): set and dict implementations.
- [string.nat](#string): for string manipulation.
- [regex.nat](#regex): for regex support.
- [types.nat](#types): for type conversion functions.
- [json.nat](#json): for json support.
- [system.nat](#system): provides an interface to the OS.
- [time.nat](#time): provides time utilities.

### Math

```
import [...] from "math.nat"
```

### Bitwise

```
import [...] from "bitwise.nat"
```

- bitwise_and: binary operation that calculates logical AND of the inputs: `result of call bitwise_and with [1, 0]  # 0`
- bitwise_or: binary operation that calculates logical OR of the inputs: `result of call bitwise_or with [1, 0]  # 1`
- bitwise_xor: binary operation that calculates logical exclusive OR of the inputs: `result of call bitwise_xor with [1, 1]  # 0`
- bitwise_not: unary operation that flips bits: `result of call bitwise_not with [5]  # -6`
- bitshift_left: binary operation that bit-shifts the first number the specified amount of times: `result of call bitshift_left with [1, 3]  # 8`
- bitshift_right: binary operation

### Collections

```
import [...] from "collections.nat"
```

### String

```
import [...] from "string.nat"
```

### Regex

```
import [...] from "regex.nat"
```

### Types

```
import [...] from "types.nat"
```

### JSON

```
import [...] from "json.nat"
```

### System

```
import [...] from "system.nat"
```

### Time

```
import [...] from "time.nat"
```
