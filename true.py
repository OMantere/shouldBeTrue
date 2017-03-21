from phaeleh import by

phaeleh = 'the best'

def lies_that_should_be_true(lie):
    if not lie:
        print('Lie is True')
        return True
    return 'Lies that should be true'

if __name__ == '__main__':
    print("Presenting possibly the best song ever written: %s" % lies_that_should_be_true(by(phaeleh)))

