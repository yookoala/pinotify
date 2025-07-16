from collections.abc import Callable
from datetime import timedelta
import gpiod
import sys
from gpiod.line import Bias, Edge

CHIP = '/dev/gpiochip0' # The default for RPi 5
LINE = 17 # Use the GPIO Pin 17 for this project

if not gpiod.is_gpiochip_device(CHIP):
    print("Chip not found: {}".format(CHIP))
    sys.exit(1)

chip = gpiod.Chip(CHIP)
print(chip.get_info())

def edge_type_str(event):
    if event.event_type is event.Type.RISING_EDGE:
        return "Rising"
    if event.event_type is event.Type.FALLING_EDGE:
        return "Falling"
    return "Unknown"

def print_event(event):
    print(
        "line: {}  type: {:<7}  event #{}".format(
            event.line_offset, edge_type_str(event), event.line_seqno
        )
    )
    
def watch_line(
    line: int,
    event_handler: Callable,
    consumer: str = '',
    chip: str = CHIP,
    edge_detection: Edge = Edge.NONE,
    bias: Bias = Bias.AS_IS,
):
    with gpiod.request_lines(
        chip,
        consumer=consumer,
        config={
            line: gpiod.LineSettings(
                edge_detection=edge_detection,
                bias=bias,
                debounce_period=timedelta(milliseconds=10),
            )
        },
    ) as request:
        while True:
            for event in request.read_edge_events():
                event_handler(event)


if __name__ == '__main__':
    watch_line(
        line=LINE,
        event_handler=print_event,
        chip=CHIP,
        consumer="Test Project",
        edge_detection=Edge.FALLING,
        bias=Bias.PULL_UP,
    )
