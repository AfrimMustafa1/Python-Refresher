def echo(text: str, repetitions: int = 3) -> str:
    """
    Imitate a real-world echo effect.
    
    :param text: The string yelled at a mountain.
    :param repetitions: Number of times the mountain echoes the voice.
    :return: A string representing the echoed sound with a fading effect.
    """
    lines = []
    for i in range(repetitions, 0, -1):  # Start with full text and remove from the beginning
        lines.append(text[-i:])  # Keep only the last i characters

    lines.append(".")  # Final fading effect
    return "\n".join(lines)

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
