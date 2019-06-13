class LatexWriter:
    def __init__(self, outfile):
        self._current_indent = 0
        self._outfile = outfile
        self._lines = {
            'documentclass': 'documentclass{{article}}',
            'package': 'usepackage{{ {} }}',
            'composite_package': 'usepackage[{}]{{ {} }}',
            'begin_document': 'begin{{document}}',
            'end_document': 'end{{document}}',
            'begin_enum': 'begin{{enumerable}}',
            'end_enum': 'end{{enumerable}}',
            'item': 'item{{ {} }}',
        }
        self._packages = []
        self._composite_packages = []

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

    def _write_documentclass(self, fd):
        fd.write(self._line('documentclass'))

    def _write_begin_document(self, fd):
        fd.write(self._line('begin_document'))
        self._increase_indent()

    def _write_end_document(self, fd):
        fd.write(self._line('end_document'))
        self._decrease_indent()

    def _write_begin_enum(self, fd):
        fd.write(self._line('begin_enum'))
        self._increase_indent()

    def _write_end_enum(self, fd):
        fd.write(self._line('end_enum'))
        self._decrease_indent()

    def _write_item(self, item, fd):
        fd.write(self._line('item', item))

    def _write_iterable(self, iterable, fd):
        self._write_begin_enum(fd)
        for item in iterable:
            self._write_item(item, fd)
        self._decrease_indent()
        self._write_end_enum(fd)

    def _write_packages(self, fd):
        for package in self._packages:
            fd.write(self._line('package', package))

    def _write_composite_packages(self, fd):
        for (generic, package) in self._composite_packages:
            fd.write(self._line('composite_package', generic, package))

    def write_iterable_to_latex_file(self, iterable):
        with open(self._outfile, "w") as fd:
            self._write_documentclass(fd)
            self._write_packages(fd)
            self._write_composite_packages(fd)
            self._write_begin_document(fd)
            self._write_iterable(iterable, fd)
            self._write_end_document(fd)

    def add_packages(self, packages):
        for package in packages:
            self._packages.append(package)

    def add_composite_packages(self, packages):
        for (generic, package) in packages:
            self._composite_packages.append((generic, package))
