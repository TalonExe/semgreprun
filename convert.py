"""Convert a temperature between Celsius and Fahrenheit."""

import argparse
import math


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("temperature", type=float)
    parser.add_argument("unit", choices=("c", "f"), help="unit of the input")
    args = parser.parse_args()

    if not math.isfinite(args.temperature):
        parser.error("temperature must be finite")

    if args.unit == "c":
        converted = args.temperature * 1.8 + 32
        unit = "F"
    else:
        converted = (args.temperature - 32) / 1.8
        unit = "C"

    if not math.isfinite(converted):
        parser.error("converted temperature is out of range")

    print(f"{converted:.2f} °{unit}")


if __name__ == "__main__":
    main()
