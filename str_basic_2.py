#Task1

text = "Berlin is a world city of culture, politics, media and science."
length = len(text)
print(length)

#Task2

text = "Berlin is a world city of culture, politics, media and science."
first = text[0]
last = text[-1]

print(first, last)

#Task3

text = "Berlin is a world city of culture, politics, media and science."
capital = text.upper()

print("First three characters:", capital[0:3])

#Task4

test = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"
letter = "B"
count = test.count(letter)

print(f"{letter} appears: {count} times")

#Task5

text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

print("Last ten characters:", text[-10:-1])

#Task6

text = "---Python programming---"
print(text.strip("-"))

#Task7

first_name = "Carlos"
last_name = "Denegri"

print(f"Firstname: {first_name}\nLastname: {last_name}")


