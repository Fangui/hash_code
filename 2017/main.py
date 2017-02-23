import datacenter

test = datacenter.datacenter('kittens.in')

for v in test.videos:
    print(v.size, v.req)

