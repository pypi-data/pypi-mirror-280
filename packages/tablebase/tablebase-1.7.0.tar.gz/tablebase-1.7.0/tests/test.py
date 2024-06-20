import unittest
import tablebase
from os import remove


class TestTable(unittest.TestCase):
    def test_table_creation(self):
        test_table = tablebase.Table()
        self.assertEqual(test_table.table_content, [[]])

    def test_override_col(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        test_table.override_col("col2", [10, 9, 8])
        self.assertEqual(test_table.table_content, [["col1", "col2"], [11, 10], [21, 9], [31, 8]])

    def test_rename_col(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        test_table.rename_col("col1", "column1")
        test_table.rename_col("col2", "column2")
        self.assertEqual(test_table.table_content, [["column1", "column2"], [11, 12], [21, 22], [31, 32]])

    def test_del_col(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        test_table.del_col("col2")
        self.assertEqual(test_table.table_content, [["col1"], [11], [21], [31]])

    def test_get_col(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        self.assertEqual(test_table.get_col("col1"), [11, 21, 31])

    def test_add_expand(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        test_table.add_expand("col3", "@col2@ * 2")
        self.assertEqual(test_table.table_content, [["col1", "col2", "col3"], [11, 12, 24], [21, 22, 44], [31, 32, 64]])

    def test_expand(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        test_table.expand("col2", "@col2@ * 2")
        self.assertEqual(test_table.table_content, [["col1", "col2"], [11, 24], [21, 44], [31, 64]])

    def test_add_col_list(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        test_table.add_col("col3", [13, 23, 33])
        self.assertEqual(test_table.table_content, [["col1", "col2", "col3"], [11, 12, 13], [21, 22, 23], [31, 32, 33]])
    
    def test_add_col_int(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        test_table.add_col("col3", 1)
        self.assertEqual(test_table.table_content, [["col1", "col2", "col3"], [11, 12, 1], [21, 22, 1], [31, 32, 1]])
    
    def test_add_col_str(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        test_table.add_col("col3", "?")
        self.assertEqual(
            test_table.table_content, [["col1", "col2", "col3"], [11, 12, "?"], [21, 22, "?"], [31, 32, "?"]]
        )
    
    def test_add_col_bool(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        test_table.add_col("col3", None)
        self.assertEqual(
            test_table.table_content, [["col1", "col2", "col3"], [11, 12, None], [21, 22, None], [31, 32, None]]
        )
    
    def test_edit_row_list(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        test_table.edit_row(1, [111, 112])
        self.assertEqual(test_table.table_content, [["col1", "col2"], [111, 112], [21, 22], [31, 32]])

    def test_edit_row_dict(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        test_table.edit_row(1, {"col1": 111, "col2": 112})
        self.assertEqual(test_table.table_content, [["col1", "col2"], [111, 112], [21, 22], [31, 32]])
    
    def test_edit_cell(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        test_table.edit_cell(1, "col1", 111)
        self.assertEqual(test_table.table_content, [["col1", "col2"], [111, 12], [21, 22], [31, 32]])
        
    def test_filter(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], [11, 12], [21, 22], [31, 32]]
        self.assertEqual(test_table.filter("@col1@ > 20").table_content, [["col1", "col2"], [21, 22], [31, 32]])


class TestCsvTable(unittest.TestCase):
    def test_csv_load(self):
        test_table = tablebase.CsvTable("test.csv")
        self.assertEqual(test_table.table_content, [["col1", "col2"], ['11', '12'], ['21', '22'], ['31', '32']])
        
    def test_csv_save(self):
        test_table = tablebase.Table()
        test_table.table_content = [["col1", "col2"], ['11', '12'], ['21', '22'], ['31', '32']]
        test_table.save("test_save.csv")
        opened_test_table = tablebase.CsvTable("test_save.csv")
        remove("test_save.csv")
        self.assertEqual([['col1', 'col2'], ['11', '12'], ['21', '22'], ['31', '32']], opened_test_table.table_content)
        
    
if __name__ == "__main__":
    unittest.main()
