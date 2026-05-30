import typing
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from ex0.creatures import CreatureFactory


def test_healing(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    hb: HealCapability = typing.cast(HealCapability, base)
    print(hb.heal())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    he: HealCapability = typing.cast(HealCapability, evolved)
    print(he.heal())


def test_transform(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    tb: TransformCapability = typing.cast(TransformCapability, base)
    print(tb.transform())
    print(base.attack())
    print(tb.revert())
    print(" evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    te: TransformCapability = typing.cast(TransformCapability, evolved)
    print(te.transform())
    print(evolved.attack())
    print(te.revert())


def main() -> None:
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    test_healing(heal_factory)
    print()
    test_transform(transform_factory)


if __name__ == "__main__":
    main()
