#!/usr/bin/env python3
#
# Given n pairs of parentheses, write a function to generate all combinations of
# well-formed parentheses.

def generate_parentheses(n):

    def _generate_parentheses(paren_string, open_remaining, close_remaining,
                              valid_parens=[]):
        if open_remaining:
            _generate_parentheses(paren_string + '(', open_remaining - 1, 
                                  close_remaining)
        if close_remaining > open_remaining:
            _generate_parentheses(paren_string + ')', open_remaining, 
                                  close_remaining - 1)
        if not close_remaining:
            valid_parens.append(paren_string)
        return valid_parens

    return _generate_parentheses('', n, n)


# Tests
print(generate_parentheses(0))
print(generate_parentheses(1))
print(generate_parentheses(3))
# print(generate_parentheses(30))

