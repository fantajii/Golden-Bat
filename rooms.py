"""
Rooms & World Map Data Repository

Description: Provides data lookup dictionaries defining spatial room connections,
             item placements, room descriptions, and item descriptions.
"""

def get_rooms() -> dict:
    """Returns map topology dictionary detailing room paths and item drops."""
    return {
        'Ancient Tomb': {'East': 'Secret Tunnel', 'item': 'Silver Baton'},
        'Echoing Gallery': {'South': 'Ancient Tomb', 'item': 'Botan Rice Candy'},
        'Secret Tunnel': {'West': 'Ancient Tomb', 'North': 'Shipwrecked Beach'},
        'Shipwrecked Beach': {'East': 'Abandoned Church', 'South': 'Secret Tunnel', 'North': 'Ocean-Facing Cliffs'},
        'Ocean-Facing Cliffs': {'East': 'Abandoned Residential District', 'South': 'Shipwrecked Beach',
                                'item': 'Red Cape'},
        'Abandoned Residential District': {'West': 'Ocean-Facing Cliffs', 'East': 'Rusted Armory'},
        'Rusted Armory': {'West': 'Abandoned Residential District', 'South': 'Ancient Atlantean Lab',
                          'item': 'Swashbuckler Armor'},
        'Abandoned Church': {'South': 'Church Cellar', 'East': 'Ancient Atlantean Lab', 'West': 'Shipwrecked Beach',
                             'item': 'Hydroflask'},
        'Church Cellar': {'North': 'Abandoned Church', 'item': 'Kinesis Stone'},
        'Ancient Atlantean Lab': {'North': 'Rusted Armory', "South": 'Submerged Observation Deck',
                                  'West': 'Abandoned Church', 'East': 'Hall of Ancient Tech',
                                  'item': 'Spectral Reins'},
        'Submerged Observation Deck': {'North': 'Ancient Atlantean Lab', 'item': 'Icarus Data'},
        'Hall of Ancient Tech': {'West': 'Ancient Atlantean Lab', 'villain': 'Nazo'}
    }

def get_room_description() -> dict:
    """Returns descriptive narrative strings for each map room."""
    return {
        'Ancient Tomb': "A silent chamber of white stone. In the center lies the golden sarcophagus where "
                        "Golden Bat slept for 10,000 years."
                        "\n[marie3]Marie sits in the corner of the tomb, weeping...",
        'Secret Tunnel': "A narrow, damp passageway lit by faint bioluminescent moss. It connects the tomb to "
                         "the surface ruins...",
        'Shipwrecked Beach': "White sands littered with the wreckage of Professor Mire's ship. The Pacific waves "
                             "crash against jagged rocks...",
        'Ocean-Facing Cliffs': "High, windswept precipices overlooking the vast ocean. From here, you can see the "
                               "faint glimmer of the lost city below...",
        'Abandoned Residential District': "Crumbling stone houses that once housed the people of Atlantis. "
                                          "Vines choke the ancient architecture...",
        'Rusted Armory': "A chamber filled with decayed bronze weapons and empty racks that once held the "
                         "military might of a lost empire...",
        'Abandoned Church': "A towering structure with vaulted ceilings. Ancient symbols are "
                            "carved into the stone...",
        'Church Cellar': "A dark, cramped basement filled with crates of old scrolls and strange, humming minerals...",
        'Ancient Atlantean Lab': "A massive hall filled with advanced machinery and glowing crystalline "
                                 "computers from a forgotten science...",
        'Submerged Observation Deck': "A glass-domed room beneath the waves. You can see the aquatic life of "
                                      "Atlantis swimming past the reinforced glass...",
        'Echoing Gallery': "\nThe room is filled with ancient wooden frames."
                           "\nInstead of statues, you see a series of painted boards depicting a golden "
                           "figure saving children from monsters."
                           "\nA faint smell of candy fills the air — a memory of the sweets sold to "
                           "children before the show began."
                           "\nA plaque reads: 'Before the screen, there was the paper. Before the comic, "
                           "there was the street...'"
    }

def get_item_description() -> dict:
    """Returns lore descriptions for collectible relics and items."""
    return {
        'Silver Baton': "An indestructible silver scepter that can fire energy rays.",
        'Red Cape': "A high-collared cape that grants flight and invisibility.",
        'Swashbuckler Armor': "Ornate Atlantean plating that grants invulnerability.",
        'Hydroflask': "A vessel holding the water needed to awaken the God of Justice.",
        'Kinesis Stone': "An ancient relic granting the user powers of terrakinesis and aerokinesis.",
        'Spectral Reins': "Ethereal bindings used to control giant ancient machines.",
        'Icarus Data': "Critical data about the rogue planet's collision course.",
        'Botan Rice Candy': "A classic Japanese treat with an edible wrapper. It smells sweet, like fortune and nostalgia."
    }