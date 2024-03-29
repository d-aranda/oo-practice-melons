############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        "musk",
        1998,
        "green",
        True,
        True,
        "Muskmelon"
    )
    musk.add_pairing("mint")
    all_melon_types.append(musk)
    
    cas = MelonType(
        "cas", 
        2003,
        "orange",
        False,
        False,
        "Casaba"
    )
    cas.add_pairing("strawberry")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType(
        "cren",
        1996,
        "green",
        False,
        False,
        "Crenshaw"
    )
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType(
        "yw",
        2013,
        "yellow",
        False,
        True,
        "Yellow Watermelon"
    )
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)


    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")
        print('')


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_codes = {}

    for melon_type in melon_types:
        melon_codes[melon_type.code] = melon_type
        
    return melon_codes


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, type, shape, color, harvested_from, harvested_by):
        self.type = type
        self.shape = shape
        self.color = color
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by
        
    def is_sellable(self):
        if self.shape > 5 and self.color > 5 and self.harvested_from != 3:
            return True
        
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)
    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")

    melons = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7,
              melon_8, melon_9]
    
    return melons



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            sold = "(CAN BE SOLD)"
            print(f"harvested by {melon.harvested_by} from Field {melon.harvested_from} {sold}")
        else:
            not_sold = "(NOT SELLABLE)"
            print(f"harvested by {melon.harvested_by} from Field {melon.harvested_from} {not_sold}")



melon_types = make_melon_types()
print_pairing_info(melon_types)
make_melon_type_lookup(melon_types)

# make_melons(melon_types)
# get_sellability_report(make_melons(melon_types))



##################
# Further Study  #
##################

def make_melons_from_file(melon_types, filename):
    with open(filename) as data:
       
        melons_by_id = make_melon_type_lookup(melon_types)

        melons = []
        
        for line in data:
            line = line.rstrip().split()
            _, shape, _, color, _, code, _, _, harvested_by, _, _, harvested_from  = line

            melons.append(Melon(melons_by_id[code], int(shape), int(color), int(harvested_from), harvested_by))
        
        return melons

melon_types = make_melon_types()
get_sellability_report(make_melons_from_file(melon_types, 'harvest_log.txt'))


