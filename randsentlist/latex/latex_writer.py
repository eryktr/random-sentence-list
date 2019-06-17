from randsentlist.latex.tag import Tag


class LatexWriter:
    def __init__(self):
        self._current_indent = 0
        self._lines = {
            Tag.DOCUMENTCLASS: 'documentclass{{article}}',
            Tag.PACKAGE: 'usepackage{{{}}}',
            Tag.COMPOSITE_PACKAGE: 'usepackage[{}]{{{}}}',
            Tag.BEGIN_DOCUMENT: 'begin{{document}}',
            Tag.END_DOCUMENT: 'end{{document}}',
            Tag.BEGIN_ENUM: 'begin{{enumerate}}',
            Tag.END_ENUM: 'end{{enumerate}}',
            Tag.ITEM: 'item{{{}}}',
        }
        self._packages = set()
        self._composite_packages = set()
        self._fd = None

    @property
    def indent(self):
        return self._current_indent * '\t'

    def _line(self, line, *args):
        if line not in self._lines:
            raise ValueError(f"{line} is not a supported LaTeX expression.")
        return f"{self.indent}" + '\\' + self._lines[line].format(*args) + "\n"

    def _increase_indent(self):
        self._current_indent += 1

    def _decrease_indent(self):
        self._current_indent -= 1

    def _write_documentclass(self):
        self._fd.write(self._line(Tag.DOCUMENTCLASS))

    def _write_begin_document(self):
        self._fd.write(self._line(Tag.BEGIN_DOCUMENT))
        self._increase_indent()

    def _write_end_document(self):
        self._decrease_indent()
        self._fd.write(self._line(Tag.END_DOCUMENT))

    def _write_begin_enum(self):
        self._fd.write(self._line(Tag.BEGIN_ENUM))
        self._increase_indent()

    def _write_end_enum(self):
        self._decrease_indent()
        self._fd.write(self._line(Tag.END_ENUM))

    def _write_item(self, item):
        self._fd.write(self._line(Tag.ITEM, item))

    def _write_iterable(self, iterable):
        self._write_begin_enum()
        for item in iterable:
            self._write_item(item)
        self._write_end_enum()

    def _write_packages(self):
        for package in self._packages:
            self._write_package(package)

    def _write_package(self, package):
        self._fd.write(self._line(Tag.PACKAGE, package))

    def _write_composite_packages(self):
        for (generic, package) in self._composite_packages:
            self._write_composite_package(generic, package)

    def _write_composite_package(self, generic, package):
        self._fd.write(self._line(Tag.COMPOSITE_PACKAGE, generic, package))

    def write_iterable_to_latex_file(self, iterable, filename):
        with open(filename, "w") as self._fd:
            self._write_documentclass()
            self._write_packages()
            self._write_composite_packages()
            self._write_begin_document()
            self._write_iterable(iterable)
            self._write_end_document()

    def add_packages(self, packages):
        for package in packages:
            self._packages.add(package)

    def add_composite_packages(self, packages):
        for (generic, package) in packages:
            self._composite_packages.add((generic, package))
