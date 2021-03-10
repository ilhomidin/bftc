from pampy import _, match

from .tokens import (GetCellValueToken, InvalidSyntaxToken, LoopEndToken,
                     LoopStartToken, MutateCellValueToken, NextCellToken,
                     PreviousCellToken, PutCellValueToken, Token)


def tokenize(char: str) -> Token:
    return match(char,
        "+", MutateCellValueToken(1),
        "-", MutateCellValueToken(-1),
        ".", PutCellValueToken(),
        ",", GetCellValueToken(),
        "[", LoopStartToken(),
        "]", LoopEndToken(),
        ">", NextCellToken(),
        "<", PreviousCellToken(),
        _, InvalidSyntaxToken()
    )


__all__ = ["tokenize"]
