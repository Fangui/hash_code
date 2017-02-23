import datacenter


if __name__ == '__main__':
    test = datacenter.datacenter('kittens.in')
    test.out('kittens.out')
    test = datacenter.datacenter('me_at_the_zoo.in')
    test.out('me_at_the_zoo.out')
    test = datacenter.datacenter('trending_today.in')
    test.out('trending_today.out')
    test = datacenter.datacenter('videos_worth_spreading.in')
    test.out('videos_worth_spreading.out')