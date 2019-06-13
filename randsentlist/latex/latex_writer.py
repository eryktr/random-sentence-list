class LatexWriter:
    def __init__(self, outfile):
        self._current_indent = 0
        self.outfile = outfile
        self.lines = {
            'documentclass': 'documentclass{{article}}'.format,
            'package': 'usepackage{{ {} }}'.format,
            'composite_package': 'usepackage[{}]{{ {} }}.'.format,
            'begin_document': 'begin{{document}}'.format,
            'end_document': 'end{{document}}'.format,
            'begin_enum': 'begin{{enumerable}}'.format,
            'end_enum': 'end{{enumerable}}'.format,
            'item': 'item{{ {} }}'.format,
        }

    @property
    def indent(self):
        return self._current_indent * '\t'

    def _line(self, line, *args):
        if line not in self.lines:
            raise ValueError(f"{line} is not a supported LaTeX expression.")
        return f"{self.indent}" + '\\' + self.lines[line](*args) + "\n"

    def _increase_indent(self):
        self._current_indent += 1

    def _decrease_indent(self):
        self._current_indent -= 1

    def _write_documentclass(self, fd):
        fd.write(self._line('documentclass'))

    def _write_packages(self, package_list, fd):
        for package in package_list:
            fd.write(self._line('package', package))

    def _write_composite_packages(self, composite_package_list, fd):
        for (generic, package) in composite_package_list:
            fd.write(self._line('composite_package', generic, package))

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

    def write_iterable_to_latex_file(self, iterable):
        with open(self.outfile, "w") as fd:
            self._write_documentclass(fd)
            self._write_packages(['polski'], fd)
            self._write_composite_packages([('utf8', 'inputenc')], fd)
            self._write_begin_document(fd)
            self._write_iterable(iterable, fd)
            self._write_end_document(fd)
