

# reasoning problem with going out
name = input("Hello! It's very nice to see you! What's your name? ").strip().title()
weather = input("What is the weather? ").strip().lower()
temp = input("How high is temperature today? ")

temp_f = (float(temp) * 9 / 5) + 32

if float(temp) > 35:
    answer_t = "too hot"
    a_temp = "ok"
elif float(temp) < 5:
    answer_t = "too cold"
    a_temp = "not ok"
else:
    answer_t = "great temperature"


if weather != "rain" or weather != "stormy" and a_temp == "ok":
    answer_w = "go outside"
else:
    answer_w = "stay inside"

print("----------")
print(f"{name} you should {answer_w}, because it's {weather} and it's {answer_t}.")
