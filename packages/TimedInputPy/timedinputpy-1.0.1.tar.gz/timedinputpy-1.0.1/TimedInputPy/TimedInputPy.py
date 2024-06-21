#!/usr/bin/env python3
from threading import Thread


class TimedInput(Thread):
    """ Timed input reader """

    def get_input(self):
        """ Actual function for reading the input """
        try:
            print(self.prompt, end='', flush=True)
            self.input = input()
        except EOFError:
            if self.action:
	        self.action()

    def __init__(self, timeout, prompt='', default=None, action=None, *args, **kwargs):
        """
        TimedInput(
            timeout -> amount of seconds to wait for the input,
            prompt -> optionl prompt to display while asking for input,
            default -> string to return in case of timeout,
            action -> action to perform when timeout fires,
            *args/**kwargs -> any additional arguments are passed down to Thread
                            constructor
        )
        Creates an object for reading input, that times out after `timeout` amount
                of seconds.
        """
        self.timeout = timeout
        self.prompt = prompt
        self.input = default
	self.action = action
        super().__init__(target=self.get_input, *args, **kwargs)
        self.daemon = True

    def join(self):
        """ The actual timeout happens here """
        super().join(self.timeout)
        return self.input

    def read(self):
        """ Reads the input from the reader """
        self.start()
        return self.join()


def timed_input(timeout=None, prompt='', default=None, *args, **kwargs):
    if timeout is None:
        return input(prompt)
    else:
        return TimedInput(timeout, prompt, default, *args, **kwargs).read()

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
