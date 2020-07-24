import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=int)
parser.add_argument("--periods", type=int)
args = parser.parse_args()

type_choices = ['annuity', 'diff']
calc_choices = ['a', 'd', 'p', 'n']
calculation = ''

if args.type is None or args.type not in type_choices:
    print("Incorrect parameters")
elif len(vars(args)) < 4:
    print("Incorrect parameters")
elif args.interest is None or args.interest < 0:
    print("Incorrect parameters")
elif args.payment is not None and args.payment < 0:
    print("Incorrect parameters")
elif args.principal is not None and args.principal < 0:
    print("Incorrect parameters")
elif args.periods is not None and args.periods < 0:
    print("Incorrect parameters")

elif args.type == 'diff':
    if args.payment is not None:
        print("Incorrect parameters")
    else:
        calculation = 'd'
else:
    if args.principal is None:
        calculation = 'p'
    elif args.payment is None:
        calculation = 'a'
    elif args.periods is None:
        calculation = 'n'


if calculation in calc_choices:
    i = args.interest / 100 / 12

    if calculation == 'd':
        sum = 0
        for j in range(args.periods):
            m = j + 1
            d = math.ceil(args.principal / args.periods + i * (args.principal - args.principal * (m - 1) / args.periods))
            sum += d
            print(f'Month {m}: paid out {d}')
        print()
        print("Overpayment = " + str(sum - args.principal))
    elif calculation == 'n':
        args.periods = math.ceil(math.log(args.payment / (args.payment - i * args.principal), (1 + i)))
        months = args.periods % 12
        years = args.periods // 12
        
        message = 'You need'
        if years == 1:
            message += ' 1 year'
        elif years > 1:
            message += ' ' + str(years) + ' years'
        if months == 1:
            message += ' and 1 month'
        elif months > 1:
            message += ' and ' + str(months) + ' months'
        
        print(message + ' to repay this credit!')
        print("Overpayment = " + str(args.payment * args.periods - args.principal))
    elif calculation == 'a':
        args.payment = math.ceil(args.principal * (i / (1 - pow(1 + i, -args.periods))))
        print(f'Your annuity payment = {args.payment}!')
        print("Overpayment = " + str(args.payment * args.periods - args.principal))
    else:
        args.principal = math.ceil(args.payment / (i / (1 - pow(1 + i, -args.periods))))
        print(f'Your credit principal = {args.principal}!')
        print("Overpayment = " + str(args.payment * args.periods - args.principal))