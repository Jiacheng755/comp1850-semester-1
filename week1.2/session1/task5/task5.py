# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Manchester"] = "Irwell"
rivers["Birmingham"] = "Tame"

# Display all the key:value pairs, as tuples
print(rivers.items())
# Delete an entry from the rivers database
del rivers["London"]
print(rivers)