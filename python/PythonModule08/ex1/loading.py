import sys
import importlib


def check_dependency(name: str, import_name: str) -> tuple[bool, str]:
    try:
        mod = importlib.import_module(import_name)
        version = getattr(mod, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, ""


def show_dependencies() -> dict[str, bool]:
    deps = [
        ("pandas", "pandas", "Data manipulation ready"),
        ("numpy", "numpy", "Numerical computation ready"),
        ("matplotlib", "matplotlib", "Visualization ready"),
    ]
    available: dict[str, bool] = {}
    print("Checking dependencies:")
    for display, import_name, desc in deps:
        ok, version = check_dependency(display, import_name)
        available[import_name] = ok
        if ok:
            print(f"[OK] {display} ({version}) - {desc}")
        else:
            print(f"[MISSING] {display} - {desc}")
    return available


def show_install_instructions() -> None:
    print()
    print("To install missing dependencies:")
    print()
    print("Using pip:")
    print("  pip install -r requirements.txt")
    print()
    print("Using Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")


def show_pip_vs_poetry() -> None:
    print()
    print("pip vs Poetry:")
    print("  pip           : Simple package installer, uses requirements.txt")
    print("  Poetry        : Dependency manager with lock files (poetry.lock)")
    print("                  Handles version conflicts, virtual envs automatically")
    print("                  Uses pyproject.toml as single config source")


def run_analysis() -> None:
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib  # type: ignore
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # type: ignore

    print()
    print("Analyzing Matrix data...")

    rng = np.random.default_rng(42)
    n = 1000
    timestamps = np.arange(n)
    signal = rng.normal(loc=0.0, scale=1.0, size=n)
    noise = rng.uniform(low=-0.5, high=0.5, size=n)
    data_values = signal + noise

    print(f"Processing {n} data points...")

    df = pd.DataFrame(
        {"timestamp": timestamps, "value": data_values}
    )
    mean_val: float = float(df["value"].mean())
    std_val: float = float(df["value"].std())
    min_val: float = float(df["value"].min())
    max_val: float = float(df["value"].max())

    print(f"Mean: {mean_val:.4f}")
    print(f"Std:  {std_val:.4f}")
    print(f"Min:  {min_val:.4f}")
    print(f"Max:  {max_val:.4f}")

    print("Generating visualization...")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

    ax1.plot(df["timestamp"], df["value"], color="green", linewidth=0.5)
    ax1.set_title("Matrix Signal over Time")
    ax1.set_xlabel("Timestamp")
    ax1.set_ylabel("Value")
    ax1.axhline(mean_val, color="red", linestyle="--", label="Mean")
    ax1.legend()

    ax2.hist(df["value"], bins=50, color="green", edgecolor="black")
    ax2.set_title("Matrix Signal Distribution")
    ax2.set_xlabel("Value")
    ax2.set_ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("matrix_analysis.png", dpi=100)
    plt.close(fig)

    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()

    available = show_dependencies()
    show_pip_vs_poetry()

    all_ok = all(available.values())
    if not all_ok:
        show_install_instructions()
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
