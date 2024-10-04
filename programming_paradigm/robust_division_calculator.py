def safe_divide(numerator, denominator):
    try :
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Erreur: Veuillez entrer des valeurs numériques."

    try:
        # Tente de diviser les deux nombres
        result = numerator / denominator
    except ZeroDivisionError:
        return "Erreur: Division par zéro."

    return f"Résultat de la division: {result}"