import sys
import os
from pathlib import Path

# Add the src directory to the path so we can import mawaqit_astro without installing it
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from mawaqit_astro import PrayerCalculator, Location, InputData, Madhab

def run_custom_example():
    """
    This example shows how to customize every aspect of the calculation:
    - Custom Date & Delta T
    - Custom Elevation (Height)
    - Custom Method (Custom Angles)
    - Custom Madhab (Shafi)
    """

    # 1. Customized Location (with Elevation/Height)
    location = Location(
        latitude=51.5074,
        longitude=-0.1278,
        timezone=0.0,
        elevation=50.0, # Height in meters
        temp_c=10.0,    # Custom temperature (e.g. 10°C)
        pressure_hpa=1010.0 # Custom pressure (e.g. 1010 hPa)
    )

    # 2. Customized Date and DeltaT
    date = InputData(
        year=2026,
        month=1,
        day=1,
        deltaT=71.5 # Specific Delta T
    )

    # 3. Custom Calculation Method & Madhab
    # Creating a custom method (e.g., Fajr 15, Isha 15)
    my_custom_method = PrayerCalculator.create_custom_method(
        name="My Professional Method",
        fajr_angle=15.0,
        isha_angle=15.0
    )

    calculator = PrayerCalculator(
        method=my_custom_method,
        madhab=Madhab.SHAFI # Custom Madhab
    )

    # 4. Calculate (Pass location first, then custom date)
    prayers = calculator.calculate(location, date)

    # Display results
    print("="*40)
    print(f"{'MAWAQIT - CUSTOM SETTINGS':^40}")
    print("="*40)
    print(f"Location:  London (Alt: {location.elevation}m)")
    print(f"Date:      {prayers.metadata['date']}")
    print(f"Method:    {prayers.metadata['method']}")
    print(f"Madhab:    {prayers.metadata['madhab']}")
    print("-" * 40)

    for name in ["fajr", "sunrise", "dhuhr", "asr", "maghrib", "isha"]:
        print(f"{name.capitalize():<15}: {getattr(prayers, name):>10}")

    print("="*40)

if __name__ == "__main__":
    run_custom_example()

