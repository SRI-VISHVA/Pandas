import random

qual = [
    "Bachelor of Arts: BA",
    "Bachelor of Business Administration: BBA",
    "Bachelor of Science: BSc",
    "Bachelor of Commerce: Bcom",
    "Bachelor of Computer Applications: BCA",
    "Bachelor of Laws: LLB",
    "Bachelor of Engineering: BE",
    "Bachelor of Technology: BTech",
    "Bachelor of Education: BEd (BEd degrees are offered after completion of a 3-year undergraduate coursework.)",
    "Bachelor of Medicine, Bachelor of Surgery: MBBS"
]


def generate_random_qualification():
    return random.choice(qual)

# print(generate_random_qualification())
