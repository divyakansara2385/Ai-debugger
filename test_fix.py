from analyzer.fix_genrator import generate_fix

error = {
    "type": "Undefined Variable",
    "variable": "y",
    "line": 3
}

fix = generate_fix(error)

print("\nSuggested Fix:")
print(fix)