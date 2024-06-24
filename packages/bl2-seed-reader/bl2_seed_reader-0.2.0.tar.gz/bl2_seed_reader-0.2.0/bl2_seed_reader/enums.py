from blib import StrEnum


class Dlc(StrEnum):
	"Name of the DLC"

	BASE = "Borderlands 2"
	SCARLETT = "Captain Scarlett and her Pirate's Booty"
	TORGUE = "Mr. Torgue's Campaign of Carnage"
	HAMMERLOCK = "Sir Hammerlock's Big Game Hunt"
	TINA = "Tiny Tina's Assault on Dragon Keep"
	LILITH = "Commander Lilith & the Fight for Sanctuary"
	PEAK = "Ultimate Vault Hunter Upgrade Pack 2"

	# headhunters
	HARVEST = "Headhunter 1: Bloody Harvest"
	GOBBLER = "Headhunter 2: Wattle Gobbler"
	MARCUS = "Headhunter 3: Mercenary Day"
	WEDDING = "Headhunter 4: Wedding Day Massacre"
	CRAWMERAX = "Headhunter 5: Son of Crawmerax"


class DropType(StrEnum):
	"Type of the drop source"

	ENEMY = "Enemy"
	MISSION = "Mission"
	OTHER = "Other"
