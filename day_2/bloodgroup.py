import random

bg = ["A RhD positive (A+)",
      "A RhD negative (A-)",
      "B RhD positive (B+)",
      "B RhD negative (B-)",
      "O RhD positive (O+)",
      "O RhD negative (O-)",
      "AB RhD positive (AB+)",
      "AB RhD negative (AB-)"]


def generate_random_blood():
    return random.choice(bg)


# print(generate_random_blood())
