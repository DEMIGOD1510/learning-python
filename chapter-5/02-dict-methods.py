marks = {
  "Ankit": 100,
  "Harry": 56,
  "Rohan":34,
  0: "Ankit"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Ankit": 99, "Antima": 100})
# print(marks)

print(marks.get("Ankit2")) # Prints None
print(marks["Ankit2"]) # Returns an error