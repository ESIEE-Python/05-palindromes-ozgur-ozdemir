"""
05 ispalindrome ozgur-ozdemir
"""

#### Fonction secondaire
def ispalindrome(s):
    """
    Vérifie si une chaîne de caractères est un palindrome.
    """
    # Table de correspondance pour enlever les accents
    accents = str.maketrans(
        "ÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸàâäçéèêëîïôöùûüÿ",
        "AAACEEEEIIOOUUUYaaaceeeeiioouuuy"
    )

    s = s.translate(accents)

    # On met en minuscule, retire les espaces et les caractères non alphanumériques
    s = ''.join(c for c in s.lower() if c.isalnum())

    return s == s[::-1]

#### Fonction principale

def main():

    """
    Fonction principale pour tester la fonction ispalindrome
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
