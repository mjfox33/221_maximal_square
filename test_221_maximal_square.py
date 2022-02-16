from code_221_maximal_square import Solution

def test_example_1():
    s = Solution()
    assert s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4

def test_example_2():
    s = Solution()
    assert s.maximalSquare([["0","1"],["1","0"]]) == 1

def test_failed():
    s = Solution()
    assert s.maximalSquare([
        ["1","0","1","1","0","1"],
        ["1","1","1","1","1","1"],
        ["0","1","1","0","1","1"],
        ["1","1","1","0","1","0"],
        ["0","1","1","1","1","1"],
        ["1","1","0","1","1","1"]])