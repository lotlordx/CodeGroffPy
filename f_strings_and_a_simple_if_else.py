MIN_DRIVING_AGE = 18


def allowed_driving(name : str, age: int) -> None:
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    allowed_to_drive = f"{name} is allowed to drive" if age >= MIN_DRIVING_AGE else f"{name} is not allowed to drive"
    print(allowed_to_drive)