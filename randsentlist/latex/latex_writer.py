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
        self._fd.write(self._line('documentclass'))

    def _write_begin_document(self):
        self._fd.write(self._line('begin_document'))
        self._increase_indent()

    def _write_end_document(self):
        self._fd.write(self._line('end_document'))
        self._decrease_indent()

    def _write_begin_enum(self):
        self._fd.write(self._line('begin_enum'))
        self._increase_indent()

    def _write_end_enum(self):
        self._fd.write(self._line('end_enum'))
        self._decrease_indent()

    def _write_item(self, item):
        self._fd.write(self._line('item', item))

    def _write_iterable(self, iterable):
        self._write_begin_enum()
        for item in iterable:
            self._write_item(item)
        self._decrease_indent()
        self._write_end_enum()

    def _write_packages(self):
        for package in self._packages:
            self._fd.write(self._line('package', package))

    def _write_composite_packages(self):
        for (generic, package) in self._composite_packages:
            self._fd.write(self._line('composite_package', generic, package))

    def write_iterable_to_latex_file(self, iterable):
        with open(self._outfile, "w") as self._fd:
            self._write_documentclass()
            self._write_packages()
            self._write_composite_packages()
            self._write_begin_document()
            self._write_iterable(iterable)
            self._write_end_document()

    def add_packages(self, packages):
        for package in packages:
            self._packages.append(package)

    def add_composite_packages(self, packages):
        for (generic, package) in packages:
            self._composite_packages.append((generic, package))