from unittest.mock import MagicMock, call

from randsentlist.latex.latex_writer import LatexWriter


class TestLatexWriter:
    def setup_method(self):
        self.latex_writer = LatexWriter("tmp.tex")
        self.latex_writer._fd = MagicMock()

    def test_write_documentclass(self):
        self.latex_writer._write_documentclass()
        self.latex_writer._fd.write.assert_called_with("\\documentclass{article}\n")

    def test_write_begin_document(self):
        initial_indent = self.latex_writer.indent
        self.latex_writer._write_begin_document()
        self.latex_writer._fd.write.assert_called_with("\\begin{document}\n")
        assert self.latex_writer.indent == initial_indent + "\t"

    def test_write_end_document(self):
        initial_indent = self.latex_writer.indent
        self.latex_writer._write_end_document()
        expected_indent = initial_indent[:-2]
        self.latex_writer._fd.write.assert_called_with(f"{expected_indent}\\end{{document}}\n")

    def test_write_begin_enum(self):
        initial_indent = self.latex_writer.indent
        self.latex_writer._write_begin_enum()
        expected_indent = "\t" + initial_indent
        self.latex_writer._fd.write.assert_called_with(f"{initial_indent}\\begin{{enumerate}}\n")
        assert self.latex_writer.indent == expected_indent

    def test_write_end_enum(self):
        initial_indent = self.latex_writer.indent
        self.latex_writer._write_end_enum()
        expected_indent = initial_indent[:-2]
        self.latex_writer._fd.write.assert_called_with(f"{expected_indent}\\end{{enumerate}}\n")

    def test_add_packages(self):
        start_count = len(self.latex_writer._packages)
        self.latex_writer.add_packages(['dummy', 'bummy'])
        end_count = len(self.latex_writer._packages)
        assert end_count - start_count == 2

    def test_add_package_repetition(self):
        start_count = len(self.latex_writer._packages)
        self.latex_writer.add_packages(['dummy', 'dummy'])
        end_count = len(self.latex_writer._packages)
        assert end_count - start_count == 1

    def test_add_composite_package(self):
        start_count = len(self.latex_writer._composite_packages)
        self.latex_writer.add_composite_packages([('a', 'dummy'), ('b', 'bummy')])
        end_count = len(self.latex_writer._composite_packages)
        assert end_count - start_count == 2

    def test_write_package(self):
        self.latex_writer._write_package("dummy")
        self.latex_writer._fd.write.assert_called_with("\\usepackage{dummy}\n")

    def test_write_composite_package(self):
        self.latex_writer._write_composite_package("foo", "bar")
        self.latex_writer._fd.write.assert_called_with("\\usepackage[foo]{bar}\n")

    def test_write_packages(self):
        self.latex_writer._packages = {"foo", "bar"}
        self.latex_writer._write_package = MagicMock()
        self.latex_writer._write_packages()
        self.latex_writer._write_package.assert_any_call("foo")
        self.latex_writer._write_package.assert_any_call("bar")

    def test_write_composite_packages(self):
        self.latex_writer._packages = {('f', 'foo'), ('b', "bar")}
        self.latex_writer._write_package = MagicMock()
        self.latex_writer._write_packages()
        self.latex_writer._write_package.assert_any_call(("f", "foo"))
        self.latex_writer._write_package.assert_any_call(("b", "bar"))

    def test_write_item(self):
        self.latex_writer._write_item("dummy")
        self.latex_writer._fd.write.assert_called_with(f"{self.latex_writer.indent}\\item{{dummy}}\n")

    def test_write_iterable(self):
        self.latex_writer._write_item = MagicMock()
        self.latex_writer._write_iterable(['q', 'm', 'p'])
        calls = [call('q'), call('m'), call('p')]
        self.latex_writer._write_item.assert_has_calls(calls)
