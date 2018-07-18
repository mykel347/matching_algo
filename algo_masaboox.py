first_group = []

request_dic = {}
available_dic = {}

users = [101,102,103]

matched_users = []
possible_matches = []

with open('requests.txt', 'r') as requests:
    requests_tup = requests.read()

with open('available.txt', 'r') as available:
    available_tup = available.read()

requests_tup = requests_tup.split("\n")
available_tup = available_tup.split("\n")

for i in requests_tup:
    request_dic[(i.split(",")[0])] = i.split(",")[1]

for j in available_tup:
    available_dic[(j.split(",")[0])] = j.split(",")[1]



while True:

    for i in users:

        i_requests = []
        for k, v in available_dic.items():
            print("is ", v, "= ", i, ' ?')
            if i == v:
                i_requests.append(k)
        print(i_requests)
    break



