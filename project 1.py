from calendar import month

age = int(input('What\'s your age?').strip())

# Calculate age in different units
months = age * 12
weeks = months // 4  # Use integer division to avoid floating-point values
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Print results with appropriate formatting
print("You've lived for:")
print(f"{months:,} months.")
print(f"{weeks:,} weeks.")
print(f"{days:,} days.")
print(f"{hours:,} hours.")
print(f"{minutes:,} minutes.")
print(f"{seconds:,} seconds.")



















