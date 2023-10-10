#!/usr/bin/env python3
# Created by: Alex Kpajika
# Created on: Oct 10, 2023
# This program asks the user for the area of an oval in cm. It then calculates.

import constants


def main():
    la = float(input("The la is (cm): "))
    sa = float(input("The sa is(cm): "))
    area = constants.PI * la * sa
    print("")
    print("The area = {} cm^2".format(area))


if __name__ == "__main__":
    main()
