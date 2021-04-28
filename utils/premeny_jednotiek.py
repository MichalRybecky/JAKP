import json
def load_data():
    data = ""
    f = open('utils/jednotky.json', 'r', encoding='utf-8')
    r = f.readline().strip()
    while r:
        data = data + r
        r = f.readline().strip()
    return json.loads(data)

def premenit(input, input_jednotka, output_jednotka):
    jednotky = load_data()
    for i in [key for key in jednotky]:
        if input_jednotka in jednotky[i] and output_jednotka in jednotky[i]:
            return input * jednotky[i][input_jednotka]['nasobok'] / jednotky[i][output_jednotka]['nasobok']
    else:
        return -1