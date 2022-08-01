def compute_patterns(inputs=[]):
    inputs.append("some stuff")
    patterns = ["a list based on"] + inputs
    return patterns

print(compute_patterns())
