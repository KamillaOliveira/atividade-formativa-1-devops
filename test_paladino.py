import unittest
from paladino import Paladino

class TestPaladino(unittest.TestCase):

    def test_01_atributos_iniciais(self):
        # teste 1: verifica atributos iniciais do paladino
        p = Paladino("Uther")
        self.assertEqual(p.nome, "Uther")
        self.assertEqual(p.hp, 100)
        self.assertEqual(p.mana, 100)
        self.assertEqual(p.faccao, "Alliance")

    def test_02_holy_light_recupera_hp(self):
        # teste 2: verifica aumento de vida ao usar holy light
        p = Paladino("Uther")
        p.hp = 50
        p.usar_holy_light()
        self.assertEqual(p.hp, 75)

    def test_03_holy_light_consome_mana(self):
        # teste 3: verifica consumo de mana ao usar holy light
        p = Paladino("Uther")
        p.usar_holy_light()
        self.assertEqual(p.mana, 85)

    def test_04_divine_shield_retorno(self):
        # teste 4: verifica o retorno da habilidade divine shield
        p = Paladino("Uther")
        retorno = p.usar_divine_shield()
        self.assertEqual(retorno, "Imune a dano por 8 segundos")

    def test_05_multiplos_usos_holy_light(self):
        # teste 5: verifica multiplos usos consecutivos de holy light
        p = Paladino("Uther")
        p.usar_holy_light()
        p.usar_holy_light()
        self.assertEqual(p.hp, 150)
        self.assertEqual(p.mana, 70)

if __name__ == '__main__':
    unittest.main()