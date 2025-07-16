import gpiod
import sys
from datetime import timedelta
from gpiod.line import Bias, Edge

CHIP = '/dev/gpiochip0'
LINE = 'GPIO17'

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

with gpiod.request_lines(
    CHIP,
    consumer='Test Project',
    config={
        17: gpiod.LineSettings(
            edge_detection=Edge.BOTH,
            bias=Bias.PULL_UP,
            debounce_period=timedelta(milliseconds=10),
        )
    },
) as request:
    while True:
        for event in request.read_edge_events():
            print(
                "line: {}  type: {:<7}  event #{}".format(
                    event.line_offset, edge_type_str(event), event.line_seqno
                )
            )
