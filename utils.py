import random


def random_project_code():
    project_code = ""
    max_len = 6
    alfavit = "QWERTYUIOPASDFGHJKLZXCVBNM"
    for _ in range(max_len):
        randomindex = random.randint(0, len(alfavit) - 1)
        point = alfavit[randomindex]
        project_code += point
    return project_code