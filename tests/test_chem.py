from maze.chem import identifier_to_smiles
import unittest

class TestIdentifierToSmiles(unittest.TestCase):
    def test_valid_identifier(self):
        # 使用已知的有效结构标识符进行测试
        self.assertEqual(identifier_to_smiles('acetaminophen'), 'CC(=O)Nc1ccc(O)cc1')

if __name__ == '__main__':
    unittest.main()