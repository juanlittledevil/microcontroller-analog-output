import re
from statistics import mean

data = """
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 20000.00
Sample Interval: 10
Phase Increment: 426.67
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19960.00
Sample Interval: 10
Phase Increment: 425.81
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
Phase Increment: 426.24
Frequency: 19980.00
Sample Interval: 10
...
"""

# Split the data into lines
lines = data.strip().split('\n')

# Initialize lists to store phase increments and frequencies
phase_increments = []
frequencies = []

# Regular expressions to match the lines
phase_increment_pattern = re.compile(r"Phase Increment: (\d+\.\d+)")
frequency_pattern = re.compile(r"Frequency: (\d+\.\d+)")

# Loop through each line and extract values
for line in lines:
    phase_match = phase_increment_pattern.match(line)
    frequency_match = frequency_pattern.match(line)
    
    if phase_match:
        phase_increments.append(float(phase_match.group(1)))
    if frequency_match:
        frequencies.append(float(frequency_match.group(1)))

# Calculate statistics
def calculate_statistics(values):
    return {
        'mean': mean(values),
        'min': min(values),
        'max': max(values)
    }

phase_stats = calculate_statistics(phase_increments)
frequency_stats = calculate_statistics(frequencies)

# Print statistics
print("Phase Increment Statistics:")
print(f"Mean: {phase_stats['mean']}")
print(f"Min: {phase_stats['min']}")
print(f"Max: {phase_stats['max']}")

print("\nFrequency Statistics:")
print(f"Mean: {frequency_stats['mean']}")
print(f"Min: {frequency_stats['min']}")
print(f"Max: {frequency_stats['max']}")
