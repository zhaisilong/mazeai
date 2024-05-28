from rdkit import Chem
from rdkit.Chem.MolStandardize import rdMolStandardize
from rdkit import RDLogger
from loguru import logger

RDLogger.DisableLog("rdApp.*")


def standardize_smi(
    smiles,
    basicClean=False,
    clearCharge=False,
    clearFrag=False,
    canonTautomer=False,
    isomeric=False,
):
    try:
        clean_mol = Chem.MolFromSmiles(smiles)
        # 除去氢、金属原子、标准化分子
        if basicClean:
            clean_mol = rdMolStandardize.Cleanup(clean_mol)
        if clearFrag:
            #  仅保留主要片段作为分子
            clean_mol = rdMolStandardize.FragmentParent(clean_mol)
        # 尝试中性化处理分子
        if clearCharge:
            uncharger = rdMolStandardize.Uncharger()
            clean_mol = uncharger.uncharge(clean_mol)
        # 处理互变异构情形，这一步在某些情况下可能不够完美
        if canonTautomer:
            te = rdMolStandardize.TautomerEnumerator()  # idem
            clean_mol = te.Canonicalize(clean_mol)
        # set to True 保存立体信息，set to False 移除立体信息，并将分子存为标准化后的SMILES形式
        stan_smiles = Chem.MolToSmiles(clean_mol, isomericSmiles=isomeric)
        if stan_smiles:
            return stan_smiles
        else:
            return None
    except Exception as e:
        logger.info(f"Falied to standardize {smiles}, since: {e}")
        return None
    return stan_smiles
