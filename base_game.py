def main():
    print_rules();
    game_loop();
    return 0;

def game_loop(rocks=21):
    pc_rocks=0;
    print("Камінчиків на полі: ", rocks);

    while True:

        p_inp = get_rocks();
        print("\n");

        if exit(p_inp):
                print("Гру завершено.");
                break;

        p_rocks = int(p_inp);
        rocks = rocks - p_rocks;
        print("Ваш хід: ", p_rocks,"\nКамінчиків лишилось:", rocks, "\n");

        if rocks < 1:
            print("Ви програли!")
            break;
            
        pc_rocks = pc_turn(p_rocks);
        rocks = rocks - pc_rocks;
        print("Хід компутера: ", pc_rocks, "\nКамінчиків лишилось: ",rocks, "\n");

        if rocks < 1:
            print("Ви перемогли!!!")
            break;

    return 0;

def exit(p_inp):
    if p_inp.lower() == "вийти":
        return 1;
    return 0;

def get_rocks(d=0):
    p_rocks = ""
    while p_rocks not in ['1', '2', '3', '4', 'вийти',]:
        p_rocks = input("Скільки камінчиків візьмете? : ").lower();
    return p_rocks;

def pc_turn(p_rocks):
    return 5-p_rocks;

def print_rules():
    print('''Привіт! \nІ вітаю у класичній грі Баше.
    Умови гри: є купка з 21 камінчика.
    Кожен гравець може брати 1, 2, 3 або 4 камінчики
    за хід. Програє той, хто візьме останні/й.
    Щоб завершити гру напишіть "вийти".
    Перший хід за вами!\n''');

main();
