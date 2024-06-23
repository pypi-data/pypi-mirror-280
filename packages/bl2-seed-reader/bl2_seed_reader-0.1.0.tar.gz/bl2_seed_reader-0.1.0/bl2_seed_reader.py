from collections.abc import Iterator
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Self


TRUE_STR = ['on', 'y', 'yes', 'true', 'enable', 'enabled', '1']
FALSE_STR = ['off', 'n', 'no', 'false', 'disable', 'disable', '0']

DLC_TEMPLATE = "{name}\n{items}"

SEED_TEMPLATE = """Loot Randomizer Seed {name}

Total locations: {location_count}
Total items: {item_count}

{settings}

{items}
"""

SETTINGS_TEMPLATE = """Base Game: {base_game}
Pirate's Booty: {pirates_booty}
Campaign Of Carnage: {campaign_of_carnage}
Hammerlock's Hunt: {hammerlocks_hunt}
Dragon Keep: {dragon_keep}
Fight For Sanctuary: {fight_for_sanctuary}
Bloody Harvest: {bloody_harvest}
Wattle Gobbler: {wattle_gobbler}
Mercenary Day: {mercenary_day}
Wedding Day Massacre: {wedding_day_massacre}
Son Of Crawmerax: {son_of_crawmerax}
UVHM Pack: {uvhm_pack}
Digistruct Peak: {digistruct_peak}
Short Missions: {short_missions}
Long Missions: {long_missions}
Very Long Missions: {very_long_missions}
Slaughter Missions: {slaughter_missions}
Unique Enemies: {unique_enemies}
Slow Enemies: {slow_enemies}
Rare Enemies: {rare_enemies}
Very Rare Enemies: {very_rare_enemies}
Mob Farms: {mob_farms}
Raid Enemies: {raid_enemies}
Mission Enemies: {mission_enemies}
Evolved Enemies: {evolved_enemies}
Digistruct Enemies: {digistruct_enemies}
Special Vendors: {special_vendors}
Miscellaneous: {miscellaneous}
Duplicate Items: {duplicate_items}
Allow Hints: {allow_hints}"""


def convert_to_boolean(value: Any) -> bool:
	if value is None:
		return False

	if isinstance(value, bool):
		return value

	if isinstance(value, str):
		if value.lower() in TRUE_STR:
			return True

		if value.lower() in FALSE_STR:
			return False

	if isinstance(value, int):
		if value == 1:
			return True

		if value == 0:
			return False

	return bool(value)


class StrEnum(str, Enum):
	@classmethod
	def parse(cls: type[Self], data: Self | str) -> Self:
		"""
			Get an enum item by name or value

			:param data: Name or value
			:raises AttributeError: If an item could not be found
		"""

		if isinstance(data, cls):
			return data

		try:
			return cls[data]

		except KeyError:
			pass

		try:
			return cls(data)

		except ValueError:
			pass

		for item in cls:
			if data.lower() == item.value.lower():
				return item

			if data.lower() == item.name.lower():
				return item

		raise AttributeError(f'Invalid enum property for {cls.__name__}: {data}')


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


@dataclass(slots = True)
class SeedItem:
	"Loot source for the seed"

	dlc: Dlc
	drop_type: DropType
	name: str
	value: str | None = None


	@classmethod
	def parse(cls: type[Self], dlc: Dlc | str, line: str) -> Self:
		"""
			Read a loot source line and parse it

			:param dlc: DLC the loot source is from
			:param line: Raw loot source line to parse
			:raises ValueError: When the line cannot be parsed
		"""

		drop_type, data = line.split(": ", 1)
		key, _, value = data.partition(" - ")

		return cls(
			Dlc.parse(dlc),
			DropType.parse(drop_type),
			key.strip(),
			value.strip() or None
		)


	def match(self,
			dlc: Dlc | None = None,
			drop_type: DropType | str | None = None,
			name: str | None = None,
			value: str | None = "NOVALUE") -> bool:
		"""
			Check if some search parameters match the item. At least one parameter must be
			specified.

			:param dlc: DLC the item is in
			:param drop_type: The type of drop source the item comes from
			:param name: Text that appears in the name of the drop source
			:param value: Text that appears in the name of the item drop
		"""

		if drop_type is not None:
			drop_type = DropType.parse(drop_type)

		if not any([dlc, drop_type, name]) and value == "NOVALUE":
			raise ValueError("Must specify at least one parameter")

		if dlc is not None and dlc != self.dlc:
			return False

		if drop_type is not None and drop_type != self.drop_type:
			return False

		if name is not None and name.lower() not in self.name.lower():
			return False

		if value != "NOVALUE":
			if isinstance(value, str) and self.value is not None:
				if value.lower() not in self.value.lower():
					return False

			elif self.value is not None and value is None:
				return False

		return True


	def to_string(self) -> str:
		"Convert the item into a seed item string"

		if self.value is not None:
			return f"{self.drop_type.value}: {self.name} - {self.value}"

		return f"{self.drop_type.value}: {self.name}"


@dataclass(slots = True)
class SeedSettings:
	"Settings for the seed"

	base_game: bool = False
	pirates_booty: bool = False
	campaign_of_carnage: bool = False
	hammerlocks_hunt: bool = False
	dragon_keep: bool = False
	fight_for_sanctuary: bool = False
	bloody_harvest: bool = False
	wattle_gobbler: bool = False
	mercenary_day: bool = False
	wedding_day_massacre: bool = False
	son_of_crawmerax: bool = False
	uvhm_pack: bool = False
	digistruct_peak: bool = False
	short_missions: bool = False
	long_missions: bool = False
	very_long_missions: bool = False
	slaughter_missions: bool = False
	unique_enemies: bool = False
	slow_enemies: bool = False
	rare_enemies: bool = False
	very_rare_enemies: bool = False
	mob_farms: bool = False
	raid_enemies: bool = False
	mission_enemies: bool = False
	evolved_enemies: bool = False
	digistruct_enemies: bool = False
	special_vendors: bool = False
	miscellaneous: bool = False
	duplicate_items: bool = False
	allow_hints: bool = False


	def to_string(self) -> str:
		"Convert to a settings block string"

		data = {key: ("On" if value else "Off") for key, value in asdict(self).items()}
		return SETTINGS_TEMPLATE.format(**data)


class Seed(list[SeedItem]):
	"Represents a seed file. Acts as a list to hold seed items."

	def __init__(self,
				name: str,
				*items: SeedItem,
				location_count: int = 0,
				item_count: int = 0,
				**kwargs: bool):
		"""
			Create a new ``Seed`` object

			:param name: Hash value of the seed
			:param items: Sequence of seed items part of the seed
			:param location_count: Number of locations randomized
			:param item_count: Number of items in the seed
			:param kwargs: Seed settings to pass to :class:`SeedSettings`
		"""

		list.__init__(self, items)

		self.name: str = name
		self.location_count: int = location_count
		self.item_count: int = item_count
		self.settings: SeedSettings = SeedSettings(**kwargs)


	@classmethod
	def from_file(cls: type[Self], path: Path | str) -> Self:
		"""
			Create a new ``Seed`` object from a seed file

			param path: Path to the seed file
		"""

		if not isinstance(path, Path):
			path = Path(path).expanduser().resolve()

		seed = cls("none")
		section: str = "headers"
		dlc: Dlc = Dlc.BASE

		with open(path, "r", encoding = "utf-8") as fd:
			for idx, line in enumerate(fd.read().split("\n")):
				line = line.strip()

				if line == "":
					continue

				if idx == 0:
					seed.name = line.split(" ")[-1]
					continue

				if idx == 2:
					seed.location_count = int(line.split(": ")[-1])
					continue

				if idx == 3:
					seed.item_count = int(line.split(": ")[-1])
					section = "config"
					continue

				if ":" not in line or line.lower().startswith("headhunter"):
					dlc = Dlc.parse(line)
					section = "items"
					continue

				if section == "config":
					key, value = line.split(":", 1)

					setattr(
						seed.settings,
						key.replace(" ", "_").replace("'", "").lower(),
						convert_to_boolean(value.strip())
					)

					continue

				seed.append(SeedItem.parse(dlc, line))

		return seed


	def find_items(self,
				dlc: Dlc | None = None,
				drop_type: DropType | str | None = None,
				name: str | None = None,
				value: str | None = "NOVALUE") -> Iterator[SeedItem]:
		"""
			Find items with the specified search criteria. Must include at least one parameter.
			Set ``value`` to ``None`` to find drops that do not have a value.

			:param dlc: DLC the item is in
			:param drop_type: The type of drop source the item comes from
			:param name: Text that appears in the name of the drop source
			:param value: Text that appears in the name of the item drop
		"""

		for item in self:
			if item.match(dlc, drop_type, name, value):
				yield item


	def to_string(self) -> str:
		"Conver the seed into seed file text"

		items: dict[Dlc, list[str]] = {}

		for item in self:
			if item.dlc not in items:
				items[item.dlc] = []

			items[item.dlc].append(item.to_string())

		str_items = []

		for key in items:
			str_items.append(DLC_TEMPLATE.format(name = key.value, items = "\n".join(items[key])))

		return SEED_TEMPLATE.format(
			name = self.name,
			location_count = self.location_count,
			item_count = self.item_count,
			settings = self.settings.to_string(),
			items = "\n\n".join(str_items)
		)
