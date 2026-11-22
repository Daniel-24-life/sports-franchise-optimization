import unittest

from optimizer import ranked_rosters, REQUIRED_ROLES

class OptimizerTests(unittest.TestCase):
    def test_budget_and_role_constraints(self):
        rosters = ranked_rosters()
        self.assertTrue(rosters)
        self.assertTrue(all(r.cost <= 14 and r.risk <= 6 for r in rosters))
        self.assertTrue(all({p.role for p in r.players} == REQUIRED_ROLES for r in rosters))
        self.assertEqual(rosters[0].contribution, 54)

    def test_tighter_budget_has_no_higher_optimum(self):
        self.assertLessEqual(ranked_rosters(budget=12)[0].contribution, ranked_rosters(budget=14)[0].contribution)

    def test_infeasible_budget(self):
        self.assertEqual(ranked_rosters(budget=4), [])

if __name__ == "__main__":
    unittest.main()
