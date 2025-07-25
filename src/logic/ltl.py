from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Ltl:
    pass


@dataclass(frozen=True)
class Prop(Ltl):
    name: str


@dataclass(frozen=True)
class Not(Ltl):
    operand: Ltl


@dataclass(frozen=True)
class Next(Ltl):
    operand: Ltl


@dataclass(frozen=True)
class Eventually(Ltl):
    operand: Ltl


@dataclass(frozen=True)
class Always(Ltl):
    operand: Ltl


@dataclass(frozen=True)
class And(Ltl):
    left: Ltl
    right: Ltl


@dataclass(frozen=True)
class Or(Ltl):
    left: Ltl
    right: Ltl


@dataclass(frozen=True)
class Implies(Ltl):
    left: Ltl
    right: Ltl


@dataclass(frozen=True)
class Until(Ltl):
    left: Ltl
    right: Ltl


def to_nuxmv(formula: Ltl) -> str:
    if isinstance(formula, Prop):
        return formula.name
    if isinstance(formula, Not):
        return f"!({to_nuxmv(formula.operand)})"
    if isinstance(formula, Next):
        return f"X ({to_nuxmv(formula.operand)})"
    if isinstance(formula, Eventually):
        return f"F ({to_nuxmv(formula.operand)})"
    if isinstance(formula, Always):
        return f"G ({to_nuxmv(formula.operand)})"
    if isinstance(formula, And):
        return f"({to_nuxmv(formula.left)} & {to_nuxmv(formula.right)})"
    if isinstance(formula, Or):
        return f"({to_nuxmv(formula.left)} | {to_nuxmv(formula.right)})"
    if isinstance(formula, Implies):
        return f"({to_nuxmv(formula.left)} -> {to_nuxmv(formula.right)})"
    if isinstance(formula, Until):
        return f"({to_nuxmv(formula.left)} U {to_nuxmv(formula.right)})"
    raise ValueError(f"Unsupported LTL construct: {formula}")


def to_string(formula: Ltl) -> str:
    return to_nuxmv(formula)
