def store():
    os.system('clear')
    print ("Welcome to the shop!")
    print ("\nWhat would you like to buy?\n")
    print ("1.) Great Sword")
    print ("back")
    print (" ")
    option = raw_input(' ')

    if option in weapons:
        if PlayerIG.gold >= weapons[option]:
            os.system('clear')
            PlayerIG.gold -= weapons[option]
            PlayerIG.weap.append(option)
            print "You have bought %s" % option
            option = raw_input(' ')
            store()

        else:
            os.system('clear')
            print "You don't have enough gold"
            option = raw_input(' ')
            store()

    elif option == "back":
        start1()

    else:
        os.system('clear')
        print "That item does not exist"
        option = raw_input(' ')
        store()

main()