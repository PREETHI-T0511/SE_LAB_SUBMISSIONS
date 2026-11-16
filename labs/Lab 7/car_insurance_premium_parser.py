from datetime import datetime


def normalize_registration(plate):
    """
    Removes spaces, dashes and dots from a registration number.
    Handles unexpected inputs safely.
    """
    if not isinstance(plate, str):
        return ""

    plate = plate.strip().upper()

    for ch in [' ', '-', '.']:
        plate = plate.replace(ch, '')

    return plate


def total_claim_amount(text):
    """
    Adds up valid claim amounts separated by semicolons.
    Ignores invalid or empty amounts.
    """
    if not isinstance(text, str):
        return 0

    total = 0

    for amount in text.split(';'):
        amount = amount.strip()

        try:
            if amount:
                total += int(amount)
        except ValueError:
            continue

    return total


def driver_age(dob, current_year=2026):
    """
    Calculates age from a DD/MM/YYYY date.
    Handles malformed dates safely.
    """
    if not isinstance(dob, str):
        return 0

    try:
        birth_date = datetime.strptime(dob, "%d/%m/%Y")
        today = datetime(current_year, 12, 31)

        age = today.year - birth_date.year

        if (birth_date.month, birth_date.day) > (today.month, today.day):
            age -= 1

        return age

    except (ValueError, TypeError):
        return 0


def main():
    print("==== Running normalize_registration ====")
    value = input("Enter a registration number (e.g. ka 01 ab 1234): ")
    print("Normalized registration:", normalize_registration(value))

    print("\n==== Running total_claim_amount ====")
    value = input("Enter past claim amounts separated by ; (e.g. 12000;4500;800): ")
    print("Total claimed:", total_claim_amount(value))

    print("\n==== Running driver_age ====")
    value = input("Enter the driver's date of birth as DD/MM/YYYY (e.g. 14/08/1999): ")
    print("Driver age in 2026:", driver_age(value))


if __name__ == "__main__":
    main()
