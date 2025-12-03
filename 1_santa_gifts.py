### Santa has received a list of gifts, but some are defective. A gift is defective if its name contains the # character.
### Help Santa by writing a function that takes a list of gift names and returns a new list that only contains the non-defective gifts.
### Examples


def filter_gifts(gifts):
    return [gift for gift in gifts if "#" not in gift]
