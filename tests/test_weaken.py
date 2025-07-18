import unittest

from src import marking, mitl, weaken


class TestWeaken(unittest.TestCase):

    def test_weakening_fg(self):
        formula = mitl.Eventually(mitl.Always(mitl.Prop("a"), (0, 2)))
        indices = [0]
        trace = marking.Trace(
            [
                {"a": False},
                {"a": False},
                {"a": False},
                {"a": True},
                {"a": True},
            ],
            0,
        )
        result = weaken.Weaken(formula, indices, trace).weaken()
        assert result is not None
        self.assertTupleEqual(result, (0, 1))

    def test_weakening_gf(self):
        formula = mitl.Always(mitl.Eventually(mitl.Prop("a"), (0, 4)))
        indices = [0]
        trace = marking.Trace(
            [
                {"a": False},
                {"a": False},
                {"a": False},
                {"a": False},
                {"a": False},
                {"a": False},
                {"a": True},
            ],
            1,
        )
        result = weaken.Weaken(formula, indices, trace).weaken()
        assert result is not None
        self.assertTupleEqual(result, (0, 6))

    def test_weakening_ff(self):
        formula = mitl.Eventually(
            mitl.And(mitl.Prop("a"), mitl.Eventually(mitl.Prop("b"), (0, 2)))
        )
        indices = [0, 1]
        trace = marking.Trace(
            [
                {"a": True, "b": False},
                {"a": True, "b": False},
                {"a": False, "b": False},
                {"a": False, "b": False},
                {"a": False, "b": False},
                {"a": False, "b": True},
            ],
            0,
        )
        result = weaken.Weaken(formula, indices, trace).weaken()
        assert result is not None
        self.assertTupleEqual(result, (0, 4))

    def test_weakening_gg(self):
        formula = mitl.Always(
            mitl.Or(mitl.Prop("a"), mitl.Always(mitl.Prop("b"), (0, 2)))
        )
        indices = [0, 1]
        trace = marking.Trace(
            [
                {"a": True, "b": False},
                {"a": True, "b": False},
                {"a": False, "b": True},
                {"a": True, "b": True},
                {"a": True, "b": False},
                {"a": True, "b": False},
                {"a": False, "b": True},
                {"a": False, "b": True},
                {"a": False, "b": True},
                {"a": True, "b": True},
            ],
            0,
        )
        result = weaken.Weaken(formula, indices, trace).weaken()
        assert result is not None
        self.assertTupleEqual(result, (0, 1))

    def test_weakening_gfg(self):
        formula = mitl.Always(
            mitl.Eventually(mitl.Always(mitl.Prop("a"), (0, 2)))
        )
        indices = [0, 0]
        trace = marking.Trace(
            [
                {"a": False},
                {"a": False},
                {"a": False},
                {"a": True},
                {"a": True},
            ],
            0,
        )
        result = weaken.Weaken(formula, indices, trace).weaken()
        assert result is not None
        self.assertTupleEqual(result, (0, 1))

    def test_weakening_gu(self):
        formula = mitl.Always(
            mitl.Until(mitl.Prop("a"), mitl.Prop("b"), (0, 2))
        )
        indices = [0]
        trace = marking.Trace(
            [
                {"a": True, "b": False},
                {"a": True, "b": False},
                {"a": True, "b": False},
                {"a": True, "b": False},
                {"a": True, "b": False},
                {"a": False, "b": True},
            ],
            0,
        )
        result = weaken.Weaken(formula, indices, trace).weaken()
        assert result is not None
        self.assertTupleEqual(result, (0, 5))

    def test_weakening_uf_right(self):
        formula = mitl.Until(
            mitl.Prop("a"), mitl.Eventually(mitl.Prop("b"), (0, 1))
        )
        indices = [1]
        trace = marking.Trace(
            [
                {"a": True, "b": False},
                {"a": True, "b": False},
                {"a": True, "b": False},
                {"a": False, "b": False},
                {"a": False, "b": False},
                {"a": False, "b": False},
                {"a": False, "b": False},
                {"a": False, "b": True},
            ],
            0,
        )
        result = weaken.Weaken(formula, indices, trace).weaken()
        assert result is not None
        self.assertTupleEqual(result, (0, 4))


if __name__ == "__main__":
    unittest.main()
