from dotenv import dotenv_values, load_dotenv
import os


VARIABLES: tuple[str, ...] = ("MATRIX_MODE", "DATABASE_URL", "API_KEY",
                              "LOG_LEVEL", "ZION_ENDPOINT")
VALID_MODES = ("production", "development")
DEFAULT_MODE: str = "production"
VALID_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
DEFAULTS: dict[str, dict[str, str | None]] = {
    "development": {
        "LOG_LEVEL": "DEBUG",
        "DATABASE_URL": "sqlite:///local.db",
        "API_KEY": None,
        "ZION_ENDPOINT": None,
    },
    "production": {
        "LOG_LEVEL": "WARNING",
        "DATABASE_URL": None,
        "API_KEY": None,
        "ZION_ENDPOINT": None,
    }
}
STATUS_WORDS: dict[str, str] = {
    "API_KEY": "Authenticated",
    "DATABASE_URL": "Connected",
    "ZION_ENDPOINT": "Online",
}
MASK: str = "****"
MIN_REVEAL_LENGTH: int = 12
MIN_REVEAL_COUNT: int = 4


def get_source(name: str,
               shell_vars: set[str], file_vars: dict[str, str | None]) -> str:
    if name in shell_vars:
        return 'shell'
    elif file_vars.get(name) is not None:
        return 'file'
    else:
        return 'default'


def format_entry(name: str, value: str | None, source: str, mode: str) -> str:
    if value is None:
        if mode == "production":
            return f"{name}: [ERROR] not set"
        else:
            return f"{name}: [WARN] not set"
    if mode == "production":
        if name in STATUS_WORDS:
            return f"{name}: {STATUS_WORDS[name]} (from {source})"
        else:
            return f"{name}: {value} (from {source})"
    else:
        if name == "API_KEY":
            return f"{name}: {mask_secret(value)} (from {source})"
        else:
            return f"{name}: {value} (from {source})"


def mask_secret(value: str) -> str:
    if len(value) < MIN_REVEAL_LENGTH:
        return MASK
    else:
        return MASK + value[-MIN_REVEAL_COUNT:]


def main() -> None:
    resolved: dict[str, str | None] = {}
    sources: dict[str, str] = {}
    notices: list[str] = []
    shell_vars: set[str] = set()
    for var in VARIABLES:
        if var in os.environ:
            shell_vars.add(var)
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    ignore_path = os.path.join(os.path.dirname(__file__), '.gitignore')
    env_found = os.path.isfile(env_path)
    if not env_found:
        notices.append("No .env found, using shell environment and defaults")
    file_vars = dotenv_values(env_path)
    load_dotenv(env_path, override=False)
    raw_mode = os.environ.get("MATRIX_MODE")
    if not raw_mode:
        mode = DEFAULT_MODE
        mode_source = "default"
    else:
        mode = raw_mode.strip().lower()
        if mode not in VALID_MODES:
            notices.append(f"Invalid MATRIX_MODE provided: '{raw_mode}'. "
                           f"Proceeding with the default: '{DEFAULT_MODE}'")
            mode = DEFAULT_MODE
            mode_source = "default"
        else:
            mode_source = get_source("MATRIX_MODE", shell_vars, file_vars)
    resolved["MATRIX_MODE"] = mode
    sources["MATRIX_MODE"] = mode_source
    raw_level = os.environ.get("LOG_LEVEL")
    if not raw_level:
        level = DEFAULTS[mode]["LOG_LEVEL"]
        level_source = "default"
    else:
        level = raw_level.strip().upper()
        if level not in VALID_LEVELS:
            default_level = DEFAULTS[mode]["LOG_LEVEL"]
            notices.append(f"Invalid LOG_LEVEL provided: '{raw_level}'. "
                           f"Proceeding with the default: '{default_level}'")
            level = default_level
            level_source = "default"
        else:
            level_source = get_source("LOG_LEVEL", shell_vars, file_vars)
    sources["LOG_LEVEL"] = level_source
    resolved["LOG_LEVEL"] = level
    for name in VARIABLES:
        if name in resolved:
            continue
        value = os.environ.get(name)
        if not value:
            value = DEFAULTS[mode][name]
            source = "default"
        else:
            source = get_source(name, shell_vars, file_vars)
        resolved[name] = value
        sources[name] = source
    print("ORACLE STATUS: Consulting the configuration...")
    print('')
    if notices:
        print("Notices:")
        for notice in notices:
            print(notice)
        print('')
    for name in VARIABLES:
        print(format_entry(name, resolved[name], sources[name], mode))
    print('')
    print("Configuration security check:")
    if any(table.get("API_KEY") for table in DEFAULTS.values()):
        print("[WARN] Hardcoded secrets detected!")
    else:
        print("[OK] No hardcoded secrets detected")
    try:
        with open(ignore_path, "r") as f:
            ignored = any(line.strip() == ".env" for line in f)
    except OSError as e:
        print(f"[WARN] Could not read .gitignore ({e}): "
              ".env may not be ignored by git")
    else:
        if ignored:
            print("[OK] .env file properly ignored by git")
        else:
            print("[WARN] .env file not ignored by git!")
    overrides = [name for name, source in sources.items()
                 if source == "shell"]
    if overrides:
        print(f"[OK] Shell overrides active: {', '.join(overrides)}")
    else:
        print("[INFO] No shell overrides active: using .env and defaults")
    print("")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
