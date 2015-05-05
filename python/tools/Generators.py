__author__ = 'nitish'
import random


class Generators():
    def __init__(self):
        pass

    def randomNumber(self, num_type, num_range=None, dec_places=None):
        if num_type == "int":
            if num_range and isinstance(num_range, list) and len(num_range) == 2:
                return random.randint(num_range[0], num_range[1])
            elif num_range and isinstance(num_range, int):
                return random.randint(0, num_range)
            else:
                return random.randint(0,100)
        elif num_type == "float":
            if num_range and isinstance(num_range, list) and len(num_range) == 2:
                if dec_places:
                    return round(random.uniform(num_range[0], num_range[1]), int(dec_places))
                else:
                    return random.uniform(num_range[0], num_range[1])
            elif num_range and isinstance(num_range, float):
                if dec_places:
                    return round(random.uniform(0, num_range), int(dec_places))
                else:
                    return random.uniform(0, num_range)
            elif dec_places:
                return round(random.uniform(0, 100.00), dec_places)
            else:
                return random.uniform(0, 100.00)
        else:
            return random.randint(0,100)

    def listRandomNumbers(self, list_length, type=None, num_range=None, dec_places=None):
        ret_list = list()
        if isinstance(list_length, int):
            for x in range(list_length):
                ret_list.append(self.randomNumber(type, num_range, dec_places))
        return ret_list

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
        print byte_list
        return_list = ':'.join(map(lambda x: "%s" % x, byte_list))
        return return_list


if __name__ == '__main__':
    generator = Generators()
    print "Random Int: " + str(generator.randomNumber("int"))
    print "Random Int<1000: " + str(generator.randomNumber("int", 1000))
    print "Random 400<Int<500: " + str(generator.randomNumber("int", [400, 500]))
    print "Random Float: " + str(generator.randomNumber("float"))
    print "Random Float<3.377 with 4 dec places: " + str(generator.randomNumber("float", 3.377, 4))
    print "Random 4.22222<Float<4.565656 with 8 dec places: : " + \
          str(generator.randomNumber("float", [4.22222, 4.565656], 8))
    print "List of 10 Random 4.22222<Float<4.565656 with 8 dec places: : " + \
          str(generator.listRandomNumbers(10, "float", [4.22222, 4.565656], 8))
    print "Random MAC Address with OUI AA:BB:CC : " + str(generator.randomMacAddress("AA:BB:CC"))
    print "Random MAC Address no OUI : " + str(generator.randomMacAddress())