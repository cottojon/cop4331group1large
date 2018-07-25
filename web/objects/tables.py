import os


# GLOBALS

# Equipment Globals
e_name = ""
e_type = ""
e_weight = 0.0
e_value = 0.0
e_desc = ""
w_cat = ""
w_range_bool = False
w_thrown = False
w_range = ""
w_props = ""
w_damage = ""
w_type = ""
a_cat = ""
a_bonus = 0
a_dis = False
a_str = 0
# =======

# Spell Globals
s_name = ""
s_level = 0
s_school = ""
s_cast = ""
s_range = ""
s_duration = ""
s_conc = False
s_verbal = False
s_somatic = False
s_material = False
s_mat_desc = ""
s_ritual = False
s_bard = False
s_druid = False
s_cleric = False
s_paladin = False
s_ranger = False
s_sorcerer = False
s_warlock = False
s_wizard = False
s_spell_desc = ""





class TableFactory(object):
    def __init__(self, db):
        # Proficiency Table
        self.add_proficiencies(db)
        # Equipment Table
        self.add_equipment(db)
        # Spell Table
        # self.add_spells(db)
        # Feature Table
        # self.add_features(db)


    def add_proficiencies(self, db):
        p_list = []
        # Language Proficiencies
        # -- Standard Languages
        p_list.append(ProficiencyLookup("Common", "Language"))
        p_list.append(ProficiencyLookup("Dwarvish", "Language"))
        p_list.append(ProficiencyLookup("Elvish", "Language"))
        p_list.append(ProficiencyLookup("Giant", "Language"))
        p_list.append(ProficiencyLookup("Gnomish", "Language"))
        p_list.append(ProficiencyLookup("Goblin", "Language"))
        p_list.append(ProficiencyLookup("Halfling", "Language"))
        p_list.append(ProficiencyLookup("Orc", "Language"))
        # -- Exotic Languages
        p_list.append(ProficiencyLookup("Abyssal", "Language"))
        p_list.append(ProficiencyLookup("Celestial", "Language"))
        p_list.append(ProficiencyLookup("Draconic", "Language"))
        p_list.append(ProficiencyLookup("Deep Speech", "Language"))
        p_list.append(ProficiencyLookup("Infernal", "Language"))
        p_list.append(ProficiencyLookup("Primordial", "Language"))
        p_list.append(ProficiencyLookup("Sylvan", "Language"))
        p_list.append(ProficiencyLookup("Undercommon", "Language"))
        # Skill Proficiencies
        p_list.append(ProficiencyLookup("Athletics", "Skill"))
        p_list.append(ProficiencyLookup("Acrobatics)", "Skill"))
        p_list.append(ProficiencyLookup("Sleight of Hand", "Skill"))
        p_list.append(ProficiencyLookup("Stealth", "Skill"))
        p_list.append(ProficiencyLookup("Arcana", "Skill"))
        p_list.append(ProficiencyLookup("History", "Skill"))
        p_list.append(ProficiencyLookup("Investigation", "Skill"))
        p_list.append(ProficiencyLookup("Nature", "Skill"))
        p_list.append(ProficiencyLookup("Religion", "Skill"))
        p_list.append(ProficiencyLookup("Animal Handling", "Skill"))
        p_list.append(ProficiencyLookup("Insight", "Skill"))
        p_list.append(ProficiencyLookup("Medicine", "Skill"))
        p_list.append(ProficiencyLookup("Perception", "Skill"))
        p_list.append(ProficiencyLookup("Survival", "Skill"))
        p_list.append(ProficiencyLookup("Deception", "Skill"))
        p_list.append(ProficiencyLookup("Intimidation", "Skill"))
        p_list.append(ProficiencyLookup("Performance", "Skill"))
        p_list.append(ProficiencyLookup("Persuasion", "Skill"))
        # Saving Throw Proficiencies
        p_list.append(ProficiencyLookup("Strength", "Saving Throw"))
        p_list.append(ProficiencyLookup("Dexterity", "Saving Throw"))
        p_list.append(ProficiencyLookup("Constitution", "Saving Throw"))
        p_list.append(ProficiencyLookup("Intelligence", "Saving Throw"))
        p_list.append(ProficiencyLookup("Wisdom", "Saving Throw"))
        p_list.append(ProficiencyLookup("Charisma", "Saving Throw"))
        # Tool Proficiencies
        p_list.append(ProficiencyLookup("", "Tool"))
        # Weapon Proficiencies
        # -- Simple
        p_list.append(ProficiencyLookup("Club", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Dagger", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Greatclub", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Handaxe", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Javelin", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Light Hammer", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Mace", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Quarterstaff", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Sickle", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Spear", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Unarmed Strike", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Light Crossbow", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Dart", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Shortbow", "Simple Weapon"))
        p_list.append(ProficiencyLookup("Sling", "Simple Weapon"))
        # -- Martial
        p_list.append(ProficiencyLookup("Battleaxe", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Flail", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Glaive", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Greataxe", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Greatsword", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Halberd", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Lance", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Longsword", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Maul", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Morningstar", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Pike", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Rapier", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Scimitar", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Shortsword", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Trident", "Martial Weapon"))
        p_list.append(ProficiencyLookup("War pick", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Warhammer", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Whip", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Blowgun", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Heavy Crossbow", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Longbow", "Martial Weapon"))
        p_list.append(ProficiencyLookup("Net", "Martial Weapon"))
        # Armor Proficiencies
        p_list.append(ProficiencyLookup("Light Armor", "Armor"))
        p_list.append(ProficiencyLookup("Medium Armor", "Armor"))
        p_list.append(ProficiencyLookup("Heavy Armor", "Armor"))
        p_list.append(ProficiencyLookup("Shield", "Armor"))

        for p in p_list:
            db.session.add(p)
            db.session.commit()



    def add_equipment(self, db):
        e_list = []
        # Currency
        e_list.append(EquipmentLookup("CP", "Currency", 1/50, 1/100, "Copper piece(s)",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("SP", "Currency", 1/50, 1/10, "Silver piece(s)",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("EP", "Currency", 1/50, 1/2, "Electrum piece(s)",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("GP", "Currency", 1/50, 1, "Gold piece(s)",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("PP", "Currency", 1/50, 10, "Platinum piece(s)",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, a_cat,\
        a_bonus, a_dis, a_str))
        # Armor (Light)
        e_list.append(EquipmentLookup("Padded", "Armor", 8, 5, "Padded armor consists of quilted layers of cloth and batting",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Light",\
        1, True, a_str))
        e_list.append(EquipmentLookup("Leather", "Armor", 10, 10, "The breastplate and shoulder protectors of this armor are made of leather that has been stiffened by being boiled in oil. The rest of the armor is made of softer and more flexible materials.",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Light",\
        1, a_dis, a_str))
        e_list.append(EquipmentLookup("Studded Leather", "Armor", 13, 45, "Made from rough but flexible leather, studded leather is reinforced with close-set rivets or spikes.",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Light",\
        2, a_dis, a_str))
        # Armor (Medium)
        e_list.append(EquipmentLookup("Hide", "Armor", 12, 10, "This crude armor consists of thick furs and pelts. It is commonly worn by barbarian tribes, evil humanoids, and other folk who lack access to the tools and materials needed to create better",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Medium",\
        2, a_dis, a_str))
        e_list.append(EquipmentLookup("Chain shirt", "Armor", 20, 50, "Made of interlocking metal rings, a chain shirt is worn between layers of clothing or leather. This armor offers modest protection to the wearer's upper body and allows the sound of the rings rubbing against one another to be muffled by outer layers.",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Medium",\
        3, a_dis, a_str))
        e_list.append(EquipmentLookup("Scale mail", "Armor", 45, 50, "This armor consists of a coat and leggings (and perhaps a separate skirt) of leather covered with overlapping pieces of metal, much like the scales of a fish. The suit includes gauntlets.",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Medium",\
        4, True, a_str))
        e_list.append(EquipmentLookup("Breastplate", "Armor", 20, 400, "This armor consists of a fitted metal chest piece worn with supple leather. Although it leaves the legs and arms relatively unprotected, this armor provides good protection for the wearer's vital organs while leaving the wearer relatively unencumbered.",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Medium",\
        4, a_dis, a_str))
        e_list.append(EquipmentLookup("Half plate", "Armor", 40, 750, "Half plate consists of shaped metal plates that cover most of the wearer's body. It does not include leg protection beyond simple greaves that are attached with leather straps.",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Medium",\
        5, True, a_str))
        # Armor (Heavy)
        e_list.append(EquipmentLookup("Ring mail", "Armor", 40, 30, "This armor is leather with heavy rings sewn into it. The rings help reinforce the armor against blows from swords and axes. Ring mail is inferior to chain mail, and it's usually only worn by those who cannot afford better armor.",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Heavy",\
        4, True, a_str))
        e_list.append(EquipmentLookup("Chain mail", "Armor", 55, 75, "Made of interlocking metal rings, chain mail includes a layer of quilted fabric worn underneath the mail to prevent chafing and to cushion the impact of blows. The suit includes gauntlets.",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Heavy",\
        6, True, 13))
        e_list.append(EquipmentLookup("Splint", "Armor", 60, 200, "This armor is made of narrow vertical strips of metal riveted to a backing of leather that is worn over cloth padding. Flexible chain mail protects the joints.",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Heavy",\
        7, True, 15))
        e_list.append(EquipmentLookup("Plate", "Armor", 65, 1500, "Plate consists of shaped, interlocking metal plates to cover the entire body. A suit of plate includes gauntlets, heavy leather boots, a visored helmet, and thick layers of padding underneath the armor. Buckles and straps distribute the weight over the body.",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Heavy",\
        8, True, 15))
        e_list.append(EquipmentLookup("Shield", "Armor", 6, 10, "A shield is made from wood or metal and carried in one hand. Weilding a shield increases your Armor Class by 2. You can benefit from only one shield at a time.",\
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, "Shield",\
        2, a_dis, a_str))
        # Weapons (Simple Melee)
        e_list.append(EquipmentLookup("Club", "Weapon", 2, 1/10, e_desc,\
        "Simple", w_range_bool, w_thrown, w_range, "Light", "1d4", "bludgeoning", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Dagger", "Weapon", 2, 2, e_desc,\
        "Simple", w_range_bool, True, "20/60", "Finesse,Light,Thrown", "1d4", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Greatclub", "Weapon", 10, 2/10, e_desc,\
        "Simple", w_range_bool, w_thrown, w_range, "Two-handed", "1d8", "bludgeoning", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Handaxe", "Weapon", 2, 5, e_desc,\
        "Simple", w_range_bool, True, "20/60", "Light,Thrown", "1d6", "slashing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Javelin", "Weapon", 2, 5/10, e_desc,\
        "Simple", w_range_bool, True, "30/120", "Thrown", "1d6", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Light hammer", "Weapon", 2, 2, e_desc,\
        "Simple", w_range_bool, True, "20/60", "Light,Thrown", "1d4", "bludgeoning", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Mace", "Weapon", 4, 5, e_desc,\
        "Simple", w_range_bool, w_thrown, w_range, w_props, "1d6", "bludgeoning", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Quarterstaff", "Weapon", 4, 2/10, e_desc,\
        "Simple", w_range_bool, w_thrown, w_range, "Versatile", "1d6|1d8", "bludgeoning", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Sickle", "Weapon", 2, 1, e_desc,\
        "Simple", w_range_bool, w_thrown, w_range, "Light", "1d4", "slashing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Spear", "Weapon", 3, 1, e_desc,\
        "Simple", w_range_bool, w_thrown, w_range, "Thrown,Versatile", "1d6|1d8", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Unarmed strike", "Weapon", 0, 0, e_desc,\
        "Simple", w_range_bool, w_thrown, w_range, "Light", "1", "bludgeoning", a_cat,\
        a_bonus, a_dis, a_str))
        # Weapons (Simple Ranged)
        e_list.append(EquipmentLookup("Light Crossbow", "Weapon", 5, 25, e_desc,\
        "Simple", True, w_thrown, "80/320", "Ammunition,Loading,Two-handed", "1d8", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Dart", "Weapon", 1/4, 5/100, e_desc,\
        "Simple", True, True, "20/60", "Finesse,Thrown", "1d4", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Shortbow", "Weapon", 2, 25, e_desc,\
        "Simple", True, w_thrown, "80/320", "Ammunition,Two-handed", "1d6", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Sling", "Weapon", 0, 1/10, e_desc,\
        "Simple", True, w_thrown, "30/120", "Ammunition", "1d6", "bludgeoning", a_cat,\
        a_bonus, a_dis, a_str))
        # Weapons (Martial Melee)
        e_list.append(EquipmentLookup("Battleaxe", "Weapon", 4, 10, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Versatile", "1d8|1d10", "slashing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Flail", "Weapon", 2, 10, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, w_props, "1d8", "bludgeoning", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Glaive", "Weapon", 6, 20, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Heavy,Reach,Two-handed", "1d10", "slashing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Greataxe", "Weapon", 7, 30, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Heavy,Two-handed", "1d10", "slashing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Greatsword", "Weapon", 6, 50, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Heavy,Two-handed", "2d6", "slashing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Halberd", "Weapon", 6, 20, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Heavy,Reach,Two-handed", "1d10", "slashing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Lance", "Weapon", 6, 10, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Reach,Special", "1d12", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Longsword", "Weapon", 3, 15, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Versatile", "1d8|1d10", "slashing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Maul", "Weapon", 10, 10, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Heavy,Two-handed", "2d6", "bludgeoning", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Morningstar", "Weapon", 15, 4, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, w_props, "1d8", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Pike", "Weapon", 18, 5, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Heavy,Reach,Two-handed", "1d10", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Rapier", "Weapon", 2, 25, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Finesse", "1d8", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Scimitar", "Weapon", 3, 25, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Finesse,Light", "1d6", "slashing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Shortsword", "Weapon", 2, 10, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Finesse,Light", "1d6", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Trident", "Weapon", 4, 5, e_desc,\
        "Martial", w_range_bool, True, "20/60", "Thrown,Versatile", "1d6|1d8", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("War pick", "Weapon", 2, 5, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, w_props, "1d8", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Warhammer", "Weapon", 2, 15, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Versatile", "1d8|1d10", "bludgeoning", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Whip", "Weapon", 3, 2, e_desc,\
        "Martial", w_range_bool, w_thrown, w_range, "Finesse,Reach", "1d4", "slashing", a_cat,\
        a_bonus, a_dis, a_str))
        # Weapon (Martial Ranged)
        e_list.append(EquipmentLookup("Blowgun", "Weapon", 1, 10, e_desc,\
        w_cat, True, w_thrown, "25/100", "Ammunition,Loading", "1", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Hand Crossbow", "Weapon", 3, 75, e_desc,\
        w_cat, True, w_thrown, "30/120", "Ammunition,Light,Loading", "1d6", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Heavy Crossbow", "Weapon", 18, 50, e_desc,\
        w_cat, True, w_thrown, "100/400", "Ammunition,Heavy,Loading,Two-handed", "1d10", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Longbow", "Weapon", 2, 50, e_desc,\
        w_cat, True, w_thrown, "150/600", "Ammunition,Heavy,Two-handed", "1d8", "piercing", a_cat,\
        a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Net", "Weapon", 3, 1, e_desc,\
        w_cat, True, True, "5/15", "Special,Thrown", w_damage, w_type, a_cat,\
        a_bonus, a_dis, a_str))
        # Adventuring Gear
        e_list.append(EquipmentLookup("Abacus", "Gear", 2, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Acid (vial)", "Gear", 1, 25, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Alchemist's fire (flask)", "Gear", 1, 50, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        # Ammunition
        e_list.append(EquipmentLookup("Arrow", "Ammunition", 1/20, 1/20, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Blowgun needle", "Ammunition", 1/50, 1/50, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Crossbow bolt", "Ammunition", 1.5/20, 1/20, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Sling bullet", "Aummunition", 1.5/20, 4/2000, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        # Gear
        e_list.append(EquipmentLookup("Antitoxin vial", "Gear", 0, 50, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Crystal", "Gear", 1, 10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        # Arcane focus
        e_list.append(EquipmentLookup("Orb", "Arcane focus", 3, 20, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Rod", "Arcane focus", 2, 10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Staff", "Arcane focus", 4, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Wand", "Arcane focus", 1, 10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        # Gear
        e_list.append(EquipmentLookup("Backpack", "Gear", 5, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Ball bearings (bag of 1,000)", "Gear", 2, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Barrel", "Gear", 70, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Basket", "Gear", 2, 4/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Bedroll", "Gear", 7, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Bell", "Gear", 0, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Blanket", "Gear", 3, 5/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Block and tackle", "Gear", 5, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Book", "Gear", 5, 25, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Bottle (glass)", "Gear", 2, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Bucket", "Gear", 2, 5/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Caltrops (bag of 20))", "Gear", 2, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Candle", "Gear", 0, 1/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Case (crossbow bolt)", "Gear", 1, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Case (map or scroll)", "Gear", 1, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Chain (10 ft)", "Gear", 10, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Chalk (1 piece)", "Gear", 0, 1/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Chest", "Gear", 25, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Climber's kit", "Gear", 12, 25, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Clothes, common", "Gear", 3, 5/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Clothes, costume", "Gear", 4, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Clothes, fine", "Gear", 6, 15, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Clothes, traveler's", "Gear", 4, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Component pouch", "Gear", 2, 25, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Crowbar", "Gear", 5, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        # Druidic focus
        e_list.append(EquipmentLookup("Sprig of mistletoe", "Druidic focus", 0, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Totem", "Druidic focus", 0, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Wooden staff", "Druidic focus", 4, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Yew wand", "Druidic focus", 1, 10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        # Gear
        e_list.append(EquipmentLookup("Fishing tackle", "Gear", 4, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Flask", "Gear", 1, 2/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Tankard", "Gear", 1, 2/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Grappling hook", "Gear", 4, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Hammer", "Gear", 3, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Hammer, sledge", "Gear", 10, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Healer's kit", "Gear", 3, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        # Holy symbol
        e_list.append(EquipmentLookup("Amulet", "Holy symbol", 1, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Emblem", "Holy symbol", 0, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Reliquary", "Holy symbol", 2, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        # Gear
        e_list.append(EquipmentLookup("Holy water (flask)", "Gear", 1, 25, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Hourglass", "Gear", 1, 25, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Hunting trap", "Gear", 25, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Ink (1 ounce bottle)", "Gear", 0, 10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Ink pen", "Gear", 0, 2/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Jug or pitcher", "Gear", 4, 2/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Ladder (10 ft)", "Gear", 25, 1/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Lamp", "Gear", 1, 5/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Lantern, bullseye", "Gear", 2, 10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Lantern, hooded", "Gear", 2, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Lock", "Gear", 1, 10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Magnifying glass", "Gear", 0, 100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Manacles", "Gear", 6, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Mess kit", "Gear", 1, 2/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Mirror, steel", "Gear", 1/2, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Oil (flask)", "Gear", 1, 1/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Sheet of Paper", "Gear", 0, 2/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Sheet of Parchment", "Gear", 0, 1/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Perfume (vial)", "Gear", 0, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Pick, miner's", "Gear", 10, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Piton", "Gear", 1/4, 5/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Poison, basic", "Gear", 0, 100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Pole (10 ft)", "Gear", 7, 5/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Pot, iron", "Gear", 10, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Potion of healing", "Gear", 1/2, 50, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Pouch", "Gear", 1, 5/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Quiver", "Gear", 1, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Ram, portable", "Gear", 35, 4, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Rations (1 day)", "Gear", 2, 5/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Robes", "Gear", 4, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Rope, hempen (50 ft)", "Gear", 10, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Rope, silk (50 ft)", "Gear", 5, 10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Sack", "Gear", 1/2, 1/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Scale, merchant's", "Gear", 3, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Sealing wax", "Gear", 0, 5/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Shovel", "Gear", 5, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Signal whistle", "Gear", 0, 5/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Signet ring", "Gear", 0, 5, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Soap", "Gear", 0, 2/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Spellbook", "Gear", 3, 50, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Spikes, iron (10)", "Gear", 5, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Spyglass", "Gear", 1, 1000, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Tent, two-person", "Gear", 20, 2, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Tinderbox", "Gear", 1, 5/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Torch", "Gear", 1, 1/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Vial", "Gear", 0, 1, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Waterskin", "Gear", 5, 2/10, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        e_list.append(EquipmentLookup("Whetstone", "Gear", 1, 1/100, e_desc, \
        w_cat, w_range_bool, w_thrown, w_range, w_props, w_damage, w_type, \
        a_cat, a_bonus, a_dis, a_str))
        
        for e in e_list:
            db.session.add(e)
            db.session.commit()



    def add_spells(self, db):
        s_list = []
        # A
        s_list.append(SpellLookup("Acid Splash", 0, "Conjuration", "1 action", "60 ft", "Instant", \
        s_conc, True, True, s_material, s_mat_desc, s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Aid", 2, "Abjuration", "1 action", "30 ft", "8 hours", \
        s_conc, True, True, True, "a tiny strip of white cloth", s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Alarm", 1, "Abjuration", "1 action", "30 ft", "8 hours", \
        s_conc, True, True, True, "a tiny bell and a piece of fine silver wire", True, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Alter Self", 2, "Transmutation", "1 action", "Self", "1 hour", \
        True, True, True, s_material, s_mat_desc, s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Animal Friendship", 1, "Enchantment", "1 action", "30 ft", "24 hours", \
        s_conc, True, True, True, "a morsel of food", s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Animal Messenger", 2, "Enchantment", "1 action", "30 ft", "24 hours", \
        s_conc, True, True, True, "a morsel of food", True, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Animal Shapes", 8, "Transmutation", "1 action", "30 ft", "24 hours", \
        True, True, True, s_material, s_mat_desc, s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Animate Dead", 3, "Necromancy", "1 minute", "10 ft", "Instant", \
        s_conc, True, True, True, "a drop of blood, a piece of flesh, and a pinch of bone dust", s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Animate Objects", 5, "Transmutation", "1 action", "120 ft", "1 minute", \
        True, True, True, s_material, s_mat_desc, s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Antilife Shell", 5, "Abjuration", "1 action", "Self (10 ft radius)", "1 hour", \
        True, True, True, s_material, s_mat_desc, s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Antimagic Field", 8, "Abjuration", "1 action", "Self (10 ft radius)", "1 hour", \
        True, True, True, True, "a pinch of powdered iron or iron filings", s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Antipathy/Sympathy", 8, "Enchantment", "1 hour", "60 ft", "10 days", \
        s_conc, True, True, True, "either a lump of alum soaked in vinegar for Antipathy or a drop of honey for Sympathy", s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Arcane Eye", 4, "Divination", "1 action", "30 ft", "1 hour", \
        True, True, True, True, "a bit of bat fur", s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup("Arcane Gate", 6, "Conjuration", "1 action", "500 ft", "10 minutes", \
        True, True, True, s_material, s_mat_desc, s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup(s_name, s_level, s_school, s_cast, s_range, s_duration, \
        s_conc, s_verbal, s_somatic, s_material, s_mat_desc, s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))
        s_list.append(SpellLookup(s_name, s_level, s_school, s_cast, s_range, s_duration, \
        s_conc, s_verbal, s_somatic, s_material, s_mat_desc, s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))



        s_list.append(SpellLookup(s_name, s_level, s_school, s_cast, s_range, s_duration, \
        s_conc, s_verbal, s_somatic, s_material, s_mat_desc, s_ritual, \
        s_bard, s_druid, s_cleric, s_paladin, s_ranger, s_sorcerer, s_warlock, s_wizard, \
        s_spell_desc))




        for s in s_list:
            db.session.add(s)
            db.session.commit()