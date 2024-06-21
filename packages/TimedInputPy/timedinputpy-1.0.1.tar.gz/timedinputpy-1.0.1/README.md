# TimedInputPy

TimedInputPy is a python library that provides input function/object that has a
thread based time limit on input.

## API

|object|method|description|
|-----|-----|-----|
|TimedInput(timeout, prompt, default||Timed input reader:|
|||timeout -> how long to wait?|
|||prompt -> what to ask?|
|||default -> what to sat when timeout happens?|
|||action -> action callback to perform when timeout happens|
||get_input()|Function to be used as input reader|
||read()|Reads the input from the reader|
|timed_input(timeout, prompt, default)|| Function for reading timed input, arguments same as above|

## Example usage
```
# Sample usage:
if __name__ == '__main__':
    test_timeout = 5
    test_prompt = 'Enter name: '
    test_default = 'world'

    # As a method
    s = timed_input(test_timeout, test_prompt, test_default)
    print('Hello {}!'.format(s), flush=True)

    print()

    # As a class
    s = TimedInput(test_timeout, test_prompt, test_default).read()
    print('Hello {}!'.format(s), flush=True)
```

## Instalation
Module can be installed using pip3:
`pip3 install TimedInputPy`
