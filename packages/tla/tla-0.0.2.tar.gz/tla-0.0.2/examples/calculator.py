"""Interpret arithmetic TLA+ expressions."""
import tla


def main():
    """Entry point."""
    expression = '1 + 2 * 3.5'
    number = calculate(expression)
    print(number)


def calculate(
        expression:
            str
        ) -> float:
    """Return the numeric value of `expression`."""
    tree = tla.parse_expr(expression)
    return evaluate(tree)


def evaluate(
        tree
        ) -> float:
    match tree.symbol.name:
        case 'OPERATOR_APPLICATION':
            args = list(map(
                evaluate,
                tree.arguments))
            match tree.operator:
                case '+':
                    assert len(args) == 2, args
                    return args[0] + args[1]
                case '-':
                    # unary minus ?
                    if len(args) == 1:
                        return args[0]
                    assert len(args) == 2, args
                    return args[0] - args[1]
                case '*':
                    assert len(args) == 2, args
                    return args[0] * args[1]
                case '/':
                    assert len(args) == 2, args
                    return args[0] / args[1]
                case op:
                    raise NotImplementedError(
                        f'operator `{op}`')
        case 'INTEGRAL_NUMERAL':
            return int(tree.value)
        case 'FLOAT_NUMERAL':
            return float(tree.value)
        case symbol:
            raise ValueError(symbol)


if __name__ == '__main__':
    main()
