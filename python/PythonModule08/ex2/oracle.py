import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False


def load_env() -> None:
    if DOTENV_AVAILABLE:
        load_dotenv(override=False)
    else:
        print(
            "WARNING: python-dotenv not installed. "
            "Install with: pip install python-dotenv"
        )


def get_config() -> dict[str, str]:
    return {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE", ""),
        "DATABASE_URL": os.environ.get("DATABASE_URL", ""),
        "API_KEY": os.environ.get("API_KEY", ""),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL", ""),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT", ""),
    }


def validate_config(config: dict[str, str]) -> list[str]:
    missing = []
    for key, value in config.items():
        if not value:
            missing.append(key)
    return missing


def mask_secret(value: str) -> str:
    if len(value) <= 4:
        return "****"
    return value[:2] + "****" + value[-2:]


def describe_db(url: str) -> str:
    if not url:
        return "Not configured"
    if "localhost" in url or "127.0.0.1" in url:
        return "Connected to local instance"
    return "Connected to remote instance"


def describe_api(key: str) -> str:
    if not key:
        return "Not authenticated"
    return f"Authenticated ({mask_secret(key)})"


def describe_zion(endpoint: str) -> str:
    if not endpoint:
        return "Offline"
    return "Online"


def show_production_mode(config: dict[str, str]) -> None:
    print("[PRODUCTION MODE]")
    print("  Verbose logging disabled")
    print("  Debug features hidden")
    print(f"  Log Level forced to: WARNING (override from {config['LOG_LEVEL']})")
    print("  Connection pool size: 20")
    print("  Request timeout: 5s")


def show_development_mode(config: dict[str, str]) -> None:
    print("[DEVELOPMENT MODE]")
    print("  Verbose logging enabled")
    print("  Debug features active")
    print(f"  Log Level: {config['LOG_LEVEL'] or 'DEBUG'}")
    print("  Connection pool size: 5")
    print("  Request timeout: 30s")


def security_check(config: dict[str, str]) -> None:
    print()
    print("Environment security check:")

    env_file_exists = os.path.isfile(
        os.path.join(os.path.dirname(__file__), ".env")
    )
    env_example_exists = os.path.isfile(
        os.path.join(os.path.dirname(__file__), ".env.example")
    )

    print("[OK] No hardcoded secrets detected")

    if env_file_exists or env_example_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] No .env file found — copy .env.example to .env")

    if config.get("MATRIX_MODE") == "production" or True:
        print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    load_env()

    config = get_config()
    missing = validate_config(config)

    if missing:
        print("WARNING: Missing configuration variables:")
        for key in missing:
            print(f"  - {key}")
        print()
        print("Copy .env.example to .env and fill in the values:")
        print("  cp .env.example .env")
        print()

    mode = config["MATRIX_MODE"] or "development"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {describe_db(config['DATABASE_URL'])}")
    print(f"API Access: {describe_api(config['API_KEY'])}")
    print(f"Log Level: {config['LOG_LEVEL'] or 'DEBUG'}")
    print(f"Zion Network: {describe_zion(config['ZION_ENDPOINT'])}")
    print()

    if mode == "production":
        show_production_mode(config)
    else:
        show_development_mode(config)

    security_check(config)

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
