import sys
import os
from pathlib import Path

# Add the src directory to the path so we can import mawaqit_astro without installing it
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from mawaqit_astro import PrayerCalculator, Location, InputData

def run_default_example():
    """
    This example shows how to calculate prayer times using only the
    REQUIRED inputs (Latitude, Longitude, and Timezone).

    All other values use professional defaults:
    - Year/Month/Day/Time: Current system time
    - Madhab: Hanafi
    - Method: Ala Hazrat (18, 18)
    - Delta T: 70s
    - Elevation: 0m
    """

    # 1. Provide only required location data
    location = Location(
        latitude=33.7000000,
        longitude=73.1500000,
        timezone=5.0
    )

    # 2. Calculate using only location (Defaults to current date/time)
    prayers = PrayerCalculator().calculate(location)

    # Display results
    print("="*40)
    print(f"{'MAWAQIT - DEFAULT SETTINGS':^40}")
    print("="*40)
    print(f"Location:  Lat: {location.latitude}, Long: {location.longitude}")
    print(f"Date:      {prayers.metadata['date']}")
    print(f"Method:    {prayers.metadata['method']} (Default)")
    print(f"Madhab:    {prayers.metadata['madhab']} (Default)")
    print("-" * 40)

    for name in ["fajr", "sunrise", "dhuhr", "asr", "maghrib", "isha"]:
        print(f"{name.capitalize():<15}: {getattr(prayers, name):>10}")

    print("="*40)

if __name__ == "__main__":
    run_default_example()

