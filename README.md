# RPi Doorbell Watcher

This is a small project for hooking a wireless doorbell receiver to an RPi.
And then trying to capture electirc signal when the doorbell button is triggered.

This involves wiring a specific misc-brand wireless doorbell receiver to the
pin 17 of a Raspberry Pi device. And then reading the rising / falling of the
voltage difference of the LED, which is triggered when the button is pressed.

The specific LED flashes many times when the doorbell is pressed, so there is
a grace mechanism to only trigger the program once for every certain period of
time.

The software make use of the new [libgpiod](https://libgpiod.readthedocs.io/)
interface with the [official Python binding library](https://libgpiod.readthedocs.io/en/latest/python_api.html).


## Usage

```
usage: python3 -m doorbot [-h] [--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [--command COMMAND] [--pin PIN]

Set logging level for the application.

options:
  -h, --help            show this help message and exit
  --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
  --command COMMAND     Command to run in JSON array format
  --pin PIN             Integer. Set the GPIO pin number to monitor. Default: 17.
```

## License

This software is licensed under the [MIT License](https://mit-license.org/).
A copy of the license can be obtained in the repository at [LICENSE.md](LICENSE.md).
