import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from mawaqit import PrayerCalculator, Location, InputData, LocationError, ValidationError, CalculationError

def test_errors():
    calc = PrayerCalculator()

    print("--- Test 1 indices: Invalid Latitude ---")
    try:
        loc = Location(latitude=100, longitude=73, timezone=5)
    except LocationError as e:
        print(f"Caught expected LocationError: {e}")

    print("\n--- Test 2: Invalid Month ---")
    try:
        data = InputData(year=2025, month=13, day=1)
        # Location is valid, but calculation triggers date validation
        loc = Location(latitude=33, longitude=73, timezone=5)
        calc.calculate(loc, data)
    except ValidationError as e:
        print(f"Caught expected ValidationError: {e}")

    print("\n--- Test 3: Polar Region (Calculation Error) ---")
    try:
        # High latitude in winter - some prayers might be impossible
        loc = Location(latitude=80, longitude=0, timezone=0)
        data = InputData(year=2025, month=12, day=24)
        calc.calculate(loc, data)
    except CalculationError as e:
        print(f"Caught expected CalculationError: {e}")

if __name__ == "__main__":
    test_errors()
