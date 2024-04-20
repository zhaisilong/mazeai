from maze.chem import identifier_to_smiles, NameToSmiles
import unittest


class TestIdentifierToSmiles(unittest.TestCase):
    def test_identifier(self):
        # 使用已知的有效结构标识符进行测试
        self.assertEqual(identifier_to_smiles("acetaminophen"), "CC(=O)Nc1ccc(O)cc1")


class TestIdentifierToSmilesOpsin(unittest.TestCase):
    def test_identifier(self):
        nts = NameToSmiles(
            allowUninterpretableStereo=True,
        )
        name = "2,4,6-trinitrotoluene"
        smiles = nts.name_to_smiles(name)
        answer = "[N+](=O)([O-])C1=C(C)C(=CC(=C1)[N+](=O)[O-])[N+](=O)[O-]"
        self.assertEqual(smiles, answer)


if __name__ == "__main__":
    unittest.main()
