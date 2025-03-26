def load_prompt(file_path):
    """Load prompt from a file."""
    with open(file_path, "r") as f:
        return f.read().strip()

def get_system_prompt(config):
    """Get system prompt from config-specified file."""
    return load_prompt(config["prompts"]["system_prompt_file"])

def get_example_prompt(config):
    """Get example prompt from config-specified file."""
    return load_prompt(config["prompts"]["example_prompt_file"])