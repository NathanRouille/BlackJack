from random import sample

wallet = 30
nombres = [2,3,4,5,6,7,8,9,10,'valet','dame','roi','as']
couleurs = ['carreau','pique','coeur','trefle']

tab = {'[2,2]':['H','S','S','S','S','S','S','H','H','H'],'[3,3]':['H','S','S','S','S','S','S','H','H','H'],'[4,4]':['H','H','H','H','S','S','H','H','H','H'],'[5,5]':['H','D','D','D','D','D','D','D','D','H'],'[6,6]':['H','S','S','S','S','S','H','H','H','H'],'[7,7]':['H','S','S','S','S','S','S','H','H','H'],'[8,8]':['S','S','S','S','S','S','S','S','S','S'],'[9,9]':['R','S','S','S','S','S','R','S','S','R'],"['as','as']":['S','S','S','S','S','S','S','S','S','S'],"['as',2]":['H','H','H','H','D','D','H','H','H','H'],"['as',3]":['H','H','H','H','D','D','H','H','H','H'],"['as',4]":['H','H','H','D','D','D','H','H','H','H'],"['as',5]":['H','H','H','D','D','D','H','H','H','H'],"['as',6]":['H','H','D','D','D','D','H','H','H','H'],"['as',7]":['H','R','D','D','D','D','R','R','H','H'],'8moins':['H','H','H','H','H','H','H','H','H','H'],'9':['H','H','D','D','D','D','H','H','H','H'],'10':['H','D','D','D','D','D','D','D','D','H'],'11':['H','D','D','D','D','D','D','D','D','D'],'12':['H','H','H','R','R','R','H','H','H','H'],'13':['H','R','R','R','R','R','H','H','H','H'],'14':['H','R','R','R','R','R','H','H','H','H'],'15':['H','R','R','R','R','R','H','H','H','H'],'16':['H','R','R','R','R','R','H','H','H','H'],'17plus':['R','R','R','R','R','R','R','R','R','R'],}

def init_deck(n):
    deck = []
    for couleur in couleurs:
        for nombre in nombres:
            deck.append([nombre,couleur])
    return n*deck

def melanger_deck(deck):
    return sample(deck,len(deck))


def ajouter_points(points,carte):
    pts = points
    if carte[0] == 'as':
        if pts+11>21:
            pts+=1
        else :
            pts += 11
    elif type(carte[0]) == str:
        pts+=10
    else :
        pts += carte[0]
    return pts


deck_initial = init_deck(6)
deck = melanger_deck(deck_initial)
while wallet>0:
    print('------------------------------------------')
    print(wallet)
    mise = float(input('Combien voulez vous miser ?'))
    while mise > wallet:
        mise = float(input('Vous ne pouvez miser plus que ce que vous avez. Combien voulez-vous miser ?'))
    wallet -= mise
    main = []
    main.append(deck.pop(0))
    if len(deck) <= 1:
        deck = melanger_deck(deck_initial)
    main.append(deck.pop(1))
    croupier = [deck.pop(0)]
    if len(deck) == 0:
        deck = melanger_deck(deck_initial)
    points = 0
    points_croupier = 0
    for carte in main:
        points = ajouter_points(points,carte)
    points_croupier = ajouter_points(points_croupier, croupier[0])
    print('main :',main)
    print('points :',points)
    print('main croupier :',croupier)
    print('points croupier :',points_croupier)
    if croupier[0][0] == 'as':
        assurance = int(input("Voulez-vous prendre l'assurance ? Non(0)/Oui(1)"))
        if assurance:
            wallet-=0.5*mise
    split = 0
    if main[0][0] == main[1][0] and wallet > mise:
        split = int(input('Voulez-vous split ? Non(0)/Oui(1)'))
    if split:
        wallet -= mise
        main1 = [main[0],deck.pop(0)]
        if len(deck) == 0:
            deck = melanger_deck(deck_initial)
        main2 = [main[1],deck.pop(0)]
        if len(deck) == 0:
            deck = melanger_deck(deck_initial)
        points1 = 0
        points2 = 0
        for carte in main1:
            points1 = ajouter_points(points1, carte)
        for carte in main2:
            points2 = ajouter_points(points2, carte)
        print('main1 :', main1)
        print('points1 :', points1)

        action1 = int(input('Voulez vous rester(0)/tirer(1)/doubler(2)'))
        if action1 == 2 and mise > wallet:
            action1 = int(input('Vous ne pouvez pas miser plus que ce que vous avez. Voulez-vous rester(0)/tirer(1)?'))
        if action1 == 2:
            wallet -= mise
            mise *= 2
            main1.append(deck.pop(0))
            if len(deck) == 0:
                deck = melanger_deck(deck_initial)
            points1 = ajouter_points(points1, main1[-1])
            print('main1 :', main1)
            print('points1 :', points1)
        elif action1 == 1:
            tirer = True
            while points1 <= 21 and tirer:
                main1.append(deck.pop(0))
                if len(deck) == 0:
                    deck = melanger_deck(deck_initial)
                points1 = ajouter_points(points1, main1[-1])
                print('main1 :', main1)
                print('points1 :', points1)
                tirer = int(input('Voulez-vous tirer à nouveau ? Non(0)/Oui(1)'))

        print('main2 :', main2)
        print('points2 :', points2)

        action2 = int(input('Voulez vous rester(0)/tirer(1)/doubler(2)'))
        if action2 == 2 and mise > wallet:
            action2 = int(input('Vous ne pouvez pas miser plus que ce que vous avez. Voulez-vous rester(0)/tirer(1)?'))
        if action2 == 2:
            wallet -= mise
            mise *= 2
            main2.append(deck.pop(0))
            if len(deck) == 0:
                deck = melanger_deck(deck_initial)
            points2 = ajouter_points(points2, main2[-1])
            print('main2 :', main2)
            print('points2 :', points2)
        elif action2 == 1:
            tirer = True
            while points2 <= 21 and tirer:
                main2.append(deck.pop(0))
                if len(deck) == 0:
                    deck = melanger_deck(deck_initial)
                points2 = ajouter_points(points2, main2[-1])
                print('main2 :', main2)
                print('points2 :', points2)
                tirer = int(input('Voulez-vous tirer à nouveau ? Non(0)/Oui(1)'))

        if points1 <= 21 or points2 <= 21:
            while points_croupier < 17:
                croupier.append(deck.pop(0))
                if len(deck) == 0:
                    deck = melanger_deck(deck_initial)
                points_croupier = ajouter_points(points_croupier, croupier[-1])
                print('main croupier :', croupier)
                print('points croupier :', points_croupier)

            if (points_croupier > 21 or points1 > points_croupier) and points1 <= 21:
                wallet += 2 * mise
            elif points1 == points_croupier or (points_croupier == 21 and len(croupier)==2 and assurance):
                wallet += mise

            if (points_croupier > 21 or points2 > points_croupier) and points2 <= 21:
                wallet += 2 * mise
            elif points2 == points_croupier or (points_croupier == 21 and len(croupier)==2 and assurance):
                wallet += mise

    else :
        action = int(input('Voulez vous rester(0)/tirer(1)/doubler(2)'))
        if action == 2 and mise > wallet :
            action= int(input('Vous ne pouvez pas miser plus que ce que vous avez. Voulez-vous rester(0)/tirer(1)?'))
        if action == 2:
            wallet -= mise
            mise *= 2
            main.append(deck.pop(0))
            if len(deck) == 0:
                deck = melanger_deck(deck_initial)
            points = ajouter_points(points,main[-1])
            print('main :', main)
            print('points :', points)
        elif action == 1:
            tirer = True
            while points <= 21 and tirer:
                main.append(deck.pop(0))
                if len(deck) == 0:
                    deck = melanger_deck(deck_initial)
                points = ajouter_points(points,main[-1])
                print('main :', main)
                print('points :', points)
                if points>21:
                    break
                tirer = int(input('Voulez-vous tirer à nouveau ? Non(0)/Oui(1)'))
        if points <= 21:
            while points_croupier<17:
                croupier.append(deck.pop(0))
                if len(deck) == 0:
                    deck = melanger_deck(deck_initial)
                points_croupier = ajouter_points(points_croupier,croupier[-1])
                print('main croupier :', croupier)
                print('points croupier :', points_croupier)

            if points_croupier > 21 or points > points_croupier:
                if points == 21 and len(main)==2:
                    wallet += 2.5*mise
                else :
                    wallet += 2*mise

            elif points==points_croupier or (points_croupier == 21 and len(croupier)==2 and assurance):
                wallet+=mise