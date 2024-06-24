from __future__ import annotations

import signal

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget
from collections.abc import Callable, Sequence
from blib import File
from importlib.resources import files as pkgfiles
from typing import Any, Generic, TypeVar

from PySide6.QtCore import (
	Qt,
	QAbstractTableModel,
	QModelIndex,
	QPersistentModelIndex,
	QSettings,
	QSortFilterProxyModel,
	QTimer
)

from PySide6.QtWidgets import (
	QTableView,
	QLineEdit,
	QPushButton,
	QComboBox,
	QFileDialog
)

from . import __version__
from .seed import Dlc, DropType, Seed, SeedItem


T = TypeVar("T")


def set_signal_handler(handler: Callable | None) -> None:
	for sig in ('SIGHUP', 'SIGINT', 'SIGQUIT', 'SIGTERM'):
		try:
			signal.signal(getattr(signal, sig), handler or signal.SIG_DFL)

		# some signals don't exist in windows, so skip them
		except AttributeError:
			pass


class SignalBlocker:
	def __init__(self, *widgets: QWidget) -> None:
		self.widgets: Sequence[QWidget] = widgets


	def __enter__(self):
		for widget in self.widgets:
			widget.blockSignals(True)

		return self


	def __exit__(self, *_: Any) -> None:
		for widget in self.widgets:
			widget.blockSignals(False)


class Widget(Generic[T]):
	def __init__(self, name: str, cls: type[T]):
		self.name = name
		self.cls = cls


	def __get__(self, app: Application | None, _: Any) -> T:
		if app is None:
			raise AttributeError("heck")

		return app.window.findChild(self.cls, self.name) # type: ignore[return-value]


class Model(QAbstractTableModel):
	def __init__(self, path: str):
		QAbstractTableModel.__init__(self)

		self.seed: Seed = Seed.from_file(path)


	def rowCount(self, index: QModelIndex | QPersistentModelIndex = QModelIndex()):
		return len(self.seed)


	def columnCount(self, index: QModelIndex | QPersistentModelIndex = QModelIndex()):
		return 4


	def data(self,
			index: QModelIndex | QPersistentModelIndex,
			role: Qt.ItemDataRole | int = Qt.ItemDataRole.DisplayRole) -> str | None:

		if not index.isValid():
			return None

		if not 0 <= index.row() < len(self.seed):
			return None

		if role != Qt.ItemDataRole.DisplayRole:
			return None

		item = self.seed[index.row()]

		if index.column() == 0:
			return item.name

		if index.column() == 1:
			return item.value or "Undiscovered"

		if index.column() == 2:
			return item.dlc.value

		if index.column() == 3:
			return item.drop_type.value

		return None


	def headerData(self,
					section: int,
					orientation: Qt.Orientation,
					role: Qt.ItemDataRole | int = Qt.ItemDataRole.DisplayRole) -> str | None:

		if role != Qt.ItemDataRole.DisplayRole:
			return None

		if orientation != Qt.Orientation.Horizontal:
			return None

		if section == 0:
			return "Name"

		if section == 1:
			return "Item"

		if section == 2:
			return "DLC"

		if section == 3:
			return "Type"

		return None


	def insertRows(self,
				position: int,
				rows: int = 1,
				index: QModelIndex | QPersistentModelIndex = QModelIndex()) -> bool:

		self.beginInsertRows(QModelIndex(), position, position + rows - 1)

		for idx in range(rows):
			self.seed.insert(position + idx, SeedItem(Dlc.BASE, DropType.OTHER, "", None))

		self.endInsertRows()
		return True


	def removeRows(self,
				position: int,
				rows: int = 1,
				index: QModelIndex | QPersistentModelIndex = QModelIndex()) -> bool:

		self.beginRemoveRows(QModelIndex(), position, position + rows - 1)

		del self.seed[position:position + rows]

		self.endRemoveRows()
		return True


	def setData(self,
				index: QModelIndex | QPersistentModelIndex,
				value: str,
				role: Qt.ItemDataRole | int = Qt.ItemDataRole.EditRole) -> bool:

		if role != Qt.ItemDataRole.EditRole:
			return False

		if index.isValid() and not 0 <= index.row() < len(self.seed):
			return False

		item = self.seed[index.row()]

		if index.column() == 0:
			item.name = value

		elif index.column() == 1:
			item.value = value

		elif index.column() == 2:
			item.dlc = Dlc.parse(value)

		elif index.column() == 3:
			item.drop_type = DropType.parse(value)

		else:
			return False

		self.dataChanged.emit(index, index, 0)
		return True


	def flags(self, index: QModelIndex | QPersistentModelIndex) -> Qt.ItemFlag:
		if not index.isValid():
			return Qt.ItemFlag.ItemIsEnabled

		return Qt.ItemFlag(QAbstractTableModel.flags(self, index) | Qt.ItemFlag.ItemIsEditable)


class SetProp(Generic[T]):
	key: str


	def __init__(self, default: T, cls: type[T]):
		self.default: T = default
		self.cls: type[T] = cls


	def __set_name__(self, _: Any, name: str) -> None:
		self.key = name


	def __get__(self, settings: AppSettings | None, _: Any = None) -> T:
		if settings is None:
			raise AttributeError("heck")

		if self.cls is File:
			return File(settings.value(self.key, str(self.default), str)).resolve() # type: ignore

		return settings.value(self.key, self.default, self.cls) # type: ignore[return-value]


	def __set__(self, settings: AppSettings, value: T) -> None:
		settings.setValue(self.key, value)


class AppSettings(QSettings):
	height: SetProp[int] = SetProp(600, int)
	width: SetProp[int] = SetProp(800, int)
	selected_seed: SetProp[str] = SetProp("", str)
	path: SetProp[File] = SetProp(
		File("~/.steam/steamapps/common/Borderlands 2/Binaries/Win32/Mods/LootRandomizer/Seeds"),
		File
	)


class Application(QApplication):
	path: Widget[QLineEdit] = Widget("path", QLineEdit)
	path_open: Widget[QPushButton] = Widget("path_open", QPushButton)
	items: Widget[QTableView] = Widget("items", QTableView)
	seeds: Widget[QComboBox] = Widget("seeds", QComboBox)
	refresh: Widget[QPushButton] = Widget("refresh", QPushButton)
	search: Widget[QLineEdit] = Widget("search", QLineEdit)

	window: QWidget


	def __init__(self):
		QApplication.__init__(self, [])

		self.setApplicationName("bl2-seed-viewer")
		self.setApplicationVersion(__version__)
		self.setOrganizationDomain("barkshark.xyz")
		self.setOrganizationName("barkshark")

		self.settings: AppSettings = AppSettings() # type: ignore[annotation-unchecked]


	def exec(self):
		self.setup()

		timer = QTimer()
		timer.timer_type = Qt.VeryCoarseTimer
		timer.timeout.connect(lambda *args: "uvu")
		timer.start(1)

		set_signal_handler(self.handle_unix_signal)
		QApplication.exec()
		set_signal_handler(None)


	def setup(self) -> None:
		self.window = QUiLoader().load(str(pkgfiles("bl2_seed_reader").joinpath("window.ui")))
		self.window.show()

		self.model = QSortFilterProxyModel()
		self.model.setDynamicSortFilter(True)
		self.model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
		self.model.setFilterKeyColumn(-1)
		self.items.setModel(self.model)

		self.path.setText(self.settings.path.resolve())
		self.handle_reload()

		self.refresh.clicked.connect(self.handle_reload)
		self.path_open.clicked.connect(self.handle_path_open)
		self.seeds.currentTextChanged.connect(self.handle_seed_change)
		self.search.textChanged.connect(self.model.setFilterFixedString)


	def handle_path_open(self) -> None:
		dialog = QFileDialog()
		dialog.setFileMode(QFileDialog.FileMode.Directory)

		if File(self.path.text()).exists:
			dialog.setDirectory(self.path.text())

		if dialog.exec():
			self.settings.path = File(dialog.selectedFiles()[0])
			self.path.setText(self.settings.path)
			self.handle_reload()


	def handle_reload(self, *_: Any) -> None:
		path = self.settings.path.resolve().join("Seed List.txt")

		if not path.exists:
			return

		with open(path, "r", encoding = "utf-8") as fd:
			lines = [line.strip() for line in fd.readlines() if line != "\n"]

		with SignalBlocker(self.seeds, self.items):
			while self.seeds.count() > 0:
				self.seeds.removeItem(0)

			self.seeds.addItems(lines)
			self.seeds.setCurrentText(self.settings.selected_seed)

			if self.seeds.count() > 0:
				self.handle_seed_change(self.settings.selected_seed)


	def handle_seed_change(self, seed: str) -> None:
		if not seed:
			self.model.setSourceModel(None) # type: ignore[arg-type]

		else:
			self.settings.selected_seed = seed
			self.model.setSourceModel(Model(f"{self.path.text()}/{seed}.txt"))

		self.items.setColumnWidth(0, 200)
		self.items.setColumnWidth(1, 200)
		self.items.setColumnWidth(2, 200)


	def handle_unix_signal(self, signum: int, _) -> None:
		self.quit()


def main():
	app = Application()
	app.exec()
