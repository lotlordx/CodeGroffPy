names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""

    for sn, val in enumerate(zip(names, countries)):
        print(f"{sn+1}. {val[0].ljust(11)}{val[1]}")


enumerate_names_countries()