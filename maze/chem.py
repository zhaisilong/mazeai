# https://github.com/dan2097/opsin

from urllib.request import urlopen
from urllib.parse import quote  # 用于确保 URL 编码正确
from loguru import logger
from typing import Optional
from pathlib import Path

import jpype
import jpype.imports
from jpype.types import *

class NameToSmiles:
    """https://github.com/SureChEMBL/opsin/tree/master"""
    def __init__(self, path=None, 
                       allowUninterpretableStereo=False, 
                       allowRadicals=False,
                       wildcardRadicals=False,
                       allowAcidsWithoutAcid=False,):
        if not path:
            self.path = Path(__file__).parent / "resource/opsin-cli-2.8.0-jar-with-dependencies.jar"
        else:
            self.path = Path(path)

        if not jpype.isJVMStarted():
            jpype.startJVM(classpath=[self.path])

        from uk.ac.cam.ch.wwmm.opsin import NameToStructureConfig, NameToStructure

        self.config = NameToStructureConfig()
        if allowUninterpretableStereo:
            self.config.setWarnRatherThanFailOnUninterpretableStereochemistry(True)
        if allowRadicals:
            self.config.setAllowRadicals(True)
        if allowAcidsWithoutAcid:
            self.config.setInterpretAcidsWithoutTheWordAcid(True)
        if wildcardRadicals:
            self.config.setOuputRadicalsAsWildCardAtoms(True)
        
        self.nts = NameToStructure.getInstance()


    def name_to_smiles(self, name):
        try:
            results = self.nts.parseChemicalName(name, self.config)
            return results.getSmiles()
        except Exception as e:
            print(f"Error converting name to SMILES: {e}")
            return None
    
    def name_to_cml(self, name):
        try:
            results = self.nts.parseChemicalName(name, self.config)
            return results.getCml()
        except Exception as e:
            print(f"Error converting name to CML: {e}")
            return None

def identifier_to_smiles(structure_identifier: str) -> Optional[str]:
    """将分子标志符转化成smiles

    Args:
        structure_identifier (str): 分子标志符

    Returns:
        str: smiles

    - [转化的网站](https://cactus.nci.nih.gov/chemical/structure)
    """
    # 对输入的结构标识符进行 URL 编码，以确保 URL 的正确性
    encoded_identifier = quote(structure_identifier)

    # 构建请求的 URL
    url = f"http://cactus.nci.nih.gov/chemical/structure/{encoded_identifier}/smiles"

    # 尝试打开 URL 并读取内容
    try:
        response = urlopen(url)
        smiles = response.read().decode("utf8")
        return smiles
    except Exception as e:
        logger.exception(f"发生错误: {e}")
        return None

if __name__ == "__main__":
    # # 示例结构标识符，可以是 CAS 号码、化学名称等
    # structure_identifier = 'Acetaminophen'  # 例如用药物的常用名
    # # 调用函数并打印结果
    # smiles = identifier_to_smiles(structure_identifier)
    # print("Structure Identifier:", structure_identifier)
    # print("SMILES Notation:", smiles)

    nts = NameToSmiles(allowUninterpretableStereo=True,)
    name = "2,4,6-trinitrotoluene"
    smiles = nts.name_to_smiles(name)
    cml = nts.name_to_cml(name)
    print(smiles)
    print(cml)
