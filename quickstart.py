import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from mawaqit import PrayerCalculator, Location

# 1. Setup Location (The only required input)
location = Location(latitude=24.8607, longitude=67.0011, timezone=5.0)

# 2. Calculate using professional defaults
# (Current date, Ala Hazrat method, Hanafi Madhab, 70s Delta T)
times = PrayerCalculator().calculate(location)

# 3. Print results
print(f"Date:    {times.metadata['date']}")
print(f"Fajr:    {times.fajr}")
print(f"Sunrise: {times.sunrise}")
print(f"Dhuhr:   {times.dhuhr}")
print(f"Asr:     {times.asr}")
print(f"Maghrib: {times.maghrib}")
print(f"Isha:    {times.isha}")
