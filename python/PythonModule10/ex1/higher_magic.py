from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
    condition: Callable, spell: Callable
) -> Callable:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [s(target, power) for s in spells]
    return sequence


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def get_power(target: str, power: int) -> int:
        return power

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    r1, r2 = combined("Dragon", 10)
    print(f"Combined spell result: {r1}, {r2}")

    print("\nTesting power amplifier...")
    mega = power_amplifier(get_power, 3)
    print(f"Original: 10, Amplified: {mega('Dragon', 10)}")

    print("\nTesting conditional caster...")
    guarded = conditional_caster(
        lambda t, p: p >= 20,
        fireball
    )
    print(guarded("Dragon", 10))
    print(guarded("Dragon", 25))

    print("\nTesting spell sequence...")
    seq = spell_sequence([fireball, heal])
    for result in seq("Dragon", 10):
        print(result)

    print(f"\ncallable(fireball): {callable(fireball)}")
    print(f"callable(42): {callable(42)}")


if __name__ == "__main__":
    main()
