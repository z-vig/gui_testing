"""
Defines the main file tree widget for the app.
"""

import logging
from pathlib import Path
from typing import Self
from dataclasses import dataclass, field

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTreeWidget,
)

log = logging.getLogger(__name__)


@dataclass
class DirectoryNode:
    root: Path
    files: list[Path] = field(default_factory=list)
    subdirectories: list[Self] = field(default_factory=list)

    def to_dict(self) -> dict[str, list[str | dict]]:
        file_dict: dict[str, list[str | dict]] = {}
        file_dict[self.root.name] = []

        for file in self.files:
            file_dict[self.root.name].append(file.name)

        for subdir in self.subdirectories:
            file_dict[self.root.name].append(subdir.to_dict())

        return file_dict


def walk(base_directory: Path | str) -> DirectoryNode:
    # ==== Validation ====
    if not (basepath := Path(base_directory)).is_dir():
        log.critical(f"{basepath} is not a directory.")
        raise ValueError(f"{basepath} is not a directory.")
    base_node = DirectoryNode(basepath)

    for p in base_node.root.iterdir():
        if p.is_dir():
            sub_node = walk(p)
            base_node.subdirectories.append(sub_node)
        else:
            base_node.files.append(p)

    return base_node


class FileTree(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout()

        self._tree = QTreeWidget()
        layout.addWidget(self._tree)

        node = walk("C:/Users/zacha/walk_test/")
        print(node.to_dict())

        self.setLayout(layout)

        log.info("FileTree Widget Initialized")
