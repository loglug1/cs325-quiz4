import argparse


def main():
    parser = argparse.ArgumentParser(prog='Arguer', description='IDK what this does', epilog='Cam\s Program')

    parser.add_argument('name', type=str, help='Name of person to argue with')
    parser.add_argument('-s', '--stupid', help='Makes the arguer stupid', action='store_true')

    args = parser.parse_args()

    if args.stupid:
        print(f'{args.name}: The sky is red. Convince me otherwise.')
    else:
        print(f'{args.name}: The sky is blue. Convince me otherwise.')


if __name__=="__main__":
    main()