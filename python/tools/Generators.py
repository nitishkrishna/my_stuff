__author__ = 'nitish'
import random
import numpy

class Generators():
    def __init__(self):
        pass

    def randomNumber(self, list_length=None, num_type=None, num_range=None, dec_places=None):
        if num_type == "int":
            if list_length:
                if num_range:
                    if isinstance(num_range, list) and len(num_range) == 2:
                        return random.sample(xrange(num_range[0], num_range[1]+1), list_length)
                    elif isinstance(num_range, int):
                        return random.sample(xrange(num_range+1), list_length)
                else:
                    return random.sample(xrange(100), list_length)
            elif num_range:
                if isinstance(num_range, list) and len(num_range) == 2:
                    return random.randint(num_range[0], num_range[1])
                elif isinstance(num_range, int):
                    return random.randint(0, num_range)
            else:
                return random.randint(0, 100)
        elif num_type == "float":
            if list_length:
                if num_range:
                    if isinstance(num_range, list) and len(num_range) == 2:
                        return numpy.random.uniform(low=num_range[0], high=num_range[1], size=list_length)
                    elif isinstance(num_range, int):
                        return numpy.random.uniform(high=num_range, size=list_length)
                    else:
                        return numpy.random.uniform(size=list_length)
            elif num_range:
                if isinstance(num_range, list) and len(num_range) == 2:
                    if dec_places:
                        return round(random.uniform(num_range[0], num_range[1]), int(dec_places))
                    else:
                        return random.uniform(num_range[0], num_range[1])
                elif isinstance(num_range, float):
                    if dec_places:
                        return round(random.uniform(0, num_range), int(dec_places))
                    else:
                        return random.uniform(0, num_range)
                else:
                    return random.randint(0, 100)
            elif dec_places:
                return round(random.uniform(0, 100.00), dec_places)
            else:
                return random.uniform(0, 100.00)
        else:
            return random.randint(0, 100)

    def randomMacAddress(self, OUI=None):
        if OUI:
            byte_list = list(str(OUI).lower().split(':'))
            byte_list = [int("0x"+str(z), 16) for z in byte_list]
            byte_list.extend([random.randint(0x00, 0xff),
                             random.randint(0x00, 0xff),
                             random.randint(0x00, 0xff)])
        else:
            byte_list = []
            choice_list = [2, 6, 10, 14]
            byte_list.extend([random.randint(0x00, 0xff),
                              random.choice(choice_list),
                              random.randint(0x00, 0xff),
                              random.randint(0x00, 0xff),
                              random.randint(0x00, 0xff),
                              random.randint(0x00, 0xff)])
        byte_list = [str(hex(int(y)))[2:] for y in byte_list]
        byte_list = ["0"+str(m) if m.isdigit() and int(m) < 10 else str(m) for m in byte_list]
        # print byte_list
        return_list = ':'.join(map(lambda x: "%s" % x, byte_list))
        return return_list


if __name__ == '__main__':
    generator = Generators()
    print "Random Int: " + str(generator.randomNumber(num_type="int"))
    print "Random Int<1000: " + str(generator.randomNumber(num_type="int", num_range=1000))
    print "Random 400<Int<500: " + str(generator.randomNumber(num_type="int", num_range=[400, 500]))
    print "Random Float: " + str(generator.randomNumber(num_type="float"))
    print "Random Float<3.377 with 4 dec places: " + str(generator.randomNumber(num_type="float",
                                                                                num_range=3.377, dec_places=4))
    print "Random 4.22222<Float<4.565656 with 8 dec places: : " + \
          str(generator.randomNumber(num_type="float", num_range=[4.22222, 4.565656], dec_places=8))
    print "List of 10 Random 4.22222<Float<4.565656: : " + \
          str(generator.randomNumber(list_length=10, num_type="float", num_range=[4.22222, 4.565656]))
    print "List of 12 Random 100<Int<1000: : " + \
        str(generator.randomNumber(list_length=12, num_type="int", num_range=[100, 1000]))
    print "Random MAC Address with OUI AA:BB:CC : " + str(generator.randomMacAddress("AA:BB:CC"))
    print "Random MAC Address no OUI : " + str(generator.randomMacAddress())