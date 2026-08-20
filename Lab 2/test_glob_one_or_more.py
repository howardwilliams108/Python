from glob_lit import Lit
from glob_one_or_more import OneorMore

def test_one_or_more_empty():
    assert not OneorMore().match("") #this is done to see if  /+/ matches "" 

def test_one_or_more_matches_entire_string():  #this is done to see if /+/ matches "abc"
    assert OneorMore().match("abc")

def test_one_or_more_matches_as_prefix():  #this is done to see if /+def/ matches "abcdef" 
    assert OneorMore(Lit("def")).match("abcdef")

def test_one_or_more_matches_as_suffix():  #this is done to see if  /abc+/ matches "abcdef"
    assert Lit("abc", OneorMore()).match("abcdef")

def test_one_or_more_matches_interior():  #this is done to see if /a+c/ matches "abc" 
    assert Lit("a", OneorMore(Lit("c"))).match("abc")
