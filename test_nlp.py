from analyzer.nlp_processor import explain_error


error = {
    "type": "Undefined Variable",
    "variable": "y",
    "line": 3
}


result = explain_error(error)


print("\n==============================")
print("NLP ANALYSIS")
print("==============================")

print("\nExplanation:")
print(result["explanation"])

print("\nSuggested Fix:")
print(result["suggested_fix"])

print("\nSimilarity Score:")
print(round(result["similarity"], 2))